vet_clubes = [
    'real madrid' .upper(),
    'barcelona'
    'Ibis'
    'Manchester united'
    'Paris Saint-German'
]

clube_buscado = input('Digite clube: ').upper()

if clube_buscado in vet_clubes:
    print('Achei')
else:
    print('Não achei')