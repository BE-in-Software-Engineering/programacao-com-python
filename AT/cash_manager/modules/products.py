"""
modules/products.py - Funções relacionadas a manipulação da lista de produtos (leitura, gravação e exibição)
    
"""

import csv
from tabulate import tabulate


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
                    product = [int(row[0]), row[1], int(row[2]), float(row[3])]
                    product_list.append(product)
                else:
                    print(f"Linha inválida no arquivo: {row}")
        print(f"{len(product_list)} produtos carregados com sucesso!")
    except FileNotFoundError:
        print(f"Erro: Arquivo '{csv_file}' não encontrado. Verifique o caminho.")
    except Exception as e:
        print(f"Erro inesperado ao carregar produtos: {e}")

    return product_list


def display_products(product_list):
    """
    Exibe a lista de produtos em formato tabular.

    Args:
        product_list (list): Lista de produtos a ser exibida.
    """
    if product_list:
        table = [
            [product[0], product[1], product[2], f"R$ {product[3]:.2f}"]
            for product in product_list
        ]
        print(
            tabulate(
                table,
                headers=["Item (ID)", "Produto", "Quant.", "Preço"],
                tablefmt="grid",
            )
        )
    else:
        print("Nenhum produto em estoque.")


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
    try:
        with open(csv_file, mode="w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)

            for product in product_list:
                writer.writerow(product)
        print(f"Produtos salvos com sucesso no arquivo: '{csv_file}'.")

    except FileNotFoundError:
        print(f"Erro: Arquivo '{csv_file}' não encontrado. Verifique o caminho.")
    except PermissionError:
        print(f"Erro: Permissão negada para gravar no arquivo '{csv_file}'.")
    except Exception as e:
        print(f"Erro ao salvar os produtos: {e}")
