NOTA_APROBACION = 15
NOTA_RECUPERACION = 11

def leer_nota(mensaje):
    while True:
        try:
            nota = float(input(mensaje))
            if 0 <= nota <= 20:
                return nota
            else:
                print("Error: Ingrese una nota numérica válida entre 0 y 20.")
        except ValueError:
            print("Error: Ingrese un valor numérico válido.")

def determinar_estado_academico():  
    while True:
        print("\n--- Nuevo Estudiante ---")
        
        # 1. Leer el nombre del estudiante
        nombre_estudiante = input("1. Ingrese el nombre del estudiante: ").strip()
        
        # Bucle de salida
        if nombre_estudiante.upper() == "FIN":
            print("Saliendo del sistema...")
            break
        
        # 2. Leer las 3 notas parciales
        nota1 = leer_nota("2. Ingrese la Nota 1 (0-20): ")
        nota2 = leer_nota("3. Ingrese la Nota 2 (0-20): ")
        nota3 = leer_nota("4. Ingrese la Nota 3 (0-20): ")
        
        # 3. Calcular el promedio
        promedio = (nota1 + nota2 + nota3) / 3.0
        
        # 4. Determinar el estado académico
        if promedio >= NOTA_APROBACION:
            estado_academico = "APROBADO"
        elif promedio >= NOTA_RECUPERACION:
            estado_academico = "RECUPERACIÓN"
        else:
            estado_academico = "DESAPROBADO"
            
        # 5. Mostrar mensaje personalizado
        print("RESULTADO ACADÉMICO:")
        print(f"Hola {nombre_estudiante}, tu promedio final es: {promedio:.2f}")
        print(f"Hola {nombre_estudiante}, tu estado es: {estado_academico}")

if __name__ == "__main__":
    determinar_estado_academico()