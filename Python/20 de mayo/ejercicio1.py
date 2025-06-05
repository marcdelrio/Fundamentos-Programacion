estado = True
while estado:
    try:
        lista = [25,55,89,99,102,150,77,104]
        contador = 0
        print(len(lista))
        for x in range(len(lista)):
            if lista [x] > 100:
                contador += 1
        
        print (f"Hay {contador} números mayores a 100")
        estado = False

    except:
        print("Valor invalido")
    finally:
        print("Fin del programa")