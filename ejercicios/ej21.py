

num_uno = int(input("Ingrese el valor del primer numero  \n"))
num_dos = int(input("Ingrese el valor del segundo numero  \n"))
num_tres = int(input("Ingrese el valor del tercer numero  \n"))

if num_uno > num_dos and num_uno > num_tres:
        mayor = num_uno
elif num_dos > num_uno and num_dos > num_tres:
        mayor = num_dos
else:
        mayor = num_tres
print(f'El numero {mayor} es el mayor')