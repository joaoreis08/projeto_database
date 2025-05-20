from objeto_relacional.gerar_dados import gerar_clientes,gerar_estoque,gerar_historico_estoque,gerar_historico_precos,gerar_produtos,gerar_vendas
from objeto_relacional.conect_db import inserir_dados
from data_warehouse.create_db import criar_tabelas_dw
from data_warehouse.insert import inserir_dados_postgres
from nao_relacional.insert import inserir_nao_relacional
from nao_relacional.create_db import criar_nao_relacional
from objeto_relacional.classes import Estoque, Cliente, Produto, Venda




clientes = gerar_clientes()
produtos = gerar_produtos()
vendas = gerar_vendas()
estoque_items = gerar_estoque()
historico_precos = gerar_historico_precos()
historico_estoque = gerar_historico_estoque()

inserir_dados(clientes,produtos,estoque_items,vendas,Cliente,Produto,Estoque,Venda)
criar_tabelas_dw()
inserir_dados_postgres(clientes,produtos,vendas,historico_estoque,historico_precos,Cliente,Produto,Venda)
criar_nao_relacional()
inserir_nao_relacional(clientes,produtos)