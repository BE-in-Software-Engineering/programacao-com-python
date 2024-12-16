"""
modules/service.py - Funções relacionadas ao atendimento ao cliente
    
"""

from tabulate import tabulate
from .common import display_error_message, get_current_date, format_currency
from .constants import (
    PRODUCT_ID_INDEX,
    PRODUCT_NAME_INDEX,
    PRODUCT_QUANTITY_INDEX,
    PRODUCT_PRICE_INDEX,
    ITEM_QUANTITY_INDEX,
    ITEM_TOTAL_INDEX,
)


def start_service(product_list, customer_id):
    """
    Inicia o atendimento de um cliente, permitindo adicionar itens ao carrinho
    e finaliza com a emissão de uma nota fiscal.

    Args:
        product_list (list): Lista de produtos disponíveis.
        customer_id (int): ID único do cliente.

    Returns:
        list: Uma lista contendo os itens comprados pelo cliente.
              Cada item é uma lista com os seguintes elementos:
              - ID do produto (int)
              - Nome do produto (str)
              - Quantidade comprada (int)
              - Preço unitário (float)
              - Preço total do item (float)
    """

    print(f"\nIniciado atendimento do 'cliente {customer_id}'")
    customer_items = []

    while True:
        print("\n[1] Adicionar item")
        print("[2] Finalizar atendimento")
        option = input("Escolha uma opção: ")

        if option == "1":
            add_item(product_list, customer_items)
        elif option == "2":
            ends_service(customer_id, customer_items)
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
        product = find_product_by_id(product_list, product_id)
        if not product:
            display_error_message("Produto não cadastrado.")
            return

        quantity = int(input("Informe a quantidade: "))
        if quantity <= 0:
            display_error_message("Quantidade deve ser maior que zero.")
            return

        if product[PRODUCT_QUANTITY_INDEX] < quantity:
            display_error_message(
                f"Estoque insuficiente. Estoque atual do {product[PRODUCT_NAME_INDEX]}: {product[PRODUCT_QUANTITY_INDEX]}"
            )
            return

        add_or_update_cart_item(customer_items, product, quantity)

    except ValueError:
        display_error_message("Entrada inválida. Tente novamente.")


def find_product_by_id(product_list, product_id):
    """
    Busca um produto pelo ID na lista de produtos.

    Args:
        product_list (list): Lista de produtos.
        product_id (int): ID do produto.

    Returns:
        list: Produto correspondente ou None se não encontrado.
    """
    return next(
        (
            product
            for product in product_list
            if product[PRODUCT_ID_INDEX] == product_id
        ),
        None,
    )


def add_or_update_cart_item(customer_items, product, quantity_to_add):
    """
    Atualiza a quantidade de um item no carrinho ou adiciona um novo item.

    Args:
        customer_items (list): Lista de itens do cliente.
        product (list): Produto a ser adicionado.
        quantity_to_add (int): Quantidade do produto.

    Returns:
        None.
    """

    total_item_price = quantity_to_add * product[PRODUCT_PRICE_INDEX]
    existing_item = next(
        (
            item
            for item in customer_items
            if item[PRODUCT_ID_INDEX] == product[PRODUCT_ID_INDEX]
        ),
        None,
    )

    if existing_item:
        existing_item[ITEM_QUANTITY_INDEX] += quantity_to_add
        existing_item[ITEM_TOTAL_INDEX] += total_item_price
        print(
            f"Quantidade atualizada: {existing_item[PRODUCT_NAME_INDEX]} agora tem {existing_item[PRODUCT_QUANTITY_INDEX]} unidades no carrinho."
        )
    else:
        customer_items.append(
            [
                product[PRODUCT_ID_INDEX],
                product[PRODUCT_NAME_INDEX],
                quantity_to_add,
                product[PRODUCT_PRICE_INDEX],
                total_item_price,
            ]
        )
        print(
            f"Item '{product[PRODUCT_NAME_INDEX]}' adicionado ao carrinho. Subtotal: {format_currency(total_item_price)}"
        )

    product[PRODUCT_QUANTITY_INDEX] -= quantity_to_add


def ends_service(customer_id, customer_items):
    """
    Finaliza o atendimento do cliente e exibe a nota fiscal.

    Args:
        customer_id (int): ID único do cliente.
        customer_items (list): Lista de itens comprados pelo cliente.

    Returns:
        None.
    """

    if not customer_items:
        print("Nenhum item foi adicionado ao carrinho. Atendimento encerrado.")
        return

    total_purchase = calculate_total_purchase(customer_items)
    total_quantity = calculate_total_quantity(customer_items)

    display_invoice(customer_id, customer_items, total_quantity, total_purchase)


def calculate_total_purchase(customer_items):
    """
    Calcula o valor total da compra a partir dos itens no carrinho.

    Args:
        customer_items (list): Lista de itens comprados pelo cliente.

    Returns:
        float: Valor total da compra.
    """
    return sum(item[ITEM_TOTAL_INDEX] for item in customer_items)


def calculate_total_quantity(customer_items):
    """
    Calcula o total de unidades dos itens no carrinho.

    Args:
        customer_items (list): Lista de itens comprados pelo cliente.

    Returns:
        int: Total de unidades dos itens no carrinho.
    """
    return sum(item[PRODUCT_QUANTITY_INDEX] for item in customer_items)


def display_invoice(customer_id, customer_items, total_quantity, total_purchase):
    """
    Exibe a nota fiscal da compra do cliente.

    Args:
        customer_id (int): Número identificador do cliente.
        customer_items (list): Lista de itens comprados.
        total_quantity (int): Total de unidades compradas.
        total_purchase (float): Valor total da compra.

    Returns:
        None.
    """
    print(f"\nNota Fiscal\nCliente {customer_id}\nData: {get_current_date()}")
    print(
        tabulate(
            customer_items,
            headers=["Item(ID)", "Produto", "Quant.", "Preço", "Total"],
            tablefmt="grid",
        )
    )
    print(
        f"Itens: {total_quantity}\nTotal: {format_currency(total_purchase)}\nAtendimento do 'cliente {customer_id}' finalizado.\n"
    )
