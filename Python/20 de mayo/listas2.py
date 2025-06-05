#Ingresa 5 valores por teclado, los añade a una lista e imprime la misma

estado = True
while estado:
    try:
        valores = []
        print("Ingrese 5 números enteros:")
        for x in range(5):
            valor = int(input(f"Ingrese el valor {x+1}: "))        
            valores.append(valor)
        
        print(valores)
        estado = False

    except ValueError:
        print("Dato no válido")
    finally:
        print("Fin del programa")