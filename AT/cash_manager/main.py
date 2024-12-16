"""
main.py - Arquivo principal (execução do programa)
    
"""

import os
from modules.products import load_products
from modules.service import start_service
from modules.utils import generate_cashier_report


def main():

    csv_file = os.path.join("./AT/cash_manager/data/products.csv")
    product_list = load_products(csv_file)
    print("\nCaixa aberto")

    customers = []
    customer_id = 1

    while True:
        print(f"\n[1] Iniciar atendimento do 'cliente {customer_id}'")
        print("[2] Finalizar atendimento")
        option = input("Escolha uma opção: ")

        if option == "1":
            customer = start_service(product_list, customer_id)
            if customer:
                customers.append(customer)
                customer_id += 1
        elif option == "2":
            generate_cashier_report(customers, product_list, csv_file)
            print("\nCaixa fechado com sucesso!")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
