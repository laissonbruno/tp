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

st.sidebar.success("Faça ao minimo duas seleções nos filtros abaixo.")

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

filtered_df = df[
    (df["Region"].isin(selected_options1)) &
    (df["Year"].isin(selected_options2)) &
    (df["Types"].isin(selected_options3))
]

num_cols = ['GDP per capita (current US$)', 'Current health expenditure per capita (current US$)', 'Deaths']
corr_df = filtered_df[num_cols]
region_data = filtered_df.groupby('Region')[['GDP per capita (current US$)', 'Current health expenditure per capita (current US$)', 'Deaths']].mean().reset_index()
entity_data = filtered_df.groupby('Entity')[['GDP per capita (current US$)', 'Current health expenditure per capita (current US$)', 'Deaths', 'lat', 'lon']].mean().reset_index()


fig1 = px.scatter(region_data, x='GDP per capita (current US$)', y='Current health expenditure per capita (current US$)', color='Region', hover_name='Region', size='Deaths', title='Relação entre PIB per Capita, Investimento em Saúde per Capita e Mortes por Região')
st.plotly_chart(fig1, use_container_width=True)

with st.expander("Explicação"):
    st.write(
        """
        

        ## Análise de Correlação entre PIB per Capita, Gastos com Saúde per Capita e Óbitos por Região
        
        ### Correlação entre PIB per Capita e Gastos com Saúde per Capita
        Existem fortes correlações positivas entre o PIB per capita e os gastos com saúde per capita por região. Regiões com maior PIB per capita, como Europa e Américas, também apresentam maiores gastos com saúde per capita. Isso sugere que o crescimento econômico pode estar relacionado ao aumento nos gastos com saúde.

        ### Correlação entre Gastos com Saúde per Capita e Número de Óbitos
        Há uma correlação positiva entre os gastos com saúde per capita e o número de óbitos por região. Regiões com maiores gastos com saúde, como Europa e Américas, registram um maior número de óbitos. Isso pode indicar que regiões com melhores sistemas de saúde e maior acesso a cuidados médicos tendem a registrar mais óbitos, possivelmente por terem melhores sistemas de coleta de dados.

        """
    )

st.markdown("---")

fig2 = px.scatter(entity_data, x='GDP per capita (current US$)', y='Current health expenditure per capita (current US$)', color='Entity', hover_name='Entity', size='Deaths', title='Relação entre PIB per Capita, Investimento em Saúde per Capita e Mortes por País')
st.plotly_chart(fig2, use_container_width=True)

fig3 = px.scatter(filtered_df.groupby("Entity").agg({"GDP per capita (current US$)": "mean", "Current health expenditure per capita (current US$)": "mean"}).reset_index(), x="GDP per capita (current US$)", y="Current health expenditure per capita (current US$)", color="Entity", title='Relação entre PIB per Capita, Investimento em Saúde per Capita e Mortes por País - (Segunda forma para melhor visualização dos países)')
st.plotly_chart(fig3)

with st.expander("Explicação"):
    st.write(
        """

        """
    )


st.write(entity_data, x='GDP per capita (current US$)', y='Current health expenditure per capita (current US$)', color='Entity', hover_name='Entity', size='Deaths', title='Relação entre PIB per Capita, Investimento em Saúde per Capita e Mortes por Entidade - Forma 1')



