import pandas as pd
import numpy as np

# Função para encontrar colunas que correspondem a um valor específico em uma linha
def matching_columns(df, row, match_col):
    # Lista compreensiva para encontrar colunas que correspondem ao valor de 'match_col' na linha 'row'
    matches = [col for col in df.columns if row[col] == row[match_col] and col != match_col]
    # Junta os nomes das colunas correspondentes em uma string separada por vírgula
    return ', '.join(matches)

# Caminho do arquivo Excel
file_path = 'PQ_Challenge_170/PQ_Challenge_170.xlsx'

# Leitura dos dados do arquivo Excel para os DataFrames df1 e df2
df1 = pd.read_excel(file_path, usecols='E:H', nrows=2) # DataFrame original
df2 = pd.read_excel(file_path, usecols='A:C') # DataFrame para cálculos

# Adiciona uma coluna 'Weekday' ao df2 que representa o dia da semana (0 = segunda-feira, ..., 6 = domingo)
df2['Weekday'] = df2['Date'].dt.weekday

# Adiciona uma coluna 'Day Type' ao df2, indicando se é dia útil ou final de semana
df2['Day Type'] = np.where(df2['Weekday'] < 5, 'Weekday', 'Weekend')

#df2['Day Type'] = df2['Weekday'].apply(lambda x: 'Weekday' if x in [5,6] else 'weekend')

# Cria uma tabela pivô no df2 com as vendas de cada item agrupadas por tipo de dia
df2 = df2.pivot_table(values='Sale', index='Day Type', columns='Item', aggfunc='sum').fillna(0).reset_index()

# Calcula o total de vendas para cada tipo de dia
df2['Total Sales'] = df2.loc[:, 'Item 1': 'Item 5'].sum(axis=1)

# Calcula o valor máximo de vendas para cada tipo de dia
df2['Maximum Value'] = df2.loc[:, 'Item 1': 'Item 5'].max(axis=1)

# Calcula o valor mínimo de vendas para cada tipo de dia
df2['Minimum Value'] = df2.loc[:, 'Item 1': 'Item 5'].min(axis=1)

# Encontra o item mais vendido para cada tipo de dia
df2['Highest Selling Item'] = df2.apply(lambda x: matching_columns(df2, x, 'Maximum Value'), axis=1)

# Encontra o item menos vendido para cada tipo de dia
df2['Lowest Selling Item'] = df2.apply(lambda x: matching_columns(df2, x, 'Minimum Value'), axis=1)

# Renomeia os rótulos das colunas para não ter um rótulo de linha
df2 = df2.rename_axis(None, axis=1)

# Seleciona apenas as colunas desejadas
df2 = df2.loc[:, ['Day Type', 'Total Sales', 'Highest Selling Item', 'Lowest Selling Item']]

# Exibe os DataFrames df1 e df2
print(f'\nExpected Answer:\n{df1} \n\nMy Answer: \n{df2}')




