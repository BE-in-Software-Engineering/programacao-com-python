"""
modules/util.py - Funções utilitárias (validações e formatações)
    
"""

from datetime import datetime
from tabulate import tabulate
from modules.products import save_products


def display_customer_report(customers):
    """
    Exibe o relatório de compras de cada cliente.
    """

    total_sales = 0
    customer_report = []

    for customer in customers:
        total_purchase = sum(item[4] for item in customer)
        customer_report.append([customer[0], f"R$ {total_purchase:.2f}"])
        total_sales += total_purchase

    print(tabulate(customer_report, headers=["Cliente", "Total"], tablefmt="grid"))
    print(f"\nTotal de vendas: R$ {total_sales:.2f}")


def display_out_of_stock_products(product_list):
    """Exibe os produtos sem estoque."""

    out_of_stock_products = [product for product in product_list if product[2] == 0]
    if out_of_stock_products:
        print("\nProdutos sem estoque:")
        for product in out_of_stock_products:
            print(f"{product[1]} (ID {product[0]})")


def displays_report_cash_manager(customers, product_list, csv_file):
    """Exibe o relatório final ao atendente fechar o caixa e grava o arquivo de produtos atualizado."""

    current_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(f"\nFechamento do caixa\nData: {current_date}\n")

    display_customer_report(customers)

    display_out_of_stock_products(product_list)
    save_products(csv_file, product_list)
