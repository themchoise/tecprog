
rango_usuario = 25
arr_numeros = []
for x in range(rango_usuario):
    num_ingresado = int(input("Ingrese un numero del 1 al 100 \n"))
    if ( num_ingresado >= 1 and num_ingresado <= 100):
       arr_numeros.append(num_ingresado)
    print("El rango es de 1 a 100")
print(f'La suma de los numeros ingresados es {sum(arr_numeros)} , su promedio es {sum(arr_numeros)/rango_usuario}')
