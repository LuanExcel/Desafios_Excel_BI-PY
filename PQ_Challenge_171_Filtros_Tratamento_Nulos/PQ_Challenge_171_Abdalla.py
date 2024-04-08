import pandas as pd

# Ler o arquivo Excel
file_path = 'PQ_Challenge_171.xlsx'
# Lê apenas as primeiras 6 linhas e as colunas de A a F
df = pd.read_excel(file_path, nrows=6, usecols='A:F')

# Calcular o número de colunas dividido por 2
columns = df.shape[1] // 2

# Inicializar um dicionário para armazenar os valores das colunas separadamente
values = {'Col1': [], 'Col2': []}

# Iterar sobre cada linha do DataFrame
for row in df.iterrows():
    # Estender a lista de valores da 'Col1' com as primeiras 'columns' colunas
    values['Col1'].extend(row[1].values[:columns])
    # Estender a lista de valores da 'Col2' com as colunas restantes
    values['Col2'].extend(row[1].values[columns:])

# Criar um novo DataFrame a partir do dicionário de valores
df = pd.DataFrame(values)

# Remover linhas onde todas as células são vazias (NaN)
df.dropna(how='all', inplace=True)

# Resetar o índice do DataFrame após a remoção das linhas vazias
df.reset_index(drop=True, inplace=True)

# Substituir os valores NaN por uma string vazia
df.replace(float('nan'), '', inplace=True)

# # Imprimir o DataFrame resultante
print(df)
