
# Se requiere un algoritmo que calcule el sueldo neto de un trabajador. Para ello, el algoritmo debe admitir el
# ingreso del monto a cobrar por horas y el total de horas trabajadas. Si el empleado trabajo más de 160 horas
# mensuales se deben considerar la diferencia como horas extras y el monto por hora deberá ser el doble del
# valor ingresado en un inicio. DF – PS - PY

pago_horas = int(input("Ingrese monto a cobrar x horas \n"))
num_horas_trab = int(input("Ingrese total de horas trabajadas \n"))
horas_ref = 160
horas_extra = 0
pago_final = 0

if num_horas_trab > horas_ref:
    horas_extra = num_horas_trab - horas_ref 
    pago_final = ((num_horas_trab-horas_extra) * pago_horas) +  (( horas_extra * pago_horas ) * 2 )
else:
    pago_final = num_horas_trab * pago_horas
print(pago_final)

