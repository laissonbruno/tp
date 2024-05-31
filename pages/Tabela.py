import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_title="Tabela",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

df = pd.read_csv(r'C://Users//Laisson Bruno//Downloads//teste//dados//CancerDataBase_Final_2.csv')
st.title("Tabela")
st.write(df)