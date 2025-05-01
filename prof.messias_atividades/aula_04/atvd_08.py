def calcular_desconto(valor_compra):
    if valor_compra > 100:
        desconto = valor_compra * 0.10
    elif 50 <= valor_compra <= 100:
        desconto = valor_compra * 0.05
    else:
        desconto = 0
    
    total_a_pagar = valor_compra - desconto
    return desconto, total_a_pagar

# Entrada do usuário
valor_compra = float(input("Digite o valor da compra: R$ "))

desconto, total = calcular_desconto(valor_compra)

# Exibição dos resultados
print(f"Desconto: R$ {desconto:.2f}")
print(f"Total a pagar: R$ {total:.2f}")
