# Ejercicio 2
vector_cadenas = []
for i in range(5):
    cadena = input(f"Ingrese la cadena {i+1}: ")
    vector_cadenas.append(cadena)
vector_inverso = vector_cadenas[::-1]
print("Vector invertido:", vector_inverso)
