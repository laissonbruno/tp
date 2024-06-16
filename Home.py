import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_title="Home",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

df = pd.read_csv(r'dados//CancerDataBase_Final_2.csv')


st.sidebar.success("Selecione uma pagina acima")


st.markdown(
    """
    # Projeto de Análise e visualização de Dados

    ## Objetivo

    O objetivo deste projeto é analisar a relação entre o PIB per capita, a despesa de saúde per capita e a taxa de mortalidade por câncer em diferentes países.

    ## Dados utilizados:

    1. [ISO-3166-Countries-with-Regional-Codes:](https://github.com/lukes/ISO-3166-Countries-with-Regional-Codes/blob/master/all/all.csv) Este conjunto de dados fornece códigos de países ISO.
    2. [Cancer Dataset - Total cancer deaths by type:](https://www.kaggle.com/datasets/programmerrdai/cancer) Este conjunto de dados fornece informações sobre o total de mortes por câncer por tipo.
    3. [World Development Indicators:](https://datacatalog.worldbank.org/search/dataset/0037712/World-Development-Indicators) Este conjunto de dados fornece indicadores de desenvolvimento mundial, incluindo o PIB per capita (em dólares americanos) e a despesa de saúde atual per capita (em dólares americanos).


    ## Participantes

    Laisson Bruno - [Linkedin](https://www.linkedin.com/in/laissonbruno/)  
    Cleiton Neves - [Linkedin](https://www.linkedin.com/in/sncleiton/)  
    Daniel Henriques - [Lattes](http://lattes.cnpq.br/3182580850135052)  
    Estanislau de Sena Filho - [Linkedin](https://www.linkedin.com/in/estanislau-sena-filho/)  

    
    ## Professora

    Raquel Cardoso de Melo Minardi - [Lattes](http://lattes.cnpq.br/9274887847308980)

    ## Disciplina

    Visualização de dados - DCC831
"""
)

st.markdown("# Descrição dos dados")

# Criar colunas para organizar a página
col1, col2, col3 = st.columns(3)  # Primeira linha com três colunas
col4, col5, col6 = st.columns(3)  # segunda linha com três colunas


col4.write("Mortes")
col4.write(df['Deaths'].describe())

col5.write("Pib Per Capita:")
col5.write(df['GDP per capita (current US$)'].describe())

col6.write("Investimento em saúde per Capita:")
col6.write(df['Current health expenditure per capita (current US$)'].describe())

