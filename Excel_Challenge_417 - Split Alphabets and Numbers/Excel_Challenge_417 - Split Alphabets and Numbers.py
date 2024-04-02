#Esta linha importa a biblioteca pandas, que é frequentemente usada para manipulação e análise de dados em Python.
import pandas as pd
import re

#Nesta linha, é definido o caminho para o arquivo Excel a ser lido. O r antes das 
# aspas indica uma "string bruta" em Python, o que significa que os 
# caracteres de escape dentro da string não serão interpretados
file_path = r'Excel_Challenge_417 - Split Alphabets and Numbers\Excel_Challenge_417 - Split Alphabets and Numbers.xlsx'

#Esta linha lê o arquivo Excel especificado (file_path) e 
# carrega-o em um DataFrame do pandas.
df = pd.read_excel(file_path)

# Define a função para dividir caracteres
def split_case(text):
    chars = re.findall('[A-z]+|[0-9]+',text)
    return ', '.join(chars)

#chars = re.findall('[a-z]+|[A-Z]+|[0-9]+', text)

df['Resposta'] = df['Data'].apply(split_case)

print(df[["Data", "Resposta"]])  
    
    


 