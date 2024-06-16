import streamlit as st


st.set_page_config(
    page_title="Documentação & Relatório",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)



# Resumo
st.header("Resumo")
st.markdown("""
Este trabalho apresenta visualizações estatísticas sobre câncer utilizando como referência a base de estimativas atualizadas pelo Instituto Nacional do Câncer (National Cancer Institute). As visualizações revelam que a somatória do número de óbitos por câncer totalizou 157.530.737, e que a somatória do investimento em saúde per capita foi de $95.325.040,96, o que demonstra que a porcentagem do investimento em saúde em relação ao PIB foi de 7.01%. Além disso, a partir das visualizações criadas, observou-se que o câncer de pulmão foi o mais frequentemente diagnosticado no ano de 2015, responsável por aproximadamente 1,88 milhões de óbitos, seguido pelos cânceres de Cólon (10,9%), Estomago (10,4%) e Mama (7,3%).

As visualizações desenvolvidas neste trabalho analisaram a variabilidade geográfica de 189 países para os 29 principais tipos de câncer, e permitiram identificar as tendências, os padrões e as disparidades nos dados. Diante disso, concluiu-se que as visualizações criadas neste trabalho são capazes de fornecer insights valiosos para formuladores de políticas públicas, o que pode incentivar os investimentos para prevenção, podendo evitar milhões de diagnósticos futuros e salvar muitas vidas em todo o mundo, trazendo enormes benefícios econômicos e sociais para os países nas próximas décadas.
""")

# Introdução
st.header("Introdução")
st.markdown("""
Os cânceres são um conjunto de doenças caracterizadas pela rápida multiplicação de células anormais, que podem invadir tecidos próximos. Essas doenças podem surgir em diversas partes do corpo e, em alguns casos, podem se disseminar para outras regiões do organismo por meio dos sistemas circulatório e linfático. Segundo Ferlay et al. (2024), o câncer é uma das principais causas de mortalidade global, sendo responsável por quase uma em cada seis mortes em pessoas que estão na faixa etária de 30 a 69 anos, e está entre as três principais causas de morte nessa faixa etária em 177 de 183 países. O estudo desenvolvido por Guida et al. (2020) ilustra o impacto significativo da alta mortalidade por câncer entre mulheres, na qual, em 2020, estimou-se que um milhão de crianças perderam suas mães devido ao câncer. Dentre essas crianças, aproximadamente metade ficou órfã porque suas mães faleceram de câncer de mama ou câncer do colo do útero.

Diante dessa complexa realidade, surge a necessidade de desenvolver estratégias mais eficazes de prevenção, diagnóstico e tratamento. Entretanto, para isso, é preciso compreender melhor a epidemiologia do câncer, suas causas, padrões de incidência e fatores de risco. Nesse contexto, dada a complexidade dos dados relacionados ao câncer, as visualizações desempenham um papel fundamental na simplificação e comunicação dessas informações. Uma visualização eficaz pode destacar tendências, padrões e anomalias que na maioria dos casos não são detectáveis ao olhar para os dados em sua forma bruta. Neste contexto, a visualização de dados se torna uma ferramenta poderosa para gerar insights valiosos para formuladores de políticas públicas, possibilitando a realização de intervenções eficazes e a criação de políticas de saúde. Diante disso, neste trabalho foram desenvolvidas visualizações de dados sobre o câncer, e uma comparação da situação desse conjunto de doenças no Brasil em relação ao resto do mundo. Também foram utilizadas informações socioeconômicas para complementar os dados sobre câncer, para desta forma visualizar a correlação entre eles.
""")

