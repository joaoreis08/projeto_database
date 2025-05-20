import ZODB, ZODB.FileStorage
import transaction

def inserir_dados(clientes,produtos,estoque_items,vendas,Cliente,Produto,Estoque,Venda):
    # Inicializar o Banco de Dados
    storage = ZODB.FileStorage.FileStorage('varejo_projeto')
    db = ZODB.DB(storage)
    connection = db.open()
    root = connection.root()


    # Inserir Clientes no Banco de Dados
    for cliente_data in clientes:
        cliente = Cliente(**cliente_data)
        root[f'cliente_{cliente_data["id"]}'] = cliente

    # Inserir Produtos e Estoque no Banco de Dados
    for produto_data, estoque_data in zip(produtos, estoque_items):
        produto = Produto(
            nome=produto_data["nome"],
            produto_id=produto_data["produto_id"],  # Incluído o produto_id
            preco=produto_data["preco"],
            descricao=produto_data["descricao"]
        )
        # Use produto_id para armazenar no root
        root[f'produto_{produto_data["produto_id"]}'] = produto
        estoque = Estoque(produto, estoque_data['quantidade'])
        root[f'estoque_{produto_data["produto_id"]}'] = estoque

    # Inserir Vendas no Banco de Dados
    for venda_data in vendas:
        cliente = root.get(f'cliente_{venda_data["cliente_id"]}')
        if cliente:
            venda = Venda(id=venda_data['id'], cliente=cliente, data=venda_data['data'])
            root[f'venda_{venda_data["id"]}'] = venda

    # Persistir mudanças
    transaction.commit()
    connection.close()
    db.close()