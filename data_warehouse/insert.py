import psycopg2
import ZODB, ZODB.FileStorage
from objeto_relacional.gerar_dados import gerar_historico_estoque,gerar_historico_precos,gerar_lojas,gerar_fatos_vendas
from objeto_relacional.classes import Cliente,Produto,Venda
import random
from faker import Faker

fake = Faker('pt_BR')


def inserir_dados_postgres(clientes,produtos,vendas,estoques,precos,Cliente,Produto,Venda):
    conn = psycopg2.connect("dbname='data_warehouse' user='postgres' host='localhost' password='123'")
    cur = conn.cursor()


    storage = ZODB.FileStorage.FileStorage('varejo_projeto')
    db = ZODB.DB(storage)
    connection = db.open()
    root = connection.root()

    # Extraia os dados
    clientes = [c for c in root.values() if isinstance(c, Cliente)]
    produtos = [p for p in root.values() if isinstance(p, Produto)]
    vendas = [v for v in root.values() if isinstance(v, Venda)]
    lojas = gerar_lojas()
    fatos_vendas = gerar_fatos_vendas()


    for loja in lojas:
        cur.execute("""
        INSERT INTO dim_loja (nome, localizacao) VALUES (%s, %s)
        """, (loja['nome'], loja['localizacao']))
   

    # Inserção de Clientes
    for cliente in clientes:
        cur.execute("""
        INSERT INTO dim_cliente (cliente_id, nome, email, telefone)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (cliente_id) DO NOTHING
        """, (cliente.id, cliente.nome, cliente.email, cliente.telefone))

    conn.commit()


    # Inserção de Produtos
    for produto in produtos:
        cur.execute("""
        INSERT INTO dim_produto (nome,produto_id, descricao, preco) VALUES (%s,%s, %s, %s)
        """, (produto.nome,produto.produto_id, produto.descricao , produto.preco))  

    for venda in fatos_vendas:
        # Inserir e obter 'data_id'
        cur.execute("""
        INSERT INTO dim_tempo (data) VALUES (%s)
        ON CONFLICT (data) DO NOTHING RETURNING data_id
        """, (venda['data'],))
        
        data_id_result = cur.fetchone()
        if data_id_result:
            data_id = data_id_result[0]

            cur.execute("""
            INSERT INTO fato_vendas (data_id, produto_id, cliente_id, loja_id, quantidade, total)
            VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                data_id,
                venda['produto_id'],
                venda['cliente_id'],
                venda['loja_id'],
                venda['quantidade'],
                venda['quantidade'] * fake.random_number(digits=3)
            ))

    conn.commit()


    for preco in precos:
        cur.execute("""
        SELECT 1 FROM historico_precos WHERE produto_id = %s AND data = %s
        """, (preco[0], preco[1]))
        if not cur.fetchone():
            cur.execute("""
            INSERT INTO historico_precos (produto_id, data, preco) 
            VALUES (%s, %s, %s)
            """, preco)

    for estoque in estoques:
        cur.execute("""
        SELECT 1 FROM historico_estoque WHERE produto_id = %s AND data = %s
        """, (estoque[0], estoque[1]))
        if not cur.fetchone():
            cur.execute("""
            INSERT INTO historico_estoque (produto_id, data, quantidade) 
            VALUES (%s, %s, %s)
            """, estoque)

    # Commitar e fechar a conexão
    conn.commit()
    cur.close()
    conn.close()