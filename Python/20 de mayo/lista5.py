estado = True
while estado:
    try:
        numeros = []
        print("Ingrese 5 valores enteros: ")

        for x in range(5):
            numero = int(input(f"Ingrese el valor {x+1}: "))
            numeros.append(numero)
        
        #Buscamos el mayor y vemos las veces que se repite

        contador = 0
        mayor = numeros[0]

        for x in range(1,len(numeros)):
            if numeros[x]> mayor:
                mayor = numeros[x]
        
        for x in range (len(numeros)):
            if mayor == numeros[x]:
                contador += 1
        print (f"El número mayor es {mayor} y se repite {contador} veces.")
        estado = False
    except ValueError:
        print("Dato incorrecto")
    finally:
        print("Fin del programa.")
