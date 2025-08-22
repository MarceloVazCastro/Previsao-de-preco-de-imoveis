import pandas as pd
import numpy as np
import statsmodels.formula.api as sm
import scipy.stats as stats

def preprocess_for_model(df):
    """
    Realiza a engenharia de features e o pré-processamento final para o modelo.

    Args:
        df (pd.DataFrame): DataFrame com os dados limpos.

    Returns:
        pd.DataFrame: DataFrame com as colunas prontas para o modelo.
    """
    ano_atual = pd.Timestamp.now().year
    df['idade_imovel'] = ano_atual - df['ano_construcao']

    df_encoded = pd.get_dummies(df, columns=['bairro'], drop_first=True)
    
    df_encoded['log_preco'] = np.log(df_encoded['preco'])
    
    return df_encoded

def train_model(df_encoded):
    """
    Treina um modelo de Regressão Linear usando statsmodels.

    Args:
        df_encoded (pd.DataFrame): DataFrame com as features prontas.

    Returns:
        statsmodels.regression.linear_model.RegressionResultsWrapper: Modelo treinado.
    """
    formula = 'log_preco ~ area_m2 + quartos + banheiros + vagas_garagem + andar + idade_imovel + tipo_imovel_Casa + bairro_Buritis + bairro_Centro + bairro_Floresta + bairro_Lourdes + bairro_Mangabeiras + bairro_Pampulha + bairro_Santo_Agostinho + bairro_Savassi'
    
    modelo = sm.ols(formula=formula, data=df_encoded).fit()
    return modelo

def evaluate_model(model, df_encoded):
    """
    Avalia o modelo treinado e imprime métricas importantes.

    Args:
        model (statsmodels.regression.linear_model.RegressionResultsWrapper): Modelo treinado.
        df_encoded (pd.DataFrame): DataFrame usado para o treinamento.
    """
    print("--- Resumo do Modelo de Regressão ---")
    print(model.summary())
    
    residuos = model.resid
    stat, pval = stats.shapiro(residuos)
    
    print("\n--- Análise de Normalidade dos Resíduos (Shapiro-Wilk) ---")
    print(f'Estatística de Shapiro-Wilk: {stat:.3f}, p-value: {pval:.3f}')
    
    if pval > 0.05:
        print("Os resíduos parecem ser normalmente distribuídos (não podemos rejeitar a hipótese nula).")
    else:
        print("A hipótese de normalidade dos resíduos é rejeitada.")

if __name__ == '__main__':
    
    from data_cleaning import clean_data

    raw_file_path = '../data/raw/imoveis_bh.csv'
    cleaned_df = clean_data(raw_file_path)
    
    df_for_model = preprocess_for_model(cleaned_df)
    
    final_model = train_model(df_for_model)
    evaluate_model(final_model, df_for_model)