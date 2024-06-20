num = int(input("Ingrese monto de la compra \n"))
monto_pagar = 0
estarjeta = True
dto_15 = 0.85
dto_10 = 0.90

if num > 2000 and num <= 5000:
   monto_pagar = num * dto_10
elif num > 5000 and not estarjeta:
    monto_pagar = num * dto_15
elif num > 5000 and estarjeta:
    monto_pagar = num * dto_10
print(monto_pagar)




