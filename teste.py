#Esta linha importa a biblioteca pandas, que é frequentemente usada para manipulação e análise de dados em Python.
import pandas as pd

#Nesta linha, é definido o caminho para o arquivo Excel a ser lido. O r antes das 
# aspas indica uma "string bruta" em Python, o que significa que os 
# caracteres de escape dentro da string não serão interpretados
file_path = r'C:\Users\Luan\PY\Alura\arquivo\Excel_Challenge_421 - Stack Diagonals.xlsx'

#Esta linha lê o arquivo Excel especificado (file_path) e 
# carrega-o em um DataFrame do pandas.
df = pd.read_excel(file_path)
print(df)