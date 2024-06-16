import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import plotly.graph_objects as go


# Configuração da página
st.set_page_config(
    page_title="Análise Exploratória",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Carrega o arquivo CSV
df = pd.read_csv(r'dados//CancerDataBase_Final_2.csv')

# Divide a página em colunas
col1, col2, col3 = st.columns(3)
col4, col5 = st.columns(2)  
col6, col7 = st.columns(2)  
col8, col9 = st.columns(2)  
col10, col11 = st.columns(2)  


col2.write("# Análise exploratória")

# Variaveis para utilização nos gráficos
most_deaths = df.groupby('Entity')['Deaths'].mean().sort_values(ascending=False).head(5)
least_deaths = df.groupby('Entity')['Deaths'].mean().sort_values(ascending=True).head(5)
max_gdp_countries = df.groupby('Entity')['GDP per capita (current US$)'].mean().sort_values(ascending=False).head(5)
min_gdp_countries = df.groupby('Entity')['GDP per capita (current US$)'].mean().sort_values(ascending=True).head(5)
most_health_exp = df.groupby('Entity')['Current health expenditure per capita (current US$)'].mean().sort_values(ascending=False).head(5)
least_health_exp = df.groupby('Entity')['Current health expenditure per capita (current US$)'].mean().sort_values(ascending=True).head(5)

# Dados do DataFrame most_deaths
categorias = most_deaths.index
valores = most_deaths.values

# Criar o gráfico de radar
fig = go.Figure(data=go.Scatterpolar(
    r=valores,
    theta=categorias,
    fill='toself',
    name='Países com maior média de mortes',
    line=dict(color='red'),  # Define a cor da linha para vermelho
))

fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, max(valores)]
        )),
    showlegend=False,
    title="Países com maior média de mortes - Gráfico de Radar",
)

col4.plotly_chart(fig)

# Criando o gráfico Sunburst
fig2 = px.sunburst(df[df['Entity'].isin(least_deaths.index)], path=['Region', 'Entity'], values='Deaths',
                   color='Deaths',
                   hover_data='GDP per capita (current US$)',
                   color_continuous_scale='oryel',
                   color_continuous_midpoint=np.average(df['Deaths'], weights=df['GDP per capita (current US$)']))
fig2.update_layout(title='Países com menor média de mortes - Gráfico Sunburst')
col5.plotly_chart(fig2)

# Gráfico de Barras com os países com maior média por PIB
fig3 = px.bar(max_gdp_countries, x='GDP per capita (current US$)', y=max_gdp_countries.index, title="Países com maior média por PIB", orientation='h', color_discrete_sequence=px.colors.sequential.Agsunset)
fig3.update_layout(
    xaxis_title='PIB per capita',
    yaxis_title='Países'
)
fig3.update_xaxes(categoryorder='total descending')
col6.plotly_chart(fig3)

# Gráfico de Barras Horizontais com os países com menor média por PIB
fig4 = px.bar(min_gdp_countries, x='GDP per capita (current US$)', y=min_gdp_countries.index, title="Países com menor média por PIB", orientation='h', color_discrete_sequence=px.colors.sequential.Agsunset)
fig4.update_layout(
    xaxis_title='PIB per capita',
    yaxis_title='Países'
)
col7.plotly_chart(fig4)

# Gráfico de Barras Horizontais com os países com maior média de investimentos em saúde
fig5 = px.bar(most_health_exp, x=most_health_exp.index, y='Current health expenditure per capita (current US$)', title="Países com maior média de investimentos em saúde", color_discrete_sequence=px.colors.sequential.Agsunset)
fig5.update_layout(
    xaxis_title='Países',
    yaxis_title='Gasto com saúde per capita'
)
col8.plotly_chart(fig5)

# Gráfico de Barras com os países com menor média de investimentos em saúde
fig6 = px.bar(least_health_exp, 
              x=least_health_exp.index, 
              y='Current health expenditure per capita (current US$)', 
              title="Países com menor média de investimentos em saúde", 
              color_discrete_sequence=px.colors.sequential.Agsunset)
fig6.update_layout(
    xaxis_title='Países',
    yaxis_title='Gasto com saúde per capita'
)
col9.plotly_chart(fig6)

# Gráfico de Treemap com o número de mortes por região/país
treemap = df.groupby(['Region', 'Entity']).agg({'Deaths': 'mean'}).reset_index()
fig7 = px.treemap(treemap, 
                  path=['Region', 'Entity'], 
                  values='Deaths', 
                  color='Deaths', 
                  title="Média de mortes por Região/País", 
                  color_continuous_scale='Reds')
fig7.update_layout(margin=dict(t=50, l=25, r=25, b=25))
st.plotly_chart(fig7)

# Texto de análise
st.write(
    """
## Análise da Mortalidade por Câncer e Investimento em Saúde Global

Com base nos dados apresentados, observa-se que a mortalidade por câncer varia significativamente entre os países, com a China liderando em número de mortes, enquanto países menores como Nauru e Tuvalu registram as menores taxas. No entanto, é importante ressaltar que a quantidade de mortes por câncer pode não estar diretamente ligada ao PIB per capita e aos gastos em saúde per capita. Mesmo países com alto investimento e PIB alto, como os Estados Unidos e Suíça, podem ter um grande número de mortes por câncer. Isso se deve ao fato de que, quanto mais habitantes um país tem, consequentemente mais mortes ele terá, como é o caso da Índia e da China.

O **PIB per capita** reflete a disparidade econômica, com nações como Mônaco e Luxemburgo apresentando os maiores valores, indicando maior capacidade de investimento em saúde. Os **gastos em saúde per capita** seguem essa tendência, com países como os Estados Unidos e Suíça investindo mais, em contraste com nações como a República Democrática do Congo e Etiópia, que têm recursos limitados para a saúde.

Esses insights destacam a interconexão entre saúde, economia e investimento em cuidados médicos em escala global, mas também ressaltam que o número de mortes por câncer não depende apenas desses fatores. Outros elementos, como o tamanho da população e a incidência da doença, também desempenham um papel importante.
"""
)