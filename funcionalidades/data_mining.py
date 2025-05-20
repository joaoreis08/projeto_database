import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np


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

# Mesclar tabelas, supondo que 'data_id' é a chave
analise_df = fatos_vendas_df.merge(dim_tempo_df, on='data_id')

# Certificar de que 'data' está no formato datetime
analise_df['data'] = pd.to_datetime(analise_df['data'])


# Supor que você já tenha um DataFrame `clientes_df` com dados relevantes
# Exemplo: total de compras por cliente
dados_cluster = fatos_vendas_df.groupby('cliente_id')['quantidade'].sum().reset_index()

# K-means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
dados_cluster['cluster'] = kmeans.fit_predict(dados_cluster[['quantidade']])

# Visualização de resultados
print(dados_cluster.head())

# Preparação dos dados de treino
analise_df['meses'] = np.arange(len(analise_df))  # Criar índice temporal
X = analise_df[['meses']]
y = analise_df['quantidade']

# Dividir em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Regressão Linear
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Previsão
predicoes = modelo.predict(X_test)

# Avaliação do modelo
print("Coeficientes:", modelo.coef_)
print("Intercepto:", modelo.intercept_)