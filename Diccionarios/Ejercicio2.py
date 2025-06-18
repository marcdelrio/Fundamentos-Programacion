def cargar():
    productos = {}
    print ("Ingrese 3 productos")
    for x in range(3):
        producto =input(f"Ingrese el producto {x+1}: ")
        precio = int(input(f"Ingrese el valor del producto {producto}: "))
        productos[producto] = precio
        
    return productos

def imprimir(productos):
    print("Lista de productos")
    for producto in productos:
        print(producto, productos[producto])

def mayor(productos):
    print("Lista de productos mayores a $10.0000")
    for producto in productos:
        if productos[producto] > 10000:
            print(producto)

estado = True
while estado:
    try:
        productos = cargar()
        imprimir(productos)
        mayor (productos)

        estado = False
    
    except ValueError:
        print("Error")
    finally:
        print("App finalizada")