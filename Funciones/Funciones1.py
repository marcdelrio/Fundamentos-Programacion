def suma(a,b):
    return a + b

estado = True
while estado:
    try:
        valor1 = int(input(f"Ingrese el primer valor: "))
        valor2 = int(input(f"Ingrese el segundo valor: "))
        resultado = suma(valor1,valor2)
        print(f"La suma es {resultado}")
        estado = False
    except ValueError:
        print("Error: Dato incorrectos.")
    finally:
        print("App de sumas.")