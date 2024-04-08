import pandas as pd
import numpy as np

# Importa as bibliotecas necessárias

file_path = 'PQ_Challenge_171.xlsx'

# Define o caminho do arquivo Excel a ser lido

df = pd.read_excel(file_path, usecols='A:F')

# Lê o arquivo Excel, selecionando apenas as colunas A a F

df.replace('NaN', np.nan, inplace=True)

# Substitui todas as ocorrências de string 'NaN' por NaN (valores nulos)

filtro0 = df.iloc[0:len(df.columns)]

# Filtra o DataFrame para obter as primeiras linhas (correspondentes ao número de colunas)

lista_dicionarios = filtro0.to_dict(orient='records').copy()

# Converte as primeiras linhas do DataFrame em uma lista de dicionários onde cada dicionário representa uma coluna

dfs_concatenados = []

# Inicializa uma lista para armazenar os DataFrames concatenados posteriormente

for i in range(len(df.columns)):
    # Itera sobre as colunas do DataFrame
    a = list(lista_dicionarios[i].values())
    # Obtém os valores da coluna atual
    lista = ['0' if pd.isna(x) else x for x in a]
    # Substitui os valores NaN por '0' e cria uma lista dividida em sublistas com comprimento 3
    split = 3
    lista = [a[i:i + split] for i in range(0, len(a), split)]
    # Divide a lista em sublistas de tamanho 'split'
    df1 = pd.DataFrame(lista).T.reset_index()
    # Cria um DataFrame com as sublistas, transpõe e reseta os índices
    df1 = df1.rename(columns={0: 'coluna1', 1: 'coluna2'})
    # Renomeia as colunas do DataFrame resultante
    df1['concatenado'] = df1['coluna1'].fillna('0') + df1['coluna2'].fillna('0')
    # Concatena as colunas 'coluna1' e 'coluna2' e preenche valores nulos com '0'
    filtro = df1.loc[df1['concatenado'] != '00']
    # Filtra as linhas onde 'concatenado' é diferente de '00'
    res = filtro[['coluna1', 'coluna2']]
    # Seleciona apenas as colunas 'coluna1' e 'coluna2' do resultado
    dfs_concatenados.append(res)
    # Adiciona o resultado à lista de DataFrames concatenados

df_concatenado = pd.concat(dfs_concatenados, ignore_index=True)
# Concatena todos os DataFrames na lista 'dfs_concatenados' e ignora os índices originais
df_concatenado['coluna1'] = df_concatenado['coluna1'].str.split(',').str[0]
# Divide os valores na coluna 'coluna1' pelo delimitador ',' e seleciona apenas o primeiro valor
print(df_concatenado)

# Imprime o DataFrame resultante após todas as operações

