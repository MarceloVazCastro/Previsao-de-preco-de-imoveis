# Projeto de Previsão de Preços de Imóveis

Este projeto é uma demonstração do processo de Ciência de Dados, focado na previsão de preços de imóveis em Belo Horizonte. A primeira etapa, detalhada neste repositório, concentra-se na **Análise Exploratória e Limpeza de Dados (EDA)**, um passo crucial para garantir a qualidade do conjunto de dados antes da modelagem.

## 1. Estrutura do Repositório

O projeto está organizado para seguir as melhores práticas de Ciência de Dados, separando os dados brutos, o código-fonte e os notebooks de análise.

/
├── data/
│   ├── raw/
│   │   └── imoveis_bh.csv         # Dados brutos e originais
│   └── processed/
│       └── imoveis_bh_cleaned.csv # Dados limpos após a primeira etapa
├── notebooks/
│   └── 01_data_exploration_and_cleaning.ipynb # Notebook com o processo de EDA e limpeza
├── .gitignore
├── README.md
├── requirements.txt

## 2. Descrição do Projeto (Fase 1)

O objetivo desta fase foi preparar o conjunto de dados para a modelagem futura. Foram executadas as seguintes tarefas:

* **Análise Exploratória de Dados (EDA):** Verificação da estrutura, tipos de dados e estatísticas descritivas para identificar problemas.
* **Tratamento de Dados Nulos:** Identificação e preenchimento de valores ausentes de forma estratégica para evitar a perda de informações.
* **Tratamento de Outliers:** Análise e remoção de valores atípicos que poderiam distorcer o modelo preditivo.
* **Padronização:** Renomeação de colunas e ajuste de tipos de dados para otimizar o processamento.

## 3. Principais Descobertas e Resultados da Análise

A análise exploratória revelou a necessidade de uma limpeza cuidadosa. Os principais desafios encontrados e as soluções aplicadas foram:

* **Dados Nulos:** As colunas `quartos` e `andar` continham valores nulos. O valor ausente em `quartos` foi preenchido com a mediana, enquanto os nulos em `andar` (que correspondiam a casas) foram preenchidos com `0`.
* **Outliers de Preço:** Foi identificado um imóvel com um preço significativamente alto (`R$ 9.500.000`), que foi removido do conjunto de dados para não enviesar o modelo de regressão.
* **Dados Inconsistentes:** A coluna `observacoes`, com a maioria dos valores nulos, foi removida, e os tipos de dados de `quartos` e `andar` foram convertidos para inteiros.

## 4. Próximos Passos

O conjunto de dados limpo, agora salvo como `imoveis_bh_cleaned.csv`, está pronto para as próximas etapas do projeto, que incluirão:

* **Engenharia de Features:** Criação de novas variáveis relevantes para a previsão.
* **Modelagem:** Construção e treinamento de um modelo de Regressão Linear.
* **Avaliação do Modelo:** Análise das métricas de desempenho e interpretação dos resultados.

## 5. Tecnologias Utilizadas

* **Python**
* **Pandas:** Para manipulação e análise de dados.
* **Matplotlib e Seaborn:** Para a visualização de dados.