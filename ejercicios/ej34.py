notas_alumnos = [
    7, 8, 6, 9, 5, 7, 8, 10, 6, 9,
    7, 5, 6, 8, 9, 10, 7, 8, 6, 5,
    9, 7, 8, 6, 5, 7, 8, 9, 10, 6,
    7, 5, 6, 8, 9, 7, 8, 6, 10, 5,
    9, 8, 7, 6, 5, 9, 10, 1, 6, 7 
]

for x in notas_alumnos:
    if(x < 4):
        notas_alumnos.remove(x)
print(notas_alumnos)
