matriz_2x2 = [[1, 2], [3, 4]]
promedio_matriz = sum(sum(fila) for fila in matriz_2x2) / 4
print(f"Promedio de los elementos de la matriz: {promedio_matriz}")
matriz_2x3 = [[1, 2, 3], [4, 5, 6]]
matriz_transpuesta = [[matriz_2x3[j][i] for j in range(2)] for i in range(3)]
print("Matriz transpuesta:")
for fila in matriz_transpuesta:
    print(fila)
