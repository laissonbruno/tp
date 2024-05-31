
# Selecionar apenas as colunas numéricas
num_cols = ['GDP per capita (current US$)', 'Current health expenditure per capita (current US$)', 'Deaths']
# correlação
corr_df = df[num_cols]

# Agrupar os dados por região
region_data = df.groupby('Region')[['GDP per capita (current US$)', 'Current health expenditure per capita (current US$)', 'Deaths']].mean().reset_index()

# Agrupar os dados por entidade
entity_data = df.groupby('Entity')[['GDP per capita (current US$)', 'Current health expenditure per capita (current US$)', 'Deaths', 'lat', 'lon']].mean().reset_index()

# Criar gráficos de dispersão com tamanho dos pontos baseado na soma de mortes e títulos
fig1 = px.scatter(region_data, x='GDP per capita (current US$)', y='Current health expenditure per capita (current US$)', color='Region', hover_name='Region', size='Deaths', title='Relação entre PIB per Capita, Investimento em Saúde per Capita e Mortes por Região')
st.plotly_chart(fig1, use_container_width=True)

fig2 = px.scatter(entity_data, x='GDP per capita (current US$)', y='Current health expenditure per capita (current US$)', color='Entity', hover_name='Entity', size='Deaths', title='Relação entre PIB per Capita, Investimento em Saúde per Capita e Mortes por Entidade')
st.plotly_chart(fig2, use_container_width=True)



