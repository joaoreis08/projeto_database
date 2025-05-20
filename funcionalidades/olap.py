import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

# Definição da conexão com o banco de dados
engine = create_engine('postgresql+psycopg2://postgres:123@localhost/data_warehouse')

# Importar tabelas para DataFrames do Pandas
dim_cliente_df = pd.read_sql('SELECT * FROM dim_cliente', engine)
dim_loja_df = pd.read_sql('SELECT * FROM dim_loja', engine)
dim_produto_df = pd.read_sql('SELECT * FROM dim_produto', engine)
dim_tempo_df = pd.read_sql('SELECT * FROM dim_tempo', engine)
fatos_vendas_df = pd.read_sql('SELECT * FROM fato_vendas', engine)
historico_estoques_df = pd.read_sql('SELECT * FROM historico_estoque', engine)
historico_precos_df = pd.read_sql('SELECT * FROM historico_precos', engine)

dim_tempo_df['data'] = pd.to_datetime(dim_tempo_df['data'])
dim_tempo_df['ano'] = dim_tempo_df['data'].dt.year
dim_tempo_df['mes'] = dim_tempo_df['data'].dt.month
dim_tempo_df['dia'] = dim_tempo_df['data'].dt.day
dim_tempo_df['trimestre'] = dim_tempo_df['data'].dt.quarter


analise_df = fatos_vendas_df.merge(dim_tempo_df, on='data_id')

# Certificar que a coluna 'data' está como índice e no formato datetime
analise_df['data'] = pd.to_datetime(analise_df['data'])
analise_df.set_index('data', inplace=True)

# Agrupar por mês e somar
vendas_por_mes = analise_df['quantidade'].resample('M').sum()

# Plotar
vendas_por_mes.plot(kind='line', title='Vendas por Mês', xlabel='Mês', ylabel='Quantidade de Vendas')

# Mostrar o gráfico
plt.show()

analise_df2 = fatos_vendas_df.merge(dim_loja_df, on='loja_id')

# Agrupar por localização e somar
vendas_por_local = analise_df2.groupby('localizacao')['quantidade'].sum().head()

# Plotar
vendas_por_local.plot(kind='bar', title='Vendas por Localização', xlabel='Localização', ylabel='Quantidade de Vendas')

# Mostrar o gráfico
plt.xticks(rotation=45)
plt.show()

# Mesclar as tabelas para incluir os produtos
analise_df3 = fatos_vendas_df.merge(dim_produto_df, on='produto_id')

# Agrupar por produto e somar as vendas
vendas_por_produto = analise_df3.groupby('nome')['quantidade'].sum()

# Plotar
vendas_por_produto.plot(kind='bar', title='Vendas por Produto', xlabel='Produto', ylabel='Quantidade de Vendas')

# Mostrar o gráfico
plt.xticks(rotation=45)
plt.show()
