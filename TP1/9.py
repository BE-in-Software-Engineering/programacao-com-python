def calculate_discount():
    purchase_value = float(input("Digite o valor da compra:"))

    if purchase_value > 500:
        discount = 0.25
    elif purchase_value > 200:
        discount = 0.15
    elif purchase_value > 100:
        discount = 0.10
    else:
        discount = 0.00

    discount_value = purchase_value * discount
    final_price = purchase_value - discount_value

    print(
        f"Valor da compra: R${purchase_value:.2f}\n"
        f"Desconto aplicado: R${discount_value:.2f}\n"
        f"Valor final: R${final_price:.2f}"
    )


calculate_discount()
