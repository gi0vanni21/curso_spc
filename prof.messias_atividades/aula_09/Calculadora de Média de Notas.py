controle = True
notas = []

while controle:
    print('->100 para sair')
    print('ou digite a noto desejada!')

    nota = int(input('digite a nota: '))

    if 0 <= nota <=10:
        notas.append(nota)

    elif nota == 100:
        controle = False 
    else:
        print('valor inválido!')

print('as notas são:')