ventas_refacciones = int(input("Ingrese Importe de ventas de refacciones \n"))
ventas_servicio = int(input("Importe de ventas de servicio\n"))
ventas_autos_camiones = int(input("Importe de ventas de autos y camiones \n"))

imp_total = ventas_refacciones+ ventas_servicio + ventas_autos_camiones
promedio = imp_total / 3

x = lambda a : 'Se alcanzo el objetivo' if a > 50000 else 'Buscar nuevas estrategias de ventas'

print(x(promedio))



