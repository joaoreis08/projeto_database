import psycopg2

def criar_tabelas_dw():
    conn = psycopg2.connect("dbname='data_warehouse' user='postgres' host='localhost' password='123'")
    cur = conn.cursor()

    # Tabela Dimensão Tempo
    cur.execute("""
    CREATE TABLE IF NOT EXISTS dim_tempo (
        data_id SERIAL PRIMARY KEY,
        data DATE UNIQUE,
        ano INT,
        mes INT,
        dia INT,
        trimestre INT
    )
    """)

    # Tabela Dimensão Produto
    cur.execute("""
    CREATE TABLE IF NOT EXISTS dim_produto (
        produto_id SERIAL PRIMARY KEY,
        nome VARCHAR(255),
        descricao VARCHAR(255),
        preco NUMERIC
    )
    """)

    # Tabela Dimensão Cliente
    cur.execute("""
    CREATE TABLE IF NOT EXISTS dim_cliente (
        cliente_id SERIAL PRIMARY KEY,
        nome VARCHAR(255),
        email VARCHAR(255),
        telefone VARCHAR(255)
    )
    """)

    # Tabela Dimensão Loja
    cur.execute("""
    CREATE TABLE IF NOT EXISTS dim_loja (
        loja_id SERIAL PRIMARY KEY,
        nome VARCHAR(255),
        localizacao VARCHAR(255)
    )
    """)

    # Tabela de Fatos Vendas
    cur.execute("""
    CREATE TABLE IF NOT EXISTS fato_vendas (
        venda_id SERIAL PRIMARY KEY,
        data_id INT REFERENCES dim_tempo(data_id),
        produto_id INT REFERENCES dim_produto(produto_id),
        cliente_id INT REFERENCES dim_cliente(cliente_id),
        loja_id INT REFERENCES dim_loja(loja_id),
        quantidade INT,
        total NUMERIC
    )
    """)

    # Tabela Histórico de Preços
    cur.execute("""
    CREATE TABLE IF NOT EXISTS historico_precos (
        produto_id INT,
        data DATE,
        preco NUMERIC,
        PRIMARY KEY (produto_id, data)
    )
    """)

    # Tabela Histórico de Estoque
    cur.execute("""
    CREATE TABLE IF NOT EXISTS historico_estoque (
        produto_id INT,
        data DATE,
        quantidade INT,
        PRIMARY KEY (produto_id, data)
    )
    """)

    # Commit e feche a conexão
    conn.commit()
    cur.close()
    conn.close()