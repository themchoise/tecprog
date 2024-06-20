import datetime as dt

anio_actual = dt.date.today().year
num_uno = int(input("Ingrese su año de nacimiento \n"))
print(f' Su edad es {anio_actual-num_uno}')