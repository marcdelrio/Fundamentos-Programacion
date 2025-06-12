def mayor(lista):
    may = lista[0]
    for x in range (1, len(lista)):
        if lista [x] > may:
            may = lista[x]
    return may

def menor(lista):
    men = lista[0]
    for x in range (1, len(lista)):
        if lista[x] < men:
            men = lista[x]
    return men

estado = True
while estado:
    try:
        lista = []
        print ("Ingrese 5 valores: ")
        for x in range (5):
            valor = int(input(f"Ingrese el valor {x+1}: "))
            lista.append(valor)
        
        print(f"El valor mayor ingresado es {mayor(lista)}")
        print(f"El valor menor ingresado es {menor(lista)}")

        estado = False

    except ValueError:
        print("Error: datos incorrectos.")
    finally:
        print("Final de app.")