# Os dados
st.header("Os dados")
st.markdown("""
Os dados utilizados neste trabalho para criar as visualizações sobre câncer estão disponíveis no site do Instituto Nacional do Câncer (National Cancer Institute) dos Estados Unidos, e na plataforma Kaggle. Esses dados se encontram organizados em uma tabela denominada “total-cancer-deaths-by-type.csv”, que contém uma quantidade extensa de dados que abrange diferentes aspectos relacionados aos casos de câncer no mundo, com registros que vão desde o ano de 1990 até o ano de 2019. Em resumo, são 6.840 registros (linhas) divididos em 32 categorias (colunas). Neste trabalho as visualizações se concentraram no número de mortes por tipo de câncer organizadas pelo país e o ano de registro.

Antes de utilizar os dados para gerar as visualizações, foi necessário seguir uma série de procedimentos de preparação da base de dados para retirar as inconsistências e valores nulos. Primeiramente, a base de dados foi carregada e visualizada para entender sua estrutura inicial, verificando as primeiras linhas e gerando um resumo estatístico. Em seguida, foi realizada a limpeza dos dados, tratando valores faltantes e padronizando categorias, como tipos de câncer e regiões, além de converter colunas para os tipos de dados apropriados, garantindo que os anos fossem representados como inteiros. Após a limpeza, foi conduzida uma análise exploratória para identificar padrões e tendências, observando a distribuição de mortes por diferentes tipos de câncer, variações temporais, diferenças entre gêneros e faixas etárias, e a distribuição geográfica das mortes.

Além das análises citadas anteriormente, algoritmos de aprendizado de máquina foram implementados para encontrar padrões ou informações que não haviam sido percebidos anteriormente, visando melhor visualizar os dados. Além disso, informações socioeconômicas foram cruzadas com as informações sobre câncer para relacionar os dois conjuntos de dados. Para uma análise adequada, foi necessário tratar os dados disponíveis sobre cada país. Muitos dos países presentes no dataset não continuaram existindo durante todo o período da coleta, na maioria dos casos devido a divisões territoriais. Diante disso, a estratégia utilizada foi dividir proporcionalmente a quantidade de casos de um país antes da divisão para a quantidade de países pós-divisão, mantendo as nomenclaturas mais recentes das nações, embora a estratégia para o tratamento desse caso ainda estivesse em análise.

A tabela 1 apresenta uma amostra da base de dados utilizadas para criar as visualizações:
""")

# Exibir a imagem da tabela
st.image(r"dados//tabela1.png", caption="Tabela 1")

# Ferramentas
st.header("Ferramentas")
st.markdown("""
Para a criação das visualizações deste trabalho, foram utilizados principalmente o Python e o Excel, além das bibliotecas clássicas do Python para manipulação de dados: Numpy, Pandas, entre outras, e o Plotly para gerar as visualizações estatísticas e interativas. Ferramentas como Geopandas foram empregadas para análises espaciais, permitindo a criação de mapas de calor e outras representações geográficas, facilitando a compreensão dos dados e a geração de insights significativos sobre a mortalidade por câncer. O Orange 3 foi empregado para realizar uma pequena mineração de dados. As visualizações foram inicialmente feitas no Power BI, mas acabaram não sendo incorporadas ao trabalho, pois foi possível reproduzi-las no Plotly.

Para a produção do texto e disponibilização dos gráficos online, foram usados o Datapane e o Plotly Chart Studio. Durante esse processo, tentou-se resolver o problema de ter que dar scroll em algumas visualizações. Algumas dessas visualizações foram corrigidas utilizando o Plotly Chart Studio, mas devido às limitações de tamanho dos gráficos e visualizações que podem ser armazenadas gratuitamente, optou-se por anexar as que não foram possíveis de incluir via Chart Studio através do Datapane, como originalmente planejado.
""")

