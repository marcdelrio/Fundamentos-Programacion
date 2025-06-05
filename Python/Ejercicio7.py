
#Realizar un programa que permita cargar dos listas de 15 valores cada una. Informar con un mensaje cual de las dos listas tiene un valor acumulado mayor (mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales")
#Tener en cuenta que puede haber dos o más estructuras repetitivas en un algoritmo.

estado = True 
while estado:
    try:
        print("Ingrese 15 valores a la lista 1")
        contador = 1; lista1 = 0
        while contador <= 15:
            num= int(input(f"Ingrese el valor {contador}:"))
            lista1 = lista1 + num
            contador = contador + 1
        
        print("Ingrese 15 valores a la lista 2")
        contador = 1; lista2=0
        while contador <= 15:
            num= int(input(f"Ingrese el valor {contador}:"))
            lista2 = lista2 + num
            contador = contador + 1
        
        if lista1 > lista2:
            print("La lista 1 es mayor")
        elif lista1 < lista2:
            print("La lista 2 es mayor")
        else:
            print("Las listas son iguales")
        print(f"La suma de la lista 1 es {lista1}")
        print(f"La suma de la lista 2 es {lista2}")
    except:
        print("El dato ingresado no es válido")
        estado = True
        


        