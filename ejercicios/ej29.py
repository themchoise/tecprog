"""
>Confeccionar un algoritmo que resuelva el siguiente problema: Dada un código alfanumérico, diseñar un
>algoritmo que valide el código una cantidad de veces que el usuario defina. Si código es correcto en algún
>intento, mostrar por pantalla: “Logueo Exitoso!!!”. Sino “Verifique su código y vuelva a cargarlo” hasta que
>agote las veces definidas. En el último intento debe cerrarse el programa mostrando el mensaje “Ha sido
>bloqueado por superar la cantidad de intentos posibles”. DF – PS
"""

intentos = 3
codigo_alfa = "clave123"


for x in range(intentos):
    input_user = input("Ingrese la contraseña \n")
    if (input_user == codigo_alfa):
        
        print("Logueo Exitoso")
        x=intentos
    else:
        print(f'Verifique su codigo y vuelva a cargarlo, le quedan: {intentos- (x+1)} intentos \n')

print("Ha sido bloqueado por superar la cantidad de intentos posibles")