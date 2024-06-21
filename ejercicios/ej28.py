rango_sup = int(input("Importe rango superior\n"))
rango_inf = int(input("Ingrese rango inferior \n"))


arr = None
impares = []
if (rango_sup > rango_inf ):
    arr=list(range(rango_inf,rango_sup))
    for x in arr:
     if not (x % 2 == 0 ):
        impares.append(x)
else:
     arr=list(range(rango_sup,rango_inf))
     for x in arr:
        if not (x % 2 == 0 ):
            impares.append(x)
     impares=impares[::-1]
print('Numeros impares:')
print(impares)

