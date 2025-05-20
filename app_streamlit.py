import streamlit as st
import pandas as pd
import altair as alt
from objeto_relacional.gerar_dados import gerar_clientes, gerar_produtos, gerar_fatos_vendas, gerar_lojas

# Carregar dados simulados
clientes_df = pd.DataFrame(gerar_clientes())
produtos_df = pd.DataFrame(gerar_produtos())
fatos_vendas_df = pd.DataFrame(gerar_fatos_vendas())
lojas_df = pd.DataFrame(gerar_lojas())

# KPIs
total_vendas = fatos_vendas_df['quantidade'].sum()
ticket_medio = fatos_vendas_df['quantidade'].mean()
total_clientes = fatos_vendas_df['cliente_id'].nunique()

st.title("Dashboard de Vendas")

# Mostrar KPIs
st.metric(label="Total de Vendas", value=f"{total_vendas}")
st.metric(label="Ticket Médio", value=f"{ticket_medio:.2f}")
st.metric(label="Total de Clientes", value=f"{total_clientes}")

# Vendas por Categoria de Produto
vendas_merge = fatos_vendas_df.merge(produtos_df, on='produto_id')
categorias_grouped = vendas_merge.groupby('nome')['quantidade'].sum().reset_index()
chart = alt.Chart(categorias_grouped).mark_bar().encode(
    x='nome',
    y='quantidade'
).properties(title="Vendas por Produto")

st.altair_chart(chart, use_container_width=True)

# Drill-Down por Tempo (Vendas Mensais)
fatos_vendas_df['data'] = pd.to_datetime(fatos_vendas_df['data'])
vendas_por_mes = fatos_vendas_df.resample('M', on='data')['quantidade'].sum().reset_index()

line_chart = alt.Chart(vendas_por_mes).mark_line().encode(
    x='data',
    y='quantidade'
).properties(title="Vendas por Mês")

st.altair_chart(line_chart, use_container_width=True)

# Vendas por Localização
vendas_loc = fatos_vendas_df.merge(lojas_df, on='loja_id')
loc_grouped = vendas_loc.groupby('localizacao')['quantidade'].sum().reset_index()
loc_chart = alt.Chart(loc_grouped).mark_bar().encode(
    x='localizacao',
    y='quantidade'
).properties(title="Vendas por Localização")

st.altair_chart(loc_chart, use_container_width=True)

# Tabelas Interativas
st.subheader("Detalhes das Vendas")
st.dataframe(fatos_vendas_df)