# Visualizações e análises
st.header("Visualizações e análises")
st.markdown("""
Diante do objetivo do trabalho, as visualizações criadas visam segmentar os casos de óbitos oncológicos segundo dois critérios: Questões demográficas e socioeconômicos. Para isso, produziu-se visualizações que explicitassem padrões sobre mortes segundo as categorias mencionadas. As conclusões tiradas são analisadas a seguir.

## Questões demográficas
1. Qual a proporção de morte por câncer ao longo dos anos, nos diferentes continentes do mundo?
A visualização representada pela na Figura 1 apresenta um gráfico de área que ilustra a média de mortes ao longo dos anos, de 2000 a 2018, distribuídas por diferentes regiões do mundo: África, Américas, Ásia, Europa e Oceania. Essa visualização evidenciou um crescimento consistente no número de mortes na maioria das regiões ao longo do período analisado.

A África, representada pela cor azul marinho, exibiu uma base relativamente baixa e constante ao longo dos anos. As Américas, marcadas pela cor azul escuro, apresentaram um leve crescimento no número de mortes em comparação com a África. A Ásia, destacada pela cor rosa, mostrou-se como a região com o maior número de mortes durante todo o período. A linha que representa a Ásia começou em um patamar elevado e continuou a subir de forma estável, refletindo um número crescente de mortes ao longo dos anos. A Europa, indicada na cor vermelha, teve uma tendência de crescimento similar à da Ásia, embora de forma mais suave em comparação com a Ásia. Por fim, a Oceania, representada pela cor verde, mostrou o maior número de mortes em comparação com outras regiões, mas ainda assim apresentou um crescimento contínuo ao longo do período analisado.

A análise do gráfico indicou que todas as regiões experimentaram um aumento no número de mortes ao longo do tempo, com variações no ritmo de crescimento entre elas. A Oceania e a Europa lideraram em termos de número de mortes, seguidas pelas Ásia, Américas e África.
""")

st.image(r"dados//figura1.png", caption="fig 1")

st.markdown(
    """
    2. Como as diferenças regionais na mortalidade por câncer refletem as desigualdades econômicas e de saúde, e quais políticas podem ser implementadas para mitigar essas disparidades?
    A visualização representada pela na Figura 2 apresenta um gráfico que ilustra a média de mortes por câncer por região e país, utilizando uma visualização de mapa de árvore (treemap) para representar a distribuição das mortes. Cada região foi representada por um conjunto de retângulos, com tamanhos proporcionais ao número de mortes por câncer, e os países dentro de cada região foram destacados individualmente.

    Na Ásia, a China destacou-se como o país com o maior número de mortes por câncer, seguida pela Índia e Japão. Estes países mostraram áreas maiores e cores mais intensas, indicando um número elevado de mortes. Na Europa, a Rússia e a Alemanha lideraram em termos de mortes por câncer, com áreas consideráveis no gráfico. Outros países como Itália, Reino Unido e França também apresentaram números significativos, embora menores comparados aos líderes regionais. Nas Américas, os Estados Unidos foram destacados como o país com o maior número de mortes, seguidos pelo Brasil e México. O tamanho dos retângulos refletiu a gravidade da situação nos Estados Unidos, comparável à China na Ásia. A África apresentou um número menor de mortes por câncer em comparação com outras regiões. Nigéria, Egito e África do Sul foram os países mais afetados, mas com áreas menores e cores menos intensas, indicando um menor número total de mortes.

    Esta visualização ilustrou as disparidades regionais na mortalidade por câncer, destacando que países com populações maiores e economias mais robustas tendem a ter números absolutos de mortes mais altos, refletindo a necessidade de políticas de saúde pública mais eficazes e investimentos em prevenção e tratamento do câncer.
"""
)

st.image(r"dados//figura2.png", caption="fig 2")

st.markdown(
    """
    3. Como o tamanho da população e o acesso aos cuidados de saúde influenciam as médias de mortes por câncer em países menores?
    O gráfico sunburst apresentado na Figura 3 destacou os países com menor média de mortes por câncer, organizados por regiões. A Oceania e as Américas foram as regiões destacadas, com alguns dos menores números de mortes registrados.

    Na Oceania, os países com as menores médias de mortes incluíram as Ilhas Marshall, Palau, Tuvalu e Nauru. Esses países exibiram áreas menores no gráfico, refletindo o número reduzido de mortes por câncer. Nas Américas, Saint Kitts e Nevis foram destacados como o país com uma das menores médias de mortes por câncer. Assim como os países da Oceania, Saint Kitts e Nevis apresentou uma área pequena no gráfico, indicando um baixo número de mortes.

    A análise do gráfico sugere que esses países têm populações menores e, consequentemente, um número menor de casos de câncer, o que resulta em médias de mortes mais baixas. Além disso, esses países podem ter diferentes perfis de risco e acesso a cuidados de saúde que influenciam suas estatísticas de mortalidade por câncer.
    """
)

