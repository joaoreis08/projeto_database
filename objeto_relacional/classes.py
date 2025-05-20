import ZODB
import transaction
from persistent import Persistent

class Produto(Persistent):
    def __init__(self,nome,produto_id,preco,descricao):
        self.nome = nome
        self.produto_id=produto_id
        self.preco = preco
        self.descricao = descricao

    


class Cliente(Persistent):
    def __init__(self,id,nome,email,telefone,endereco):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.endereco = endereco

class Venda(Persistent):
    def __init__(self,id,cliente,data):
        self.id = id
        self.cliente = cliente 
        self.data = data        

class Estoque(Persistent):
    def __init__(self,produto,quantidade):
        self.produto = produto
        self.quantidade = quantidade
        

