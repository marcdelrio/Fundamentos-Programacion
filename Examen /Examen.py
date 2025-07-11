
productos ={
'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '12GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '12GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

stock = {
  '123FHD': [290890, 32],
  '2175HD': [327990, 4],
  '342FHD': [444990, 7],
  '8475HD': [387990, 10],
  'FS1230HD': [249990, 0],
  'GF75HD': [749990, 2],
  'JjfFHD': [424990, 1],
  'UWU131HD': [349990, 1],
  'fgdxFHD': [664990, 21]
}


def mostrar_menu():
    print("***MENU PRINCIPAL***")
    print("1. Stock marca.")
    print("2. Búsqueda por precio.")
    print("3. Eliminar Producto.")
    print("4.- Salir.")

def stock_marca(marca):
    total = sum(stock[m][1] for m, datos in productos.items()
                if datos[0].lower() == marca.lower())
    print(f"El stock es: {total}")

def búsqueda_precio(p_min, p_max):
    if not isinstance(p_min, int) or not isinstance(p_max, int):
        print("Error: los precios deben ser números enteros.")
        return
    if p_min <= 0 or p_max <= 0:
        print("Error: los precios deben ser mayores que 0.")
        return
    if p_min > p_max:
        print("Error: el precio mínimo no puede ser mayor que el precio máximo.")
        return
    resultados = [
        f"{productos[m][0]}--{m}"
        for m, (precio, cant) in stock.items()
        if cant > 0 and p_min <= precio <= p_max
    ]
    if resultados:
        resultados.sort()
        print(f"Los notebooks entre los precios consultados son: {resultados}")
    else:
        print("No hay notebooks en ese rango de precios.")


def eliminar_producto(modelo):
    llave_a_eliminar = None

    for llave_real in productos.keys():
        if llave_real.lower() == modelo.lower():
            llave_a_eliminar = llave_real
            break


    if llave_a_eliminar:
        del productos[llave_a_eliminar]
        del stock[llave_a_eliminar]
        return True
    else:
        return False


def main():
    while True:
        mostrar_menu()

        estado = True
        while estado:
            try:
                opcion = int(input("Ingrese opción: "))
                estado = False
            except ValueError:
                print("Error, el dato ingresado es erroneo")

        if opcion == 1:
            marca = input("Ingrese marca a consultar: ")
            stock_marca(marca)

        elif opcion == 2:
            while True:
                try:
                    p_min = int(input("Ingrese precio mínimo: "))
                    p_max = int(input("Ingrese precio máximo: "))
                    búsqueda_precio(p_min, p_max)
                    break
                except ValueError:
                    print("Debe ingresar valores enteros!!")

        elif opcion == 3:
            while True:
                modelo = input("Ingrese modelo a eliminar: ")
                if eliminar_producto(modelo):
                    print("Producto eliminado!!")
                else:
                    print("El modelo no existe!!")
                if input("Desea eliminar otro producto (s/n)?: ").lower() not in ('s', 'si'):
                    break

        elif opcion == 4:
            print("Programa finalizado.")
            break

        else:
            print("Debe seleccionar una opción válida!!")

if __name__ == "__main__":
    main()