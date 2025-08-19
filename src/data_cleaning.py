import pandas as pd
from datetime import datetime

def load_data(file_path):
    """
    Carrega o arquivo CSV em um DataFrame.
    """
    df = pd.read_csv(file_path)
    return df

def standardize_column_names(df):
    """
    Renomeia as colunas para um formato padronizado (snake_case).
    """
    df.rename(columns={
        'ID': 'id',
        'Area (m2)': 'area_m2',
        'Quartos': 'quartos',
        'Banheiros': 'banheiros',
        'Vagas de Garagem': 'vagas_garagem',
        'Bairro': 'bairro',
        'Andar': 'andar',
        'Preco (R$)': 'preco',
        'Tipo de Imovel': 'tipo_imovel',
        'Ano de Construcao': 'ano_construcao',
        'Observacoes': 'observacoes'
    }, inplace=True)
    return df

def handle_missing_values(df):
    """
    Trata os valores nulos nas colunas 'quartos' e 'andar'.
    """
    # Preenche o valor nulo em 'quartos' com a mediana
    mediana_quartos = df['quartos'].median()
    df['quartos'] = df['quartos'].fillna(mediana_quartos)
    
    # Preenche os valores nulos em 'andar' com 0
    df['andar'] = df['andar'].fillna(0)
    
    return df

def remove_unnecessary_columns(df):
    """
    Remove a coluna 'observacoes' que não é útil para o modelo.
    """
    df = df.drop('observacoes', axis=1)
    return df

def remove_outliers(df, column, value):
    """
    Remove as linhas com valores atípicos em uma coluna.
    """
    df = df[df[column] < value]
    return df

def cast_to_int(df, columns):
    """
    Converte o tipo de dado de colunas para inteiro.
    """
    for col in columns:
        df[col] = df[col].astype(int)
    return df

def create_feature_age(df, year_column):
    """
    Cria a coluna 'idade_imovel' a partir do ano de construcao.
    """
    ano_atual = datetime.now().year
    df['idade_imovel'] = ano_atual - df[year_column]
    return df

def clean_data(file_path):
    """
    Executa todas as etapas de limpeza e retorna o DataFrame limpo.
    """
    df = load_data(file_path)
    df = standardize_column_names(df)
    df = remove_unnecessary_columns(df)
    df = handle_missing_values(df)
    df = remove_outliers(df, 'preco', 9500000)
    df = cast_to_int(df, ['quartos', 'andar'])
    df = create_feature_age(df, 'ano_construcao')
    
    return df

if __name__ == '__main__':
    # Este bloco só será executado se o script for rodado diretamente
    # O código aqui serve para testar as funções
    
    file_path = '../data/raw/imoveis_bh.csv'
    cleaned_df = clean_data(file_path)
    
    # Exibe informações do DataFrame limpo para verificação
    print("DataFrame limpo:")
    print(cleaned_df.info())
    print(cleaned_df.describe())
    
    # Salva o arquivo limpo para a proxima etapa do projeto
    cleaned_df.to_csv('../data/processed/imoveis_bh_cleaned.csv', index=False)
    print("Arquivo limpo salvo em ../data/processed/imoveis_bh_cleaned.csv")