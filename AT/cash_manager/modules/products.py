"""
modules/products.py - Funções relacionadas a manipulação da lista de produtos (leitura e gravação )
    
"""

import csv
from .common import display_error_message
from .constants import (
    PRODUCT_ID_INDEX,
    PRODUCT_NAME_INDEX,
    PRODUCT_QUANTITY_INDEX,
    PRODUCT_PRICE_INDEX,
)


def load_products(csv_file):
    """
    Carrega os produtos de um arquivo CSV e retorna uma lista de produtos.

    Cada produto é representado como uma lista com os campos:
    [ID (int), Nome (str), Quantidade (int), Preço (float)].

    Args:
        csv_file (str): Caminho para o arquivo CSV contendo os produtos.

    Returns:
        list: Lista de produtos carregados.

    Exceptions:
        - FileNotFoundError: Se o arquivo não for encontrado.
        - Exception: Para outros erros ao processar o arquivo.
    """
    product_list = []
    try:
        with open(csv_file, "r", encoding="utf-8") as file:
            reader = csv.reader(file)

            for row in reader:
                if len(row) == 4:
                    try:
                        product = [
                            int(row[PRODUCT_ID_INDEX]),
                            row[PRODUCT_NAME_INDEX],
                            int(row[PRODUCT_QUANTITY_INDEX]),
                            float(row[PRODUCT_PRICE_INDEX]),
                        ]

                        if product[PRODUCT_PRICE_INDEX] < 0:
                            print(
                                f"Preço inválido para o produto '{product[PRODUCT_NAME_INDEX]}' (ID {product[PRODUCT_ID_INDEX]}). Preço deve ser maior ou igual a zero."
                            )
                            continue

                        product_list.append(product)
                    except ValueError:
                        display_error_message(
                            f"Dados inválidos para o produto '{row[PRODUCT_NAME_INDEX]}' (ID {row[PRODUCT_ID_INDEX]}). Verifique os valores."
                        )
                else:
                    display_error_message(f"Linha inválida no arquivo: {row}")
        print(f"{len(product_list)} produtos carregados com sucesso!")
    except FileNotFoundError:
        display_error_message(
            f"Arquivo '{csv_file}' não encontrado. Verifique o caminho."
        )
    except Exception as e:
        display_error_message(f"Erro inesperado ao carregar produtos: {e}")

    return product_list


def save_products(csv_file, product_list):
    """
    Salva a lista de produtos em um arquivo CSV.

    Args:
        csv_file (str): Caminho para o arquivo CSV onde os produtos serão salvos.
        product_list (list): Lista de produtos a ser salva.

    Returns:
        None

    Exceptions:
        - FileNotFoundError: Se o arquivo não puder ser encontrado.
        - PermissionError: Se não houver permissão para gravar no arquivo.
        - Exception: Para outros erros ao salvar o arquivo.
    """

    if not product_list:
        print("Nenhum produto para salvar.")
        return

    try:
        with open(csv_file, mode="w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)

            for product in product_list:
                writer.writerow(product)
        print(f"Produtos salvos com sucesso no arquivo: '{csv_file}'.")

    except FileNotFoundError:
        display_error_message(
            f"Arquivo '{csv_file}' não encontrado. Verifique o caminho."
        )
    except PermissionError:
        display_error_message(f"Permissão negada para gravar no arquivo '{csv_file}'.")
    except Exception as e:
        display_error_message(f"Não foi possível salvar os produtos: {e}.")
