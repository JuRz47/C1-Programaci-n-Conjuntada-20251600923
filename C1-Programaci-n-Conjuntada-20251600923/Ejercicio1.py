import random

# Ejercicio 1
vector_numeros = [random.randint(1, 10) for _ in range(10)]
print("Número - Cuadrado - Cubo")
for num in vector_numeros:
    print(f"{num} - {num**2} - {num**3}")

