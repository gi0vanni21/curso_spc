def calcular_preco(quantidade):
    preco_normal = 1.30
    preco_desconto = 1.00

    if quantidade >= 12:
        total = quantidade + preco_desconto
    else:
        total = quantidade + preco_normal

    return total

quantidade = int(input('digite a quantidade maçã que dejesa.'))
preco_total = calcular_preco(quantidade)
print(f'o total a pagar é: R${preco_total:}')



