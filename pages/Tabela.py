import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(
    page_title="Tabela",
    page_icon="📊",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Carrega o dataframe
df = pd.read_csv(r'C://Users//Laisson Bruno//Desktop//tp//dados//CancerDataBase_Final_2.csv')


# colunas e linhas
col1, col2, col3 = st.columns(3)
col4, col5 = st.columns(2)
col6, col7 = st.columns(2)


# Título
col2.title("Tabela")
col2.write("")
col2.write("")
col2.write("")

# Barra lateral
with st.sidebar:
    # Container para regiões
    container1 = st.container(height=100)
    all1 = st.checkbox("Selecione todos países", value=True)

    if all1:
        selected_options1 = container1.multiselect("Selecione um ou mais países:", df["Entity"].unique(), df["Entity"].unique())
    else:
        selected_options1 = container1.multiselect("Selecione um ou mais países:", df["Entity"].unique())

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
    (df["Entity"].isin(selected_options1)) &
    (df["Year"].isin(selected_options2)) &
    (df["Types"].isin(selected_options3))
]



# Defina uma função para determinar a ordem de grandeza
def determinar_ordem_grandeza(numero):
    if numero < 1000:
        return "centenas"
    elif numero < 1000000:
        return "milhares"
    elif numero < 1000000000:
        return "milhões"
    else:
        return "bilhões"

# Número de mortes
mortes = round(filtered_df["Deaths"].sum())
mortes_formatted = '{:,.0f}'.format(mortes).translate(str.maketrans(',.', '.,'))  # Sem casas decimais
ordem_mortes = determinar_ordem_grandeza(mortes)
col4.metric("Somatória do Número de Mortes", mortes_formatted, ordem_mortes, delta_color="inverse")

# Soma do PIB per capita
gdp = round(filtered_df['GDP per capita (current US$)'].sum(), 2)
gdp_formatted = '${:,.2f}'.format(gdp).translate(str.maketrans(',.', '.,'))
ordem_gdp = determinar_ordem_grandeza(gdp)
col5.metric("Somatória de PIB per Capita", gdp_formatted, ordem_gdp)

# Soma do investimento em saúde per capita
current_health = round(filtered_df['Current health expenditure per capita (current US$)'].sum(), 2)
current_health_formatted = '${:,.2f}'.format(current_health).translate(str.maketrans(',.', '.,'))
ordem_investimento_saude = determinar_ordem_grandeza(current_health)
col6.metric("Somatória de Investimento com Saúde per capita", current_health_formatted, ordem_investimento_saude)

# Porcentagem do investimento em saúde em relação ao PIB
porcentagem = (current_health / gdp) * 100
porcentagem_formatada = "{:.2f}%".format(porcentagem)
col7.metric("Porcentagem do investimento em saúde em relação ao PIB", porcentagem_formatada)


filtered_df = df.drop(['lat', 'lon'], axis=1)
filtered_df = filtered_df.rename(
    columns={"Current health expenditure per capita (current US$)": "Gasto em saúde per capita"})
filtered_df = filtered_df.rename(
    columns={"GDP per capita (current US$)": "GDP per capita"}
)
filtered_df = filtered_df.rename(
    columns={"Entity": "País"}
)
filtered_df = filtered_df.rename(
    columns={"Year": "Ano"}
)
filtered_df = filtered_df.rename(
    columns={"Types": "Tipos"}
)
filtered_df = filtered_df.rename(
    columns={"Deaths": "Mortes"}
)

# Mostra a tabela filtrada
st.dataframe(filtered_df, hide_index=True)

