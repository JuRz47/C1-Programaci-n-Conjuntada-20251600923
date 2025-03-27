inicial = 'A'
letra = input("Ingrese una letra: ")
print(f"Letra ingresada: {letra}")
simbolo = '#'
caracter = input("Ingrese un carácter: ")
if caracter.lower() in 'aeiou':
    print("Es una vocal")
else:
    print("No es una vocal")