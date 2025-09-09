matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Recorrido por filas:")

for i in range(len(matriz)):     
    for j in range(len(matriz[i])): 
        print(matriz[i][j], end=" ")

print()
print("Recorrido por columnas:")

for i in range(len(matriz)):     
    for j in range(len(matriz[i])): 
        print(matriz[j][i], end=" ")