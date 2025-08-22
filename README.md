# Projeto de Previsão de Preços de Imóveis

Este projeto é uma demonstração do processo de Ciência de Dados, focado na previsão de preços de imóveis em Belo Horizonte. A primeira etapa, detalhada neste repositório, concentra-se na **Análise Exploratória e Limpeza de Dados (EDA)**, um passo crucial para garantir a qualidade do conjunto de dados antes da modelagem.

## 1. Estrutura do Repositório

O projeto está organizado para seguir as melhores práticas de Ciência de Dados, separando os dados brutos, o código-fonte e os notebooks de análise.

* `data/`
    * `raw/`
        * `imoveis_bh.csv`         # Dados brutos e originais
    * `processed/`
        * `imoveis_bh_cleaned.csv` # Dados limpos após a primeira etapa
* `notebooks/`
    * `01_data_exploration_and_cleaning.ipynb` # Notebook com o processo de EDA e limpeza
    * `02_feature_engineering_and_modeling.ipynb` # Notebook de modelagem e avaliação
    * `03_model_evaluation_and_insights.ipynb` # Relatório final de resultados
* `.gitignore`
* `README.md`
* `requirements.txt`
* `LICENSE`

## 2. Descrição do Projeto (Fase 1: Análise e Limpeza de Dados)

O objetivo desta fase foi preparar o conjunto de dados para a modelagem futura. Foram executadas as seguintes tarefas:

* **Análise Exploratória de Dados (EDA):** Verificação da estrutura, tipos de dados e estatísticas descritivas para identificar problemas.
* **Tratamento de Dados Nulos:** Identificação e preenchimento de valores ausentes de forma estratégica para evitar a perda de informações.
* **Tratamento de Outliers:** Análise e remoção de valores atípicos que poderiam distorcer o modelo preditivo.
* **Padronização:** Renomeação de colunas e ajuste de tipos de dados para otimizar o processamento.

A análise exploratória revelou a necessidade de uma limpeza cuidadosa. Os principais desafios encontrados e as soluções aplicadas foram:

* **Dados Nulos:** As colunas `quartos` e `andar` continham valores nulos. O valor ausente em `quartos` foi preenchido com a mediana, enquanto os nulos em `andar` (que correspondiam a casas) foram preenchidos com `0`.
* **Outliers de Preço:** Foi identificado um imóvel com um preço significativamente alto (`R$ 9.500.000`), que foi removido do conjunto de dados para não enviesar o modelo de regressão.
* **Dados Inconsistentes:** A coluna `observacoes`, com a maioria dos valores nulos, foi removida, e os tipos de dados de `quartos` e `andar` foram convertidos para inteiros.

## 3. Descrição do Projeto (Fase 2: Modelagem e Avaliação)

Nesta fase, o conjunto de dados limpo foi utilizado para construir um modelo de Machine Learning capaz de prever o preço de um imóvel.

* **Engenharia de Features:** Uma nova variável, `idade_imovel`, foi criada a partir do ano de construção. A coluna `bairro`, que é categórica, foi convertida em variáveis numéricas usando a técnica de **One-Hot Encoding** para que o modelo pudesse processá-la.
* **Construção do Modelo:** Foi utilizado um modelo de **Regressão Linear Múltipla** para estabelecer a relação entre as características do imóvel (área, quartos, bairro, etc.) e o preço.
* **Avaliação do Modelo:** A performance do modelo foi avaliada utilizando o **R-squared**, que atingiu um valor de `0.956`. Isso indica que o modelo consegue explicar 95,6% da variabilidade dos preços, o que demonstra uma alta capacidade de previsão. Além disso, a análise dos resíduos (com histogramas e Q-Q plots) confirmou que o modelo atende aos pressupostos estatísticos, tornando-o confiável.

## 4. Principais Insights e Conclusões

A análise dos coeficientes do modelo de regressão revelou `insights` importantes sobre quais características mais influenciam o preço dos imóveis no dataset:

* **Área:** Para cada metro quadrado adicional, o preço do imóvel aumenta **0,56%** em média.
* **Localização:** O modelo, utilizando o bairro Anchieta como referência, mostrou que:
    * Um imóvel no **Centro** é, em média, **21,9%** mais barato que um imóvel com características semelhantes no Anchieta.
    * Um imóvel no **Buritis** é, em média, **12,7%** mais barato.
    * Um imóvel no bairro **Floresta** é, em média, **29,7%** mais barato.

## 5. Tecnologias Utilizadas

* **Python**
* **Pandas:** Para manipulação e análise de dados.
* **Matplotlib e Seaborn:** Para a visualização de dados.
* **Statsmodels:** Para a construção e análise do modelo de regressão linear.