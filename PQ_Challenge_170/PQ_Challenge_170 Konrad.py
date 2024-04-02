import pandas as pd  # Importa a biblioteca pandas

# Lê os dados da planilha "Sheet1" do arquivo Excel, selecionando as colunas A a C
input = pd.read_excel("PQ_Challenge_170/PQ_Challenge_170.xlsx", sheet_name="Sheet1", usecols="A:C")

# Lê os primeiros 2 registros das colunas E a H da planilha "Sheet1"
test = pd.read_excel("PQ_Challenge_170/PQ_Challenge_170.xlsx", sheet_name="Sheet1", usecols="E:H", nrows=2)

# Faz uma cópia do DataFrame "input"
result = input.copy()

# Adiciona uma nova coluna chamada "week_part", que indica se é final de semana ou dia útil
result["week_part"] = result["Date"].apply(lambda x: "Weekend" if pd.to_datetime(x).weekday() in [5, 6] else "Weekday")

# Calcula o total de vendas para cada combinação de "week_part" e "Item" e armazena na coluna "total"
result["total"] = result.groupby(["week_part", "Item"])["Sale"].transform("sum")

# Calcula o mínimo e o máximo total de vendas para cada "week_part" e armazena nas colunas "min" e "max", respectivamente
result["min"] = result.groupby(["week_part"])["total"].transform("min")
result["max"] = result.groupby(["week_part"])["total"].transform("max")

# Calcula o total de vendas para cada "week_part" e armazena na coluna "full_total"
result["full_total"] = result.groupby(["week_part"])["Sale"].transform("sum")

# Remove a coluna "Date"
result = result.drop(columns=["Date"])

# Adiciona uma nova coluna chamada "min_max" para indicar se o total de vendas é mínimo, máximo ou nenhum dos dois
result["min_max"] = result.apply(lambda row: "min" if row["total"] == row["min"] else ("max" if row["total"] == row["max"] else "none"), axis=1)

# Remove as linhas onde "min_max" é "none"
result = result[result["min_max"] != "none"].reset_index(drop=True)

# Mantém apenas as colunas relevantes, remove linhas duplicadas e redefine os índices
result = result[["Item", "week_part", "min_max",  "full_total"]].drop_duplicates().reset_index(drop=True)

# Agrupa os itens por "full_total", "min_max" e "week_part" e concatena os itens em uma string separada por vírgula
result["Item"] = result.groupby(["full_total", "min_max", "week_part"])["Item"].transform(lambda x: ", ".join(x))

# Remove linhas duplicadas após a concatenação dos itens
result = result.drop_duplicates().reset_index(drop=True)

# Converte o DataFrame de um formato longo para um formato largo usando a função pivot
result = result.pivot(index=["week_part", "full_total"], columns="min_max", values="Item").reset_index()

# Renomeia as colunas do DataFrame com os mesmos nomes das colunas de "test"
result.columns = test.columns

print(result)


