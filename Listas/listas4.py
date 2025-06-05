estado = True
numeros =[]
while estado:
    try:
        print("Ingrese cinco números enteros:")
        for x in range (5):
            numero = int(input(f"Ingrese el valor {x+1}: "))
            numeros.append(numero)

        mayor = numeros[0]
        contador = 0

        for x in range (1,5):
            if numeros [x] > mayor:
                mayor = numeros[x]

        for x in range (5):
            if mayor == numeros[x]:
                contador += 1
        
        print(f"Los valores ingresados son: {numeros}")
        print(f"El mayor valor ingresado es: {mayor}")
        print(f"El valor mayor se ingresó {contador} veces")
        estado = False

    except ValueError:
        print("Error: dato incorrecto")
    finally:
        print("Se finaliza de forma correcta.")