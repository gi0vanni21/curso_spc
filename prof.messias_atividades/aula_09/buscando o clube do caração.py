# encontrar um valor dentro de um vetor

vet_clubes = [
    'flamengo',
    'palmeiras',
    'real madrid',
    'barcelona',
    'inter'
]

busca = False # controle

clube_buscado = input('Digite clube: ').upper()

for i in range(len(vet_clubes)):

    if clube_buscado == vet_clubes[i].upper():
        busca = True 

if busca:
    print('achei')
else:
    print('não achei')