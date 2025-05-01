def conta_vogais(texto):
    vogais = 'aeiouAEIOU'
    contador = 0
    for letra in texto:
        if letra in vogais:
            contador += 1
    return contador

# Exemplo de uso
frase = "Programação é incrível!"
print(conta_vogais(frase))  # Saída: 9
