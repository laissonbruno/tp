# with st.sidebar:

#     container1 = st.container(height=100)
#     all1 = st.checkbox("Selecione todas regiões", value=True)

#     if all1:
#         selected_options1 = container1.multiselect("Selecione uma ou mais regiões:", df["Region"].unique(), df["Region"].unique())
#     else:
#         selected_options1 = container1.multiselect("Selecione uma ou mais regiões:", df["Region"].unique())
    
#     container2 = st.container(height=100)
#     all2 = st.checkbox("Selecione todos anos", value=True)

#     if all2:
#         selected_options2 = container2.multiselect("Selecione um ou varios anos:", df["Year"].unique(), df["Year"].unique())
#     else:
#         selected_options2 = container2.multiselect("Selecione um ou varios anos:", df["Year"].unique())

#     container3 = st.container(
#         height=100
#     )
#     all3 = st.checkbox("selecione todos os tipos", value=True)

#     if all3:
#         selected_options3 = container3.multiselect("Selecione um ou mais tipos de cancer:", df["Types"].unique(), df["Types"].unique())
#     else:
#         selected_options3 = container3.multiselect("Selecione um ou mais tipos de cancer:", df["Types"].unique())

# filtered_df = df[
#     (df["Region"].isin(selected_options1)) &
#     (df["Year"].isin(selected_options2)) &
#     (df["Types"].isin(selected_options3))
# ]


# metrics = {
#     'Deaths': 'Mortes',
#     'GDP per capita (current US$)': 'PIB',
#     'Current health expenditure per capita (current US$)': 'Gasto com Saúde'
# }

# for metric_col, metric_name in metrics.items():
#     mean_value = filtered_df[metric_col].mean()
#     median_value = filtered_df[metric_col].median()
#     desvio_padrao = filtered_df[metric_col].std()

#     # Display the metrics
#     col1, col2, col3 = st.columns(3)
#     col1.metric(f"{metric_name} || Média", round(mean_value))
#     col2.metric(f"{metric_name} || Mediana", round(median_value))
#     col3.metric(f"{metric_name} || Desvio Padrão", round(desvio_padrao))
