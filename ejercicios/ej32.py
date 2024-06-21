
arr = []
rango = 6
new_arr = []
for x in range(rango):
    input_usuario=input("Ingrese una palabra \n")
    arr.append(input_usuario)
new_arr = arr.copy()[::-1]
print(new_arr)