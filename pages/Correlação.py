import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_title="Correlação",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.write('Correlação')

df = pd.read_csv(r'C://Users//Laisson Bruno//Desktop//tp//dados//CancerDataBase_Final_2.csv')

num_cols = ['GDP per capita (current US$)', 'Current health expenditure per capita (current US$)', 'Deaths']
corr_df = df[num_cols]
region_data = df.groupby('Region')[['GDP per capita (current US$)', 'Current health expenditure per capita (current US$)', 'Deaths']].mean().reset_index()
entity_data = df.groupby('Entity')[['GDP per capita (current US$)', 'Current health expenditure per capita (current US$)', 'Deaths', 'lat', 'lon']].mean().reset_index()


fig1 = px.scatter(region_data, x='GDP per capita (current US$)', y='Current health expenditure per capita (current US$)', color='Region', hover_name='Region', size='Deaths', title='Relação entre PIB per Capita, Investimento em Saúde per Capita e Mortes por Região')
st.plotly_chart(fig1, use_container_width=True)

fig2 = px.scatter(entity_data, x='GDP per capita (current US$)', y='Current health expenditure per capita (current US$)', color='Entity', hover_name='Entity', size='Deaths', title='Relação entre PIB per Capita, Investimento em Saúde per Capita e Mortes por Entidade')
st.plotly_chart(fig2, use_container_width=True)