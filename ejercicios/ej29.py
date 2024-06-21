
intentos = 3
codigo_alfa = "clave123"
acceso_exitoso = False

for x in range(intentos):
    input_user = input("Ingrese la contraseña \n")
    if (input_user == codigo_alfa):
        
        print("Logueo Exitoso")
        acceso_exitoso=True
        break
    else:
        print(f'Verifique su codigo y vuelva a cargarlo, le quedan: {intentos- (x+1)} intentos \n')
 
if not (acceso_exitoso):
    print("Ha sido bloqueado por superar la cantidad de intentos posibles")

