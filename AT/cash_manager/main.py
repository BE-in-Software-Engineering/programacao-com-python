"""
main.py - Arquivo principal (execução do programa)
    
"""

import os
from modules.products import (
    load_products,
    display_products,
    save_products,
)
from modules.service import start_service
from modules.utils import displays_report_cash_manager


def main():

    csv_file = os.path.join("./AT/cash_manager/data/products.csv")
    product_list = load_products(csv_file)
    print("\nCaixa aberto")

    customers = []
    customer_count = 1

    while True:
        print(f"\n[1] Iniciar atendimento do 'cliente {customer_count}'")
        print("[2] Finalizar atendimento")
        option = input("Escolha uma opção: ")

        if option == "1":
            customer = start_service(product_list, customer_count)
            if customer:
                customers.append(customer)
                customer_count += 1
        elif option == "2":
            displays_report_cash_manager(customers, product_list, csv_file)
            print("\nCaixa fechado com sucesso!")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
