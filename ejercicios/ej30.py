"""
>Se requiere de un algoritmo que almacene en un arreglo 10 números ingresados por un usuario y luego los
>muestre en el mismo orden en que los ingreso. . DF – PS
"""

arr=[]
rango=10
for x in range(rango):
    arr.append(int(input(f'[{x+1}|{rango}]Ingrese un numero:')))
print(arr)