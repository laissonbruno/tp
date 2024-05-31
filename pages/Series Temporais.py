import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_title="Series Temporais",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.write('Series Temporais')

df = pd.read_csv(r'C://Users//Laisson Bruno//Desktop//tp//dados//CancerDataBase_Final_2.csv')


mortes_data = df[['Year', 'Deaths']]
mortes_anuais = mortes_data.groupby('Year')['Deaths'].mean().reset_index()

# Criar um gráfico de série temporal
fig1 = px.line(mortes_anuais, x='Year', y='Deaths', title='Série Temporal de Mortes')
st.plotly_chart(fig1, use_container_width=True)


# Selecionar apenas as colunas necessárias
gastos_saude_data = df[['Region', 'Current health expenditure per capita (current US$)']]

# Agrupar os dados por região e calcular a média
gastos_saude_data = gastos_saude_data.groupby('Region')['Current health expenditure per capita (current US$)'].mean().reset_index()

# Criar um gráfico de barras
fig2 = px.bar(gastos_saude_data, x='Region', y='Current health expenditure per capita (current US$)', title='Média de Gastos em Saúde per Capita por Região')
st.plotly_chart(fig2, use_container_width=True)