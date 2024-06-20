numero = int(input("Por favor, ingrese un número: "))

if numero % 2 != 0:
    resultado = numero * 2
    print(f"El número es impar. El resultado de {numero} multiplicado por 2 es {resultado}.")
else:
    print(f"El número {numero} es par.")
