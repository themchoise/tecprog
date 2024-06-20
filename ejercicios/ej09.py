qnt_minutos = int(input("Ingrese los minutos  \n"))
horas = int(qnt_minutos/60)
minutos_restantes = int(qnt_minutos-(horas*60))

print(f'Tiempo: Horas:{horas} , minutos:{minutos_restantes}')