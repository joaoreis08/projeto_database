
# Projeto Database Dashboard
Este projeto consiste em um dashboard de visualização de dados de vendas, desenvolvido usando Streamlit e dados simulados gerados com Faker.

# Descrição
O projeto foi criado para visualizar KPIs de vendas, gerar relatórios analíticos e permitir exploração de dados através de consultas OLAP. As principais funcionalidades incluem:

- KPIs de Vendas: Total de vendas, ticket médio e número de clientes únicos.
- Relatórios Analíticos: Gráficos de vendas por categoria de produto e localização.
- Consultas OLAP: Drill-down de vendas por tempo.
- Visualização Interativa: Utilizando Streamlit para interação em tempo real.

# Estrutura do Projeto

dash.py: Script principal do dashboard.
objeto_relacional/gerar_dados.py: Funções para gerar dados simulados.

# Pré-requisitos

Python 3.8 ou superior
Pip

# Instalação

# Clone o repositório:
git clone https://github.com/joaoreis08/projeto_database.git
cd projeto_database


# Crie e ative o ambiente virtual:
python -m venv venv
source venv/bin/activate  # No Windows use: venv\Scripts\activate


# Instale as dependências:
pip install -r requirements.txt



# Executando os Scripts

Executar o Streamlit App:
streamlit run app_streamlit.py

Isso vai abrir o aplicativo do Streamlit e mostrar o dashboard.

Gerar Dados e Configurar o Banco de Dados:

main.py: Este script gera dados fictícios usando a biblioteca Faker, insere os dados no banco objeto-relacional ZODB, cria as tabelas fato e dimensão no PostgreSQL, insere esses dados, e cria o banco não relacional no MongoDB, inserindo dados nele.