st.image(r"dados//figura3.png", caption="fig 3")

st.markdown(
    """
    4. Quais fatores específicos podem explicar as altas médias de mortes por câncer nos países destacados no gráfico radar?
    A visualização representada pela na figura 4 apresenta um gráfico que ilustra os países com a maior média de mortes por câncer, destacando especificamente a China, Estados Unidos, Índia, Japão e Rússia. Cada um desses países foi representado em um ponto no radar, com o tamanho e a forma do gráfico refletindo a magnitude das mortes por câncer em cada país.

    A China foi identificada como o país com a maior média de mortes por câncer, ocupando a maior área no gráfico radar. Este fato pode ser atribuído à sua grande população e à alta incidência de câncer, particularmente câncer de pulmão, estômago e fígado. Os Estados Unidos também apresentaram uma média elevada de mortes por câncer, com uma área significativa no gráfico. A Índia, o Japão e a Rússia seguiram com médias altas de mortes por câncer. A Índia tem grande população e enfrenta desafios significativos no tratamento e prevenção de cânceres como os de boca, pulmão e estômago.

    Essa análise destacou as diferenças regionais na mortalidade por câncer e a necessidade de abordagens específicas de saúde pública para reduzir essas taxas, especialmente em países com altos índices de mortalidade.
"""
)

st.image(r"dados//figura4.png", caption="fig 4")

# Questões Socioeconômicas
st.header("Questões Socioeconômicas")
st.markdown("""
1. Qual região apresentou o maior crescimento no PIB per capita ao longo do período analisado?
A visualização criada e apresentada na Figura 5 ilustra a média do PIB per capita ao longo dos anos, de 2000 a 2020, para diferentes regiões do mundo: África, Américas, Ásia, Europa e Oceania. A análise revelou variações significativas no PIB per capita entre as regiões ao longo do período.

A Europa, representada pela cor vermelha, destacou-se com o maior PIB per capita. Em 2000, a Europa já apresentava um PIB per capita elevado, que continuou a crescer até atingir um pico por volta de 2008. Após uma leve queda e uma fase de estabilização, o PIB per capita europeu retomou o crescimento a partir de 2015. A Ásia, indicada em rosa, apresentou um PIB per capita mais baixo em comparação com a Europa, mas mostrou um crescimento contínuo ao longo dos anos, especialmente acentuado na primeira década do século XXI. A partir de 2010, o crescimento continuou, mas em um ritmo mais moderado.

As Américas, indicadas em azul escuro, apresentaram um PIB per capita significativamente inferior ao da Europa, mas próximo ao das outras regiões. O PIB per capita nas Américas mostrou um crescimento constante ao longo dos anos, com uma leve tendência de estabilização a partir de 2010. A Oceania, representada pela cor verde, teve um comportamento similar ao das Américas, com um PIB per capita ligeiramente inferior ao das Américas durante a maior parte do período. O crescimento foi constante, com uma leve estabilização nos anos mais recentes. A África, destacada em azul marinho, teve o PIB per capita mais baixo entre todas as regiões. O crescimento do PIB per capita na África foi modesto, com uma lenta e constante elevação ao longo dos anos, refletindo desafios econômicos persistentes.

A análise do gráfico indicou que, apesar do crescimento econômico em todas as regiões, existem disparidades significativas no PIB per capita, com a Europa liderando substancialmente, seguida pelas Ásia, Américas e Oceania, enquanto a África ficou bem atrás.
""")

st.image(r"dados//figura5.png", caption="fig 5")

