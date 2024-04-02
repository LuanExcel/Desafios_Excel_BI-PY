
import pandas as pd

file_path = r'C:\Users\Luan\OneDrive\Planilhas de estudos aleatorios\Desafios Excel BI\Desafios_Omid\CH-029 Identifying Customers Staple Products.xlsx'

# Carregar o arquivo Excel e selecionar as colunas C a E
df = pd.read_excel(file_path, usecols='C:E')

# Calcular a soma das quantidades agrupadas por 'Product'
grouped_df = df.groupby('Product')['Quantity'].sum().reset_index()

# Mesclar as informações agrupadas de volta ao DataFrame original
df = df.merge(grouped_df, on='Product', suffixes=('', '_total'))

print(df)

