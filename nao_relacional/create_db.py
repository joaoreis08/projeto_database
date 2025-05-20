from pymongo import MongoClient

def criar_nao_relacional():
    client = MongoClient('localhost', 27017)
    db = client['seu_banco_de_dados']
    comentarios = db['comentarios']

