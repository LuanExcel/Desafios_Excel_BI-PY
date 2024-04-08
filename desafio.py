#Esta linha importa a biblioteca pandas, que é frequentemente usada para manipulação e análise de dados em Python.
import pandas as pd
import numpy as np

file_path = 'PQ_Challenge_171.xlsx'

df = pd.read_excel(file_path,usecols='A:F')

lista_dicionarios = df.to_dict(orient='records').copy()


a = list(lista_dicionarios[0].values())
lista = ['0' if isinstance(x, float) and pd.isna(x) else x for x in a]

split = 3
lista = [a[i:i + split] for i in range(0, len(a), split)]
df1 = pd.DataFrame(lista).T

df1.replace('NaN', np.nan, inplace=True)

filtro = df1.loc[df1.iloc[:, 0].notna()]

print(filtro)