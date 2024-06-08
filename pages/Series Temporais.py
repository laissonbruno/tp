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


st.sidebar.success("Faça ao minimo duas seleções nos filtros abaixo.")

# Cria a barra lateral
with st.sidebar:

    # Container para regiões
    container1 = st.container(height=100)
    all1 = st.checkbox("Selecione todas regiões", value=True)

    if all1:
        selected_options1 = container1.multiselect("Selecione uma ou mais regiões:", df["Region"].unique(), df["Region"].unique())
    else:
        selected_options1 = container1.multiselect("Selecione uma ou mais regiões:", df["Region"].unique())

    # Container para anos
    container2 = st.container(height=100)
    all2 = st.checkbox("Selecione todos anos", value=True)

    if all2:
        selected_options2 = container2.multiselect("Selecione um ou varios anos:", df["Year"].unique(), df["Year"].unique())
    else:
        selected_options2 = container2.multiselect("Selecione um ou varios anos:", df["Year"].unique())

    # Container para tipos de cancer
    container3 = st.container(height=100)
    all3 = st.checkbox("Selecione todos os tipos", value=True)

    if all3:
        selected_options3 = container3.multiselect("Selecione um ou mais tipos de cancer:", df["Types"].unique(), df["Types"].unique())
    else:
        selected_options3 = container3.multiselect("Selecione um ou mais tipos de cancer:", df["Types"].unique())

# Filtra os dados com base nas seleções
filtered_df = df[
    (df["Region"].isin(selected_options1)) &
    (df["Year"].isin(selected_options2)) &
    (df["Types"].isin(selected_options3))
]

# Gráfico de Linha com média do "GDP per capita (current US$)" por país ao longo dos anos
fig = px.line(filtered_df.groupby(["Year", "Region"])["GDP per capita (current US$)"].mean().reset_index(), x="Year", y="GDP per capita (current US$)", color="Region", title="Média do PIB per capita ao longo dos anos")
fig.update_traces(mode='markers+lines')
st.plotly_chart(fig)


# Gráfico de Linha com média de "Deaths" por país ao longo dos anos
fig = px.area(filtered_df.groupby(["Year", "Region"])["Deaths"].mean().reset_index(), x="Year", y="Deaths", color="Region", title="Média de mortes ao longo dos anos - Gráfico de área")
fig.update_traces(mode='markers+lines')
st.plotly_chart(fig)

