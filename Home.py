import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_title="Home",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

df = pd.read_csv(r'C://Users//Laisson Bruno//Downloads//teste//dados//CancerDataBase_Final_2.csv')

st.write("# Welcome to Streamlit!")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.
    **👈 Select a demo from the sidebar** to see some examples
    of what Streamlit can do!
    ### Want to learn more?
    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community
        forums](https://discuss.streamlit.io)
    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)

st.markdown("# Analises Descritivas dos dados")

# Criar colunas para organizar a página
col1, col2, col3 = st.columns(3)  # Primeira linha com três colunas
col4, col5, col6 = st.columns(3)  # segunda linha com três colunas



col4.write("Mortes")
col4.write(df['Deaths'].describe())

col5.write("Pib Per Capita:")
col5.write(df['GDP per capita (current US$)'].describe())

col6.write("Investimento em saúde per Capita:")
col6.write(df['Current health expenditure per capita (current US$)'].describe())