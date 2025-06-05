estado = True
while estado:
    try:
        productos = []
        precios = []

        print("Ingrese 5 productos con sus precios")
        for x in range(5):
            producto =input(f"Ingrese el preoducto {x + 1}: ")
            productos.append(producto)
            precio = int(input(f"Ingrese el precio del producto {x + 1}: "))
            precios.append(precio)

        contador = 0
        primero = precios[0]
        for x in range(1,len(precios)):
            if precios[x] > primero:
                contador += 1
        
        print(f"El precio mayor es {primero} y hay {contador} productos mayores al primer precio.")
        estado = False
    except ValueError:
        print ("Error: Valor invalido.")
    finally:
        print("Fin del programa.")