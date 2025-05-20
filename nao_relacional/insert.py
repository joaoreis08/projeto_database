from pymongo import MongoClient
import ZODB, ZODB.FileStorage
from objeto_relacional.classes import Cliente,Produto


def inserir_nao_relacional(clientes,produtos):
    storage = ZODB.FileStorage.FileStorage('varejo_projeto')
    db = ZODB.DB(storage)
    connection = db.open()
    root = connection.root()

    # Extração de dados necessários
    clientes = [c for c in root.values() if isinstance(c, Cliente)]
    produtos = [p for p in root.values() if isinstance(p, Produto)]

    # Conectar ao MongoDB
    client = MongoClient('localhost', 27017)
    db = client['seu_banco_de_dados']
    colecao_comentarios = db['comentarios']

    # Inserir Comentários de Exemplo
    for cliente in clientes:
        comentario = {
            'cliente_id': cliente.id,
            'nome': cliente.nome,
            'comentario': 'Este é um comentário de exemplo.'
        }
        colecao_comentarios.insert_one(comentario)