st.markdown("""
2. Como a correlação entre PIB per capita e investimento em saúde per capita pode influenciar as políticas de saúde pública em países com diferentes níveis de desenvolvimento econômico?
A visualização gerada é mostrada na Figura 6 e mostra a relação entre o PIB per capita, o investimento em saúde per capita e as mortes por câncer em diferentes países. No eixo horizontal, foram representados os valores do PIB per capita em dólares, enquanto no eixo vertical, foram apresentados os valores do gasto em saúde per capita também em dólares. Cada ponto no gráfico representa um país, identificado por uma cor específica conforme a legenda à direita.

A análise do gráfico revelou que países com maior PIB per capita tendiam a investir mais em saúde per capita. Por exemplo, países como a Austrália e a Noruega, que possuem um PIB per capita elevado, também mostraram altos investimentos em saúde per capita, refletindo uma correlação positiva entre a riqueza econômica de um país e seu gasto em saúde.

No entanto, havia variações significativas entre os países. Alguns países com PIB per capita relativamente alto, como os Estados Unidos, mostraram disparidades maiores no investimento em saúde per capita, indicando que o PIB elevado não se traduzia diretamente em investimentos proporcionais em todos os casos.

A análise dos dados também sugeriu que países com menor PIB per capita, como os da África Subsaariana, geralmente apresentaram menores investimentos em saúde per capita. Isso pode indicar limitações econômicas que impedem maiores investimentos na saúde pública, refletindo desafios em alcançar melhorias substanciais nos cuidados de saúde.

"""
)

st.image(r"dados//figura6.png", caption="fig 6")

st.markdown("""
3. Como o nível de investimento em saúde per capita e o PIB per capita influenciam a mortalidade por câncer em diferentes regiões do mundo?
A visualização gerada (Figura 7) ilustra a relação entre o PIB per capita, o investimento em saúde per capita e as mortes por câncer por região. No eixo horizontal, foram apresentados os valores do PIB per capita em dólares, enquanto no eixo vertical, foram exibidos os gastos em saúde per capita, também em dólares. O tamanho dos pontos no gráfico refletiu a magnitude das mortes por câncer, com diferentes cores representando as regiões: África, Américas, Ásia, Europa e Oceania.

A análise do gráfico mostrou que a Europa, representada pelo ponto vermelho maior, teve o maior gasto em saúde per capita e um PIB per capita elevado. Isso indicou que os países europeus, em média, investiram uma porção significativa de seus recursos econômicos à saúde. A América, com um ponto azul escuro de tamanho considerável, também apresentou um investimento substancial em saúde e um PIB per capita relativamente alto.

A Ásia, destacada por um ponto grande na cor rosa, indicou que, embora alguns
"""
)

st.image(r"dados//figura7.png", caption="fig 7")

st.markdown("""
4. Quais são as implicações do baixo investimento em saúde per capita nos índices de mortalidade por câncer nos países da África Subsaariana?
A visualização utilizada mostra os países com a menor média de investimentos em saúde per capita e pode ser vista na Figura 8. Os países destacados incluíram a República Democrática do Congo, Etiópia, Burundi, República Centro-Africana e Madagáscar. O eixo vertical indicou o gasto com saúde per capita em dólares americanos, enquanto o eixo horizontal listou os países.
            
A República Democrática do Congo apresentou o menor investimento em saúde per capita entre os países destacados, seguido pela Etiópia. Burundi, a República Centro-Africana e Madagáscar também mostraram investimentos baixos, mas um pouco superiores comparados aos dois primeiros países. Esses países, situados majoritariamente na África Subsaariana, enfrentaram desafios econômicos significativos que impactaram diretamente seus sistemas de saúde. O baixo investimento em saúde per capita refletiu a incapacidade desses países de fornecer cuidados médicos adequados e infraestrutura de saúde robusta, resultando em taxas elevadas de mortalidade por doenças, incluindo o câncer.
A visualização demonstra que os limitados recursos econômicos e o baixo investimento em saúde contribuíram para as dificuldades no combate ao câncer, evidenciando a necessidade de intervenções internacionais e políticas locais eficazes para melhorar os cuidados de saúde e reduzir a mortalidade.

"""
)

st.image(r"dados//figura8.png", caption="fig 8")

