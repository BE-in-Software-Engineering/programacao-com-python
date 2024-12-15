"""
modules/service.py - Funções relacionadas ao atendimento ao cliente
    
"""

from tabulate import tabulate
from datetime import datetime


def start_service(product_list, customer_count):
    """
    Inicia o atendimento de um cliente, permitindo adicionar itens ao carrinho
    e finaliza com a emissão de uma nota fiscal.

    Args:
        product_list (list): Lista de produtos disponíveis.
        customer_count (int): Número identificador do cliente.

    Returns:
        list: Lista de itens comprados pelo cliente.
    """

    print(f"\nIniciado atendimento do 'cliente {customer_count}'")
    customer_items = []

    while True:
        print("\n[1] Adicionar item")
        print("[2] Finalizar atendimento")
        option = input("Escolha uma opção: ")

        if option == "1":
            add_item(product_list, customer_items)
        elif option == "2":
            ends_service(customer_count, customer_items)
            break
        else:
            print("Opção inválida, tente novamente.")

    return customer_items


def add_item(product_list, customer_items):
    """
    Adiciona itens ao carrinho do cliente.

    Args:
        product_list (list): Lista de produtos disponíveis.
        customer_items (list): Lista de itens do cliente.

    Returns:
        None.
    """

    try:
        product_id = int(input("Informe o ID do produto: "))
        quantity = int(input("Informe a quantidade: "))

        product = next(
            (product for product in product_list if product[0] == product_id), None
        )
        if not product:
            print("Erro: Produto não cadastrado.")
            return
        if quantity <= 0:
            print("Erro: Quantidade deve ser maior que zero.")
            return
        if product[2] < quantity:
            print(
                f"Erro: Estoque insuficiente. Estoque atual do {product[1]}: {product[2]}"
            )
            return

        total_items = quantity * product[3]
        customer_items.append(
            [product[0], product[1], quantity, product[3], total_items]
        )
        product[2] -= quantity
        print(f"Item '{product[1]}' adicionado. Subtotal: R$ {total_items:.2f}")

    except ValueError:
        print("Erro: Entrada inválida.")


def ends_service(customer_count, customer_items):
    """
    Finaliza o atendimento do cliente e exibe a nota fiscal.

    Args:
        customer_count (int): Número identificador do cliente.
        customer_items (list): Lista de itens comprados pelo cliente.

    Returns:
        None.
    """

    if not customer_items:
        print("Nenhum item foi adicionado. Atendimento encerrado.")
        return

    total_purchase = sum(item[4] for item in customer_items)
    total_quantity = sum(item[2] for item in customer_items)

    current_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    print(f"\nNota Fiscal\nCliente {customer_count}\nData: {current_date}")
    print(
        tabulate(
            customer_items,
            headers=["Item(ID)", "Produto", "Quant.", "Preço", "Total"],
            tablefmt="grid",
        )
    )
    print(
        f"Itens: {total_quantity}\nTotal: R$ {total_purchase:.2f}\nAtendimento do 'cliente {customer_count}' finalizado.\n"
    )
