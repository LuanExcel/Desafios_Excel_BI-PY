# Importa a biblioteca pandas e a renomeia como pd para facilitar a referência
import pandas as pd

# Define o caminho do arquivo Excel que será lido, utilizando um "raw string" (r) para evitar problemas com barras invertidas
file_path = r"Excel_Challenge_424 - Insert In Between Multiplication\Excel_Challenge_424 - Insert In Between Multiplication.xlsx"

# Lê o arquivo Excel especificado, selecionando apenas a coluna 'A' e as primeiras 9 linhas, armazenando o resultado na variável 'input'
input = pd.read_excel(file_path, usecols='A', nrows=9)

# Lê o arquivo Excel especificado novamente, desta vez selecionando apenas a coluna 'B' e as primeiras 9 linhas, armazenando o resultado na variável 'test'
test = pd.read_excel(file_path, usecols='B', nrows=9)

# Define uma função chamada 'transform_number' que recebe um número como entrada e retorna uma versão transformada desse número
def transform_number(number):
    # Converte o número em uma lista de dígitos
    digits = [int(digit) for digit in str(number)]
    # Calcula os produtos dos dígitos adjacentes e os armazena em 'transformed_digits'
    transformed_digits = [digits[i] * digits[i+1] for i in range(len(digits)-1)]
    # Adiciona uma string vazia ao final da lista 'transformed_digits' para garantir que tenha o mesmo comprimento que 'digits'
    transformed_digits.append('')
    # Combina os dígitos originais e transformados alternadamente em uma lista
    mixed_digits = [digit for pair in zip(digits, transformed_digits) for digit in pair]
    # Converte a lista resultante em uma string e a retorna
    result = ''.join(map(str, mixed_digits))
    return result

# Aplica a função 'transform_number' a cada valor na coluna 'Words' do DataFrame 'input' e armazena os resultados na nova coluna 'Answer Expected'
input["Answer Expected"] = input["Words"].apply(transform_number)

# Imprime o DataFrame 'input', que agora inclui a coluna 'Answer Expected'
print(input)
