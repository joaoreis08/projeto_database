from faker import Faker
import random
import faker_commerce

def gerar_clientes():
    fake = Faker('pt_BR') 
    clientes = []
    for _ in range(100):
        cliente = {
            'id': fake.random_int(min=1, max=100),
            'nome': fake.name(),
            'endereco': fake.address(),
            'email': fake.email(),
            'telefone': fake.phone_number()
        }
        clientes.append(cliente)
    return clientes

def gerar_produtos():
    fake = Faker('pt_BR') 
    fake.add_provider(faker_commerce.Provider)
    produtos = []
    for _ in range(100):
        produto = {
            'nome': fake.ecommerce_name(),  # Usando nome de produto de comércio
            'produto_id': fake.random_int(min=1, max=100),
            'preco': round(fake.pyfloat(left_digits=5, right_digits=2, positive=True), 2),
            'descricao': fake.paragraph()
        }
        produtos.append(produto)
    return produtos

def gerar_vendas():
    fake = Faker('pt_BR') 
    vendas = []
    for _ in range(100):
        venda = {
            'id': fake.random_int(min=1, max=100),
            'cliente_id': fake.random_int(min=1, max=100),
            'data': fake.date_time_this_year()
        }
        vendas.append(venda)
    return vendas

def gerar_estoque():
    fake = Faker('pt_BR') 
    estoque = []
    for _ in range(100):
        item_estoque = {
            'produto_id': fake.random_int(min=1, max=100),
            'quantidade': fake.random_int(min=1, max=100)
        }
        estoque.append(item_estoque)
    return estoque

def gerar_historico_precos():
    fake = Faker('pt_BR') 
    precos = []
    produtos_ids = [1, 2, 3, 4, 5] 
    for _ in range(100):
        produto_id = fake.random.choice(produtos_ids)
        data = fake.date_between(start_date='-1y', end_date='today')
        preco = round(fake.random.uniform(10.0, 100.0), 2)
        precos.append((produto_id, data, preco))
    return precos

def gerar_historico_estoque():
    fake = Faker('pt_BR') 
    estoques=[]
    produtos_ids = [1, 2, 3, 4, 5] 
    for _ in range(100):
        produto_id = fake.random.choice(produtos_ids)
        data = fake.date_between(start_date='-1y', end_date='today')
        quantidade = fake.random.randint(0, 100)
        estoques.append((produto_id, data, quantidade))
    return estoques 

def gerar_lojas():
    fake = Faker('pt_BR') 
    lojas = []
    for loja_id in range(1, 6):
        loja = {
            'loja_id': loja_id,
            'nome': fake.company(),
            'localizacao': fake.city()
        }
        lojas.append(loja)
    return lojas

def gerar_fatos_vendas():
    fake = Faker('pt_BR') 
    vendas = []
    for _ in range(1000):
        venda = {
            'venda_id': fake.unique.random_int(min=1, max=5000),
            'cliente_id': fake.random_int(min=1, max=100),
            'data': fake.date_this_year(),
            'produto_id': fake.random_int(min=1, max=100),
            'quantidade': random.choice([1, 2, 3, 4, 5]),
            'loja_id': fake.random_int(min=1, max=5)
        }
        vendas.append(venda)
    return vendas