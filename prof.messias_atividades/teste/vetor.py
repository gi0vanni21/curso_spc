import time
from random import randint

min = 0
max = 1000
QTD_ITEM = 10
vetor10 = []

# preparação do vetor 
for i in range(QTD_ITEM):
    vetor10.append(randint(min, max))

print(vetor10)

# buscar o maior valor do vetor
maior_valor = min
posicao = min

for i in range(len(vetor10)):
    print(f'iniciando o ciclo {i}')
    print(f'maior valor: {maior_valor} e vetor: {vetor10[i]}')
    if maior_valor < vetor10[i]:
        maior_valor = vetor10[i]
        posicao = i
    
    time.sleep(3)

print('0 vetor 10 completo:')
print(vetor10)
print(f'maior valor: {maior_valor}')
print(f'posição / índice: {posicao}')