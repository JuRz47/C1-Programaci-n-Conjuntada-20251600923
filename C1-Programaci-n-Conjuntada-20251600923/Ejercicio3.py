# Ejercicio 3
matriz = []
for i in range(5):
    fila = [random.randint(1, 10) for _ in range(5)]
    matriz.append(fila)

print("Matriz:")
for fila in matriz:
    print(fila)

total_filas = [sum(fila) for fila in matriz]
total_columnas = [sum(matriz[i][j] for i in range(5)) for j in range(5)]

print("Suma de cada fila:", total_filas)
print("Suma de cada columna:", total_columnas)
