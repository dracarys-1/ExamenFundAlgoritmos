Algoritmo Estructuras_Secuenciales
	
		Definir IGV_TASA Como Real
		IGV_TASA <- 0.18
		Definir N_productos, i Como Entero
		Definir PrecioUnitario, Cantidad, SubtotalProducto Como Real
		Definir SubtotalGeneral, MontoIGV, TotalPagar Como Real
		SubtotalGeneral <- 0
		
		Escribir "Ingrese el número de productos diferentes a comprar (N):"
		Leer N_productos
		Para i <- 1 Hasta N_productos Con Paso 1 Hacer
			Escribir "--- Producto ", i, " ---"
			Escribir "Ingrese el precio unitario:"
			Leer PrecioUnitario
			Escribir "Ingrese la cantidad comprada:"
			Leer Cantidad
			SubtotalProducto <- PrecioUnitario * Cantidad
			SubtotalGeneral <- SubtotalGeneral + SubtotalProducto
		Fin Para
		MontoIGV <- SubtotalGeneral * IGV_TASA
		TotalPagar <- SubtotalGeneral + MontoIGV
		Escribir ""
		Escribir "--- RESUMEN DE COMPRA ---"
		Escribir "Subtotal (Base Imponible): ", SubtotalGeneral
		Escribir "IGV (18%): ", MontoIGV
		Escribir "Total a Pagar: ", TotalPagar
		
FinAlgoritmo
	