st.markdown("""
5. Como os altos níveis de investimento em saúde per capita nos países desenvolvidos influenciam os resultados de saúde e a mortalidade por câncer em comparação com países de menor investimento?
A visualização que utilizamos, exibida na Figura 9, mostra os países com a maior média de investimentos em saúde per capita. Os países destacados incluíram os Estados Unidos, Suíça, Noruega, Luxemburgo e Dinamarca. O eixo vertical indicou o gasto em saúde per capita em dólares americanos, enquanto o eixo horizontal listou os países.

Os Estados Unidos apresentaram o maior investimento em saúde per capita, seguido pela Suíça. A Noruega, Luxemburgo e Dinamarca também mostraram altos níveis de investimento, embora um pouco inferiores aos dos Estados Unidos e da Suíça. Esses países, situados principalmente na Europa Ocidental e América do Norte, são conhecidos por suas economias robustas e sistemas de saúde avançados. O alto investimento em saúde per capita refletiu a capacidade desses países de fornecer cuidados médicos de alta qualidade, infraestrutura de saúde sofisticada e acesso abrangente a serviços de saúde para suas populações.
A visualização demonstra que altos investimentos em saúde contribuíram para melhores resultados de saúde e potencialmente menores taxas de mortalidade por doenças, incluindo o câncer. No entanto, também levantou questões sobre a eficiência do gasto em saúde e a equidade no acesso aos serviços de saúde.

"""
)

st.image(r"dados//figura9.png", caption="fig 9")

st.markdown("""
6. Como o baixo PIB per capita nos países da África Subsaariana afeta a qualidade e a disponibilidade dos cuidados de saúde, particularmente no combate ao câncer?
A visualização mostrada na Figura 10 exibe os países com a menor média de PIB per capita nos países da África Subsaariana. Os países destacados incluíram Serra Leoa, Etiópia, República Centro-Africana, República Democrática do Congo e Burundi. O eixo horizontal indicou o PIB per capita em dólares, enquanto o eixo vertical listou os países.

Serra Leoa apresentou a maior média por PIB per capita entre os países destacados, seguido pela Etiópia. A República Centro-Africana, a República Democrática do Congo e Burundi também mostraram PIBs per capita baixos, com Burundi tendo o menor valor entre eles. 
Esses países enfrentam desafios econômicos significativos que impactaram diretamente seus sistemas de saúde e a capacidade de investir em infraestrutura médica e tratamentos adequados. O baixo PIB per capita refletiu a limitação desses países em alocar recursos suficientes para combater doenças, incluindo o câncer, resultando em altas taxas de mortalidade e uma carga significativa de doenças.
A visualização demonstra que as condições econômicas precárias e o baixo PIB per capita contribuíram para a insuficiência nos cuidados de saúde, evidenciando a necessidade de apoio internacional e políticas eficazes para melhorar a saúde pública nesses países.

"""
)

st.image(r"dados//figura10.png", caption="fig 10")

st.markdown(
    """
    7. Como a alta média de PIB per capita nos países desenvolvidos influencia a qualidade dos cuidados de saúde e os resultados de saúde, particularmente na prevenção e tratamento do câncer?
A visualização da Figura 11 mostra a maior média de PIB per capita de países situados principalmente na Europa Ocidental e Oriente Médio. Os países destacados incluíram Catar, Suíça, Noruega, Luxemburgo e Mônaco. Esses, são conhecidos por suas economias robustas e altos níveis de renda per capita 

O eixo horizontal indicou o PIB per capita em dólares americanos, enquanto o eixo vertical listou os países. Mônaco apresentou o maior PIB per capita entre os países destacados, seguido por Luxemburgo. A Noruega, Suíça e Catar também mostraram PIBs per capita elevados, mas um pouco inferiores aos de Mônaco e Luxemburgo.
A visualização demonstra que o alto PIB per capita nesses países refletiu sua capacidade de investir significativamente em várias áreas, incluindo saúde. Este investimento resultou em melhores condições de vida e maior acesso a serviços de saúde de qualidade, o que pode contribuir para melhores resultados de saúde e menores taxas de mortalidade por doenças, incluindo câncer.

"""
)

st.image(r"dados//figura11.png", caption="fig 11")

st.header("Conclusões")

