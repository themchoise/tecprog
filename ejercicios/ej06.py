import requests
pesos = int(input("Ingrese la cantidad en pesos Argentinos \n"))
dolar_blue = 1000
try:
    dolar_blue = requests.get("https://dolarapi.com/v1/dolares/blue").json()["venta"]
except:
    None

print(f'El equivalente en dolares es {pesos/dolar_blue}')


