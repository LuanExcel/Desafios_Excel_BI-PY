"""
Este script fornece funções para analisar e transformar dados de texto. Ele resolve
o desafio aproveitando as funções para transformar os dados de texto fornecidos.
"""

import string

import pandas as pd


def tipo_caracter(caracter: str) -> str:
    """
    Esta função recebe um único caractere como entrada e retorna
    o tipo do caractere.

    Args:
        caracter (str): Uma string de caractere única.

    Returns:
        str: O tipo do caractere. Retorna "minúsculo" se o caractere for uma
        letra minúscula, "maiúsculo" se o caractere for uma letra maiúscula, "dígito"
        se o caractere for um dígito, e "especial" para quaisquer outros caracteres.
    """
    if caracter in string.ascii_lowercase:
        grupo = "minúsculo"
    elif caracter in string.ascii_uppercase:
        grupo = "maiúsculo"
    elif caracter in string.digits:
        grupo = "dígito"
    else:
        grupo = "especial"
    return grupo


def transformar_texto(texto: str) -> str:
    """
    Esta função transforma um texto dado inserindo uma vírgula entre caracteres
    de diferentes tipos.

    Args:
        texto (str): A string de entrada que precisa ser transformada.

    Returns:
        str: A string transformada com vírgulas inseridas entre caracteres
        de diferentes tipos.
    """
    tamanho_texto = len(texto)
    letras = ""
    for idx in range(tamanho_texto):
        tipo_caracter_atual = tipo_caracter(texto[idx])
        tipo_caracter_anterior = tipo_caracter(texto[idx - 1])
        if idx > 0:
            if tipo_caracter_atual != tipo_caracter_anterior:
                letras += f", {texto[idx]}"
            else:
                letras += texto[idx]
        else:
            letras += texto[idx]
    return letras


if __name__ == "__main__":
    # Carregando os dados
    CAMINHO_DADOS = "./dados/2024/Q1/ch2024_01_04.csv"
    df = pd.read_csv(CAMINHO_DADOS)
    dados = df["Dados"]

    # Transformar os textos
    texto_transformado = [transformar_texto(texto) for texto in dados]

    # Imprimir os textos transformados
    print("\n".join(texto_transformado))
