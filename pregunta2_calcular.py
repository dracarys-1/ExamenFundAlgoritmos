# Constante para la tasa de IGV (18%)
IGV_TASA = 0.18

def leer_dato(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor >= 0:
                return valor
            else:
                print("Error: El valor debe ser positivo o cero.")
        except ValueError:
            print("Error: Ingrese un valor numérico válido.")

def calcular_monto_final():
    subtotal_general = 0.0
    # 1. Entrada de Datos (Número de productos)
    while True:
        try:
            n_productos = int(input("Ingrese el número de productos diferentes a comprar (N): "))
            if n_productos > 0:
                break
            else:
                print("Error: Ingrese un número entero positivo.")
        except ValueError:
            print("Error: Ingrese un número entero válido.")

    # 2. Proceso de Cálculo (Bucle para N productos)
    for i in range(1, n_productos + 1):
        print(f"\n--- Datos del Producto {i} de {n_productos} ---")

        # Leer precio y cantidad usando la función auxiliar
        precio_unitario = leer_dato("Ingrese el precio unitario del producto: ")
        cantidad = leer_dato("Ingrese la cantidad comprada: ")

        # Cálculo del subtotal por producto
        subtotal_producto = precio_unitario * cantidad
        subtotal_general += subtotal_producto

        print(f"Subtotal para Producto {i}: {subtotal_producto:.2f}")

    # Cálculos Finales
    monto_igv = subtotal_general * IGV_TASA
    total_pagar = subtotal_general + monto_igv

    # 3. Salida de Resultados
    print(f"Subtotal (Base Imponible): {subtotal_general:.2f}")
    print(f"IGV ({IGV_TASA * 100:.0f}%):             {monto_igv:.2f}")
    print(f"Total a Pagar:             {total_pagar:.2f}")

# Ejecutar la función principal
if __name__ == "__main__":
    calcular_monto_final()