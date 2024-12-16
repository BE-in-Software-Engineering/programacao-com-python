"""
modules/utils.py - Funções auxiliares para exibir relatórios de vendas, produtos sem estoque e gerar o relatório de fechamento de caixa.
    
"""

from tabulate import tabulate
from .products import save_products
from .common import format_currency, get_current_date
from .constants import (
    ITEM_TOTAL_INDEX,
    PRODUCT_ID_INDEX,
    PRODUCT_NAME_INDEX,
    PRODUCT_QUANTITY_INDEX,
)


def display_customer_report(customers):
    """
    Exibe o relatório de compras de cada cliente.

    Args:
        customers (list): Lista de clientes, onde cada cliente é representado
                          por uma lista de itens, e cada item possui os detalhes
                          da compra, como ID, nome, quantidade e preço.

    Returns:
        None
    """

    total_sales = 0
    customer_report = []
    customer_id = 1

    for customer in customers:
        total_purchase = sum(item[ITEM_TOTAL_INDEX] for item in customer)

        customer_report.append(
            [f"Cliente {customer_id}", format_currency(total_purchase)]
        )
        total_sales += total_purchase
        customer_id += 1

    print(tabulate(customer_report, headers=["Cliente", "Total"], tablefmt="grid"))
    print(f"\nTotal de vendas: {format_currency(total_sales)}")


def display_out_of_stock_products(product_list):
    """Exibe os produtos sem estoque."""

    out_of_stock_products = [
        product for product in product_list if product[PRODUCT_QUANTITY_INDEX] == 0
    ]
    if out_of_stock_products:
        print("\nProdutos sem estoque:")
        for product in out_of_stock_products:
            print(f"{product[PRODUCT_NAME_INDEX]} (ID {product[PRODUCT_ID_INDEX]})\n")


def generate_cashier_report(customers, product_list, csv_file):
    """Exibe o relatório final ao atendente fechar o caixa e grava o arquivo de produtos atualizado."""

    print(f"\nFechamento do Caixa\nData: {get_current_date()}")
    display_customer_report(customers)

    display_out_of_stock_products(product_list)
    save_products(csv_file, product_list)
