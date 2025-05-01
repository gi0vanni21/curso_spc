matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]

#imprimir a matriz 
print(matriz)

#imprimir a segunda linha da matriz
print(matriz[1])

#imprimir o número 6 apenas
print(matriz[1][2])

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(f'i={i} e j={j} - {matriz[i][j]}')