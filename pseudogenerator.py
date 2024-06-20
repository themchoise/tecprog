def main(ruta, ruta_salida):

    def leer_archivo_python(ruta):
        with open(ruta, 'r') as archivo:
            return archivo.readlines()

    def convertir_a_pseudocodigo(lineas_codigo):
        pseudocodigo = []
        
        for linea in lineas_codigo:
            linea = linea.strip()
            
            # Detectar definiciones de funciones
            if linea.startswith('def '):
                nombre_funcion = linea.split('(')[0][4:]
                pseudocodigo.append(f"FUNCION {nombre_funcion}")
            
            # Detectar retornos
            elif linea.startswith('return '):
                retorno = linea.split('return ')[1]
                pseudocodigo.append(f"RETORNAR {retorno}")
            
            # Detectar condicionales
            elif linea.startswith('if '):
                condicion = linea.split('if ')[1].rstrip(':')
                pseudocodigo.append(f"SI {condicion} ENTONCES")
            
            # Detectar else
            elif linea.startswith('else'):
                pseudocodigo.append("SINO")
            
            # Detectar bucles while
            elif linea.startswith('while '):
                condicion = linea.split('while ')[1].rstrip(':')
                pseudocodigo.append(f"MIENTRAS {condicion} HACER")
            
            # Detectar bucles for
            elif linea.startswith('for '):
                bucle = linea.split('for ')[1].rstrip(':')
                pseudocodigo.append(f"PARA {bucle} HACER")
            
            # Detectar impresiones
            elif linea.startswith('print('):
                imprimir = linea.split('print(')[1].rstrip(')')
                pseudocodigo.append(f"IMPRIMIR {imprimir}")
            
            # Otros casos (asignaciones, etc.)
            else:
                if linea:
                    pseudocodigo.append(linea)
        
        pseudocodigo.append("FIN")
        return pseudocodigo

    def guardar_pseudocodigo(pseudocodigo, ruta_salida):
        with open(ruta_salida, 'w') as archivo:
            for linea in pseudocodigo:
                archivo.write(linea + '\n')



    lineas_codigo = leer_archivo_python(ruta)
    pseudocodigo = convertir_a_pseudocodigo(lineas_codigo)
    guardar_pseudocodigo(pseudocodigo, ruta_salida)        

