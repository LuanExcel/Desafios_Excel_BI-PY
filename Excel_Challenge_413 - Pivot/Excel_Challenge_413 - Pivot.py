##Aqui, estamos importando a biblioteca pandas e a estamos utilizando com o alias pd. Isso nos permite acessar todas as funcionalidades do pandas usando pd.
import pandas as pd

## Carregue os dados do arquivo Excel
## Estamos definindo o caminho do arquivo Excel como uma string e, em seguida, usando 
## a função pd.read_excel() para ler os dados do arquivo Excel e armazená-los no DataFrame Fonte.

file_path = r"Excel_Challenge_413 - Pivot\Excel_Challenge_413 - Pivot.xlsx"
Fonte = pd.read_excel(file_path)

## Agrupe os dados por 'ID' e aplique uma transformação para criar uma nova tabela
## Aqui, estamos agrupando os dados do DataFrame Fonte por valores únicos na coluna 'ID' usando o método .groupby(). Para cada grupo, estamos aplicando uma função que cria um novo DataFrame onde:

## A coluna 'ID' é repetida para cada linha do grupo, garantindo que tenhamos uma coluna 'ID' consistente para cada linha no novo DataFrame.
## Estamos criando colunas 'Num 0', 'Num 1', etc., onde cada valor da coluna 'Num' no grupo original é atribuído a uma coluna separada no novo DataFrame. Isso é feito usando uma compreensão de dicionário para criar as colunas.
## Finalmente, estamos redefinindo os índices do novo DataFrame para garantir que eles sejam sequenciais e não contenham referências aos índices antigos dos grupos.*/

gp = Fonte.groupby("ID").apply(lambda x: pd.DataFrame({
    "ID": [x["ID"].iloc[0]] * len(x),  # Repetir o ID para cada linha do grupo
    **{f"Num {i}": x["Num"].iloc[i] for i in range(len(x))}  # Criar colunas Num 0, Num 1, etc.
})).reset_index(drop=True)

#Ordenar o resultado por 'ID' e 'Num 0'
#Estamos usando o método .sort_values() para ordenar o DataFrame gp pelas colunas 'ID' e 'Num 0'. 
#Isso garante que as linhas sejam ordenadas primeiro por 'ID' e, em seguida, dentro de cada grupo 'ID', elas são ordenadas por 'Num 0'.
res = gp.sort_values(by=["ID", "Num 0"])

#Estamos usando o método .drop_duplicates() para remover linhas duplicadas do 
#DataFrame res. Isso retorna um novo DataFrame res_sem_duplicatas que contém apenas as linhas únicas de res.
res_sem_duplicatas = res.drop_duplicates()

print(res_sem_duplicatas)

