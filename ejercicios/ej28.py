""" 28. Confeccionar un algoritmo que resuelva el siguiente problema: Dado 2 números (rango inferior y rango
superior) diseñar un algoritmo que devuelva la cantidad de números impares que hay en el rango definido.
Solo DF. Ej: 10 - 50 (incrementando), O de 1350 a 1000 (decrementando). DF – PS
"""
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
     impares[::-1]
print(impares)

