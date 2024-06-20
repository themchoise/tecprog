num_uno = int(input("Ingrese el valor del primer numero  \n"))
num_dos = int(input("Ingrese el valor del segundo numero  \n"))

if num_uno > num_dos:
    print(f'El numero {num_uno} es mayor que {num_dos}')
elif num_uno < num_dos:
    print(f'El numero {num_dos} es menor que {num_uno}')
else:
    print(f'El numero {num_dos} es igual que {num_uno}')