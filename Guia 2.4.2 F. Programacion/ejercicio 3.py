estado = True
while estado:
    try:
        numerador = float(input("Ingrese el númerador: "))
        divisor = float(input("Ingrese el divisor: "))

        if divisor == 0:
            raise ValueError ("No se puede dividir por cero!")

        resultado = numerador / divisor 

        print (f" El resultado de la division es : {resultado}")
        
        estado = False
    except ValueError as ve:
        print (f" Error: {ve}")
    except ZeroDivisionError:
        print ("Error: No se puede dividir por cero.")
    finally:
        print("Fin del programa")