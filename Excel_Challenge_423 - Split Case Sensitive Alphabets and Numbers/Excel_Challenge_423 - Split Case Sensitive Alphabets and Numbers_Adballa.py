import pandas as pd
import re

# Ler o arquivo Excel
file_path = r'Excel_Challenge_423 - Split Case Sensitive Alphabets and Numbers\Excel_Challenge_423 - Split Case Sensitive Alphabets and Numbers.xlsx'

# Usar o pandas para ler o arquivo Excel, selecionando apenas a coluna 'Data'
df = pd.read_excel(file_path, usecols=['Data'])

# Função para gerar a saída desejada
def split_case(text):
    # Usar expressão regular para encontrar letras minúsculas, letras maiúsculas e números na string 'text'
    chars = re.findall('[a-z]+|[A-Z]+|[0-9]+', text)
    # Juntar os caracteres encontrados em uma string separada por vírgula e espaço
    return ', '.join(chars)

# Aplicar a função 'split_case' a cada valor na coluna 'Data' e criar uma nova coluna 'My Answer' com os resultados
df['My Answer'] = df['Data'].apply(split_case)

# Imprimir as colunas 'Data' e 'My Answer'
print(f'Expected Results:\n{df[["Data", "My Answer"]]}')
