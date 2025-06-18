def mostrar(paises):
    for clave in paises:
        print(clave, paises[clave])

estado = True
while estado:
    try:
        paises = {'Chile':20000000, 'Argentina': 40000000, 'Italia': 45000000}
        mostrar(paises)

        estado = False
    except ValueError:
        print("Error")
    finally:
        print("App diccionarios")