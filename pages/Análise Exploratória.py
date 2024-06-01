import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np


st.set_page_config(
    page_title="Tabela",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

df = pd.read_csv(r'C://Users//Laisson Bruno//Desktop//tp//dados//CancerDataBase_Final_2.csv')

col1, col2, col3 = st.columns(3)  # Primeira linha com três colunas
col4, col5 = st.columns(2)  # segunda linha com três colunas
col6, col7  = st.columns(2)  # segunda linha com três colunas
col8, col9  = st.columns(2)  # segunda linha com três colunas
col10, col11  = st.columns(2)  # segunda linha com três colunas


col2.write("# Análise exploratória")


most_deaths = df.groupby('Entity')['Deaths'].mean().sort_values(ascending=False).head(5)
least_deaths = df.groupby('Entity')['Deaths'].mean().sort_values(ascending=True).head(5)
max_gdp_countries = df.groupby('Entity')['GDP per capita (current US$)'].mean().sort_values(ascending=False).head(5)
min_gdp_countries = df.groupby('Entity')['GDP per capita (current US$)'].mean().sort_values(ascending=True).head(5)
most_health_exp = df.groupby('Entity')['Current health expenditure per capita (current US$)'].mean().sort_values(ascending=False).head(5)
least_health_exp = df.groupby('Entity')['Current health expenditure per capita (current US$)'].mean().sort_values(ascending=True).head(5)


col4.write("Países com mais mortes:")
fig1 = px.bar(most_deaths, x=most_deaths.index, y='Deaths', labels={'x':'Países', 'y':'Total de Mortes'})
col4.plotly_chart(fig1)

col5.write("Países com menos mortes:")
fig2 = px.bar(least_deaths, x=least_deaths.index, y='Deaths', labels={'x':'Países', 'y':'Total de Mortes'})
col5.plotly_chart(fig2)

col6.write("Países com maior PIB:")
fig3 = px.bar(max_gdp_countries, x=max_gdp_countries.index, y='GDP per capita (current US$)', labels={'x':'Países', 'y':'PIB per capita'})
col6.plotly_chart(fig3)

col7.write("Países com menor PIB:")
fig4 = px.bar(min_gdp_countries, x=min_gdp_countries.index, y='GDP per capita (current US$)', labels={'x':'Países', 'y':'PIB per capita'})
col7.plotly_chart(fig4)


col8.write("Países que gastam mais com saúde:")
fig5 = px.bar(most_health_exp, x=most_health_exp.index, y='Current health expenditure per capita (current US$)', labels={'x':'Países', 'y':'Gasto com saúde per capita'})
col8.plotly_chart(fig5)
 
col9.write("Países que gastam menos com saúde:")
fig6 = px.bar(least_health_exp, x=least_health_exp.index, y='Current health expenditure per capita (current US$)', labels={'x':'Países', 'y':'Gasto com saúde per capita'})
col9.plotly_chart(fig6)



st.write(
    """
## Análise da Mortalidade por Câncer e Investimento em Saúde Global

Com base nos dados apresentados, observa-se que a mortalidade por câncer varia significativamente entre os países, com a China liderando em número de mortes, enquanto países menores como Nauru e Tuvalu registram as menores taxas. No entanto, é importante ressaltar que a quantidade de mortes por câncer pode não estar diretamente ligada ao PIB per capita e aos gastos em saúde per capita. Mesmo países com alto investimento e PIB alto, como os Estados Unidos e Suíça, podem ter um grande número de mortes por câncer. Isso se deve ao fato de que, quanto mais habitantes um país tem, consequentemente mais mortes ele terá, como é o caso da Índia e da China.

O **PIB per capita** reflete a disparidade econômica, com nações como Mônaco e Luxemburgo apresentando os maiores valores, indicando maior capacidade de investimento em saúde. Os **gastos em saúde per capita** seguem essa tendência, com países como os Estados Unidos e Suíça investindo mais, em contraste com nações como a República Democrática do Congo e Etiópia, que têm recursos limitados para a saúde.

Esses insights destacam a interconexão entre saúde, economia e investimento em cuidados médicos em escala global, mas também ressaltam que o número de mortes por câncer não depende apenas desses fatores. Outros elementos, como o tamanho da população e a incidência da doença, também desempenham um papel importante.
"""
)