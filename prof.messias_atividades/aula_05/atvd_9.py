#entrada de dados
nota_1 = float(input('digete a nota 1:'))
nota_2 = float(input('digete a nota 2:'))

#processamemnto
media = (nota_1 + nota_2) / 2

#sida de dados
if media >= 6:
    print(f'aprovado , com média {media}.')

else:
    print(f'recuperação, commédia {media}.')