st.markdown("""
A análise dos dados sobre a mortalidade por câncer, cruzada com informações socioeconômicas, revelou tendências significativas que variam de acordo com as regiões do mundo. Observou-se um aumento geral no número de mortes por câncer ao longo dos anos, com destaque para a região da Ásia, que apresentou os maiores índices de mortalidade. Este crescimento pode estar relacionado a diversos fatores, incluindo a densidade populacional, os hábitos culturais, e as condições de saúde pública. Além disso, a análise dos dados demonstrou que o investimento em saúde per capita, embora essencial, ainda está desigual entre as regiões, refletindo diretamente na eficácia dos tratamentos e na prevenção de câncer. A região europeia, com um PIB per capita significativamente mais elevado, apresentou melhores condições de saúde, o que possivelmente contribui para taxas de mortalidade menos acentuadas em comparação com outras regiões.

Com base nas visualizações gráficas geradas, fica evidente a necessidade de políticas globais mais equilibradas de saúde pública, que considerem as disparidades econômicas e invistam de forma mais equitativa em prevenção, diagnóstico precoce e tratamento do câncer. As variações no PIB per capita e no gasto em saúde são fatores críticos que afetam diretamente os índices de mortalidade. Assim, estratégias de intervenção focadas em melhorar as condições de saúde nas regiões menos favorecidas podem ajudar a reduzir as taxas de mortalidade por câncer. Este estudo reforça a importância de investimentos contínuos e direcionados, que não apenas melhorem os índices de sobrevivência, mas também promovam uma melhor qualidade de vida para os pacientes em nível global.
""")

st.header("Referências Bibliográficas")

st.markdown("""
Allemani, C., Weir, H. K., Carreira, H., Harewood, R., Spika, D., Wang, X. S., ... & Marcos-Gragera, R. (2015). Global surveillance of cancer survival 1995–2009: analysis of individual data for 25 676 887 patients from 279 population-based registries in 67 countries (CONCORD-2). *The Lancet*, 385(9972), 977-1010. [Online](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(14)62038-9/fulltext).

Bray F, Laversanne M, Weiderpass E, Soerjomataram I. (2021). The ever-increasing importance of cancer as a leading cause of premature death worldwide. *Cancer*, 127(16), 3029-3030. https://doi.org/10.1002/cncr.33587

Chen S, Cao Z, Prettner K, et al. (2023). Estimates and projections of the global economic cost of 29 cancers in 204 countries and territories from 2020 to 2050. *JAMA Oncology*, 9(4), 465-472. https://doi.org/10.1001/jamaoncol.2022.7826

Guida F, Kidman R, Ferlay J, et al. (2022). Global and regional estimates of orphans attributed to maternal cancer mortality in 2020. *Nature Medicine*, 28(12), 2563-2572. https://doi.org/10.1038/s41591-022-02109-2

Ferlay J, Ervik M, Lam F, et al. (2024). Global Cancer Observatory: Cancer Today (Version 1.0). International Agency for Research on Cancer. Acessado em 1 de fevereiro de 2024. https://gco.iarc.who.int/today

Parkin DM, Bray F, Ferlay J, Pisani P. (2005). Global cancer statistics, 2002. *CA: A Cancer Journal for Clinicians*, 55(2), 74-108. https://doi.org/10.3322/canjclin.55.2.74

Jemal A, Bray F, Center MM, Ferlay J, Ward E, Forman D. (2011). Global cancer statistics. *CA: A Cancer Journal for Clinicians*, 61(2), 69-90. https://doi.org/10.3322/caac.20107

Torre LA, Bray F, Siegel RL, Ferlay J, Lortet-Tieulent J, Jemal A. (2015). Global cancer statistics, 2012. *CA: A Cancer Journal for Clinicians*, 65(2), 87-108. https://doi.org/10.3322/caac.21262

Bray F, Ferlay J, Soerjomataram I, Siegel RL, Torre LA, Jemal A. (2018). Global cancer statistics 2018: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries. *CA: A Cancer Journal for Clinicians*, 68(6), 394-424. https://doi.org/10.3322/caac.21492
""")