op = 0
x = b = h = r = area = perimetro = 0
resultado = ""

while True:
    print("1 Cuadrado   2 Rectangulo   3 Circulo   4 Salir")
    op = int(input("Opcion: "))

    if op == 1:
        x = float(input("Lado: "))
        area = x * x
        perimetro = 4 * x
        resultado = f"A: {round(area, 2)}  P: {round(perimetro, 2)}"
        print(resultado)

    elif op == 2:
        b = float(input("Base: "))
        h = float(input("Altura: "))
        area = b * h
        perimetro = 2 * (b + h)
        resultado = f"A: {round(area, 2)}  P: {round(perimetro, 2)}"
        print(resultado)

    elif op == 3:
        r = float(input("Radio: "))
        area = 3.14159265 * r * r
        perimetro = 2 * 3.14159265 * r
        resultado = f"A: {round(area, 2)}  P: {round(perimetro, 2)}"
        print(resultado)

    elif op == 4:
        print("Fin")
        break

    else:
        print("Opcion invalida")

    print()