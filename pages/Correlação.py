import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# Configuração da página
st.set_page_config(
    page_title="Correlação",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Título da página
st.write('Correlação')

# Carrega o arquivo CSV
df = pd.read_csv(r'dados//CancerDataBase_Final_2.csv')

# Container para seleção de regiões
with st.sidebar:
    # Container para regiões
    container1 = st.container(height=100)
    all1 = st.checkbox("Selecione todas regiões", value=True)

    if all1:
        selected_options1 = container1.multiselect(
            "Selecione uma ou mais regiões:", 
            sorted(df["Region"].unique()), 
            sorted(df["Region"].unique())
        )
    else:
        selected_options1 = container1.multiselect(
            "Selecione uma ou mais regiões:", 
            sorted(df["Region"].unique())
        )

    # Container para anos
    container2 = st.container(height=100)
    all2 = st.checkbox("Selecione todos anos", value=True)

    if all2:
        selected_options2 = container2.multiselect(
            "Selecione um ou varios anos:", 
            sorted(df["Year"].unique()), 
            sorted(df["Year"].unique())
        )
    else:
        selected_options2 = container2.multiselect(
            "Selecione um ou varios anos:", 
            sorted(df["Year"].unique())
        )

    # Container para tipos de cancer
    container3 = st.container(height=100)
    all3 = st.checkbox("Selecione todos os tipos", value=True)

    if all3:
        selected_options3 = container3.multiselect(
            "Selecione um ou mais tipos de cancer:", 
            sorted(df["Types"].unique()), 
            sorted(df["Types"].unique())
        )
    else:
        selected_options3 = container3.multiselect(
            "Selecione um ou mais tipos de cancer:", 
            sorted(df["Types"].unique())
        )


# Filtro dos dados
filtered_df = df[
    (df["Region"].isin(selected_options1)) &
    (df["Year"].isin(selected_options2)) &
    (df["Types"].isin(selected_options3))
]

# Seleção de colunas para análise de correlação
num_cols = ['GDP per capita (current US$)', 'Current health expenditure per capita (current US$)', 'Deaths']
corr_df = filtered_df[num_cols]

# Gráfico de dispersão para regiões
region_data = filtered_df.groupby('Region')[['GDP per capita (current US$)', 'Current health expenditure per capita (current US$)', 'Deaths']].mean().reset_index()
fig1 = px.scatter(region_data, x='GDP per capita (current US$)', y='Current health expenditure per capita (current US$)', color='Region', hover_name='Region', size='Deaths', title='Relação entre PIB per Capita, Investimento em Saúde per Capita e Mortes por Região')
st.plotly_chart(fig1, use_container_width=True)

# Explicação do gráfico
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

# Gráfico de dispersão para países
entity_data = filtered_df.groupby('Entity')[['GDP per capita (current US$)', 'Current health expenditure per capita (current US$)', 'Deaths', 'lat', 'lon']].mean().reset_index()
fig2 = px.scatter(entity_data, x='GDP per capita (current US$)', y='Current health expenditure per capita (current US$)', color='Entity', hover_name='Entity', size='Deaths', title='Relação entre PIB per Capita, Investimento em Saúde per Capita e Mortes por País')
st.plotly_chart(fig2, use_container_width=True)

# Gráfico de dispersão para países (segunda forma)
fig3 = px.scatter(filtered_df.groupby("Entity").agg({"GDP per capita (current US$)": "mean", "Current health expenditure per capita (current US$)": "mean"}).reset_index(), x="GDP per capita (current US$)", y="Current health expenditure per capita (current US$)", color="Entity", title='Relação entre PIB per Capita, Investimento em Saúde per Capita e Mortes por País - (Segunda forma para melhor visualização dos países)')
st.plotly_chart(fig3)

# Explicação do gráfico
with st.expander("Explicação"):
    st.write(
        """
        ## Análise da Correlação entre PIB per Capita, Investimento em Saúde per Capita e Mortes por País

        ### Correlação entre PIB per Capita e Investimento em Saúde per Capita
        **Existe uma correlação positiva entre PIB per capita e investimento em saúde per capita**. Países com maior PIB per capita tendem a investir mais em saúde per capita. Por exemplo, Noruega, Suíça e Luxemburgo estão entre os países com maior PIB per capita e também com maior investimento em saúde per capita.

        ### Correlação entre PIB per Capita e Mortes
        **Países com maior PIB per capita e investimento em saúde per capita tendem a ter menor número de mortes**. Países como Islândia, Japão e Suíça têm alto PIB per capita, alto investimento em saúde per capita e baixo número de mortes.

        ### Exceções
        **Alguns países fogem a essa tendência geral**. Por exemplo, Estados Unidos tem alto PIB per capita e investimento em saúde per capita, mas número de mortes relativamente alto em comparação a outros países desenvolvidos.

        ### Conclusão
        Em resumo, **embora não haja uma correlação perfeita**, os dados sugerem que **países com maior riqueza e investimento em saúde tendem a ter melhores indicadores de saúde, com menor número de mortes**. No entanto, fatores como distribuição de renda, eficiência dos gastos em saúde e densidade habitacional também desempenham um papel importante.
        """
    )


# corr_matrix é a sua matriz de correlação
corr_matrix = corr_df.corr()

# Cria uma máscara para o triângulo superior
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))

# Converte a máscara em um array de valores booleanos
mask = mask.tolist()

# Inverte os valores da máscara
mask = [[not cell for cell in row] for row in mask]

# Cria um texto de exibição ao passar o mouse sobre o heatmap
hovertext = [[f'x: {x}<br>y: {y}<br>z: {z}' for x, y, z in zip(corr_matrix.columns, corr_matrix.index, row)] for row in corr_matrix.values]

# Cria o heatmap
fig = go.Figure(data=go.Heatmap(
    z=corr_matrix,
    x=corr_matrix.columns,
    y=corr_matrix.columns,
    xgap=1, ygap=1,
    colorscale='Reds',
    zmin=0, zmax=1,
    hovertext=hovertext,
    hoverinfo='text',
    showscale=True,
    visible=True
))

# Aplica a máscara ao heatmap e remove as células onde a correlação é 1
for i in range(len(mask)):
    for j in range(len(mask[i])):
        if mask[i][j] or corr_matrix.iloc[i, j] == 1:
            fig.data[0]['z'][i][j] = None

# Adiciona anotações de texto
for i in range(len(corr_matrix.columns)):
    for j in range(len(corr_matrix.columns)):
        if not mask[i][j] and corr_matrix.iloc[i, j] != 1:
            fig.add_annotation(
                x=corr_matrix.columns[j],
                y=corr_matrix.columns[i],
                text=str(round(corr_matrix.iloc[i, j], 2)),
                showarrow=False,
                font=dict(
                    color="black",
                    size=12
                )
            )

# Configura o layout do gráfico
fig.update_layout(
    title_text='Matriz de Correlação',
    title_x=0.5,
    autosize=False,
    margin=dict(t=60, b=60, l=60, r=60),
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis_showgrid=False,
    yaxis_showgrid=False,
    xaxis_zeroline=False,
    yaxis_zeroline=False,
)

# Exibe o gráfico
st.plotly_chart(fig)