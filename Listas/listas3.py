estado =True
nombres =[]
while estado:
    try:
        print ("Ingrese 5 nombres de personas")
        for x in range (5):
            nombre = input(f"Ingrese el nombre de la persona {x+1}: ")
            nombres.append(nombre)
        menor = nombres [0]

        for x in range (1,5):
            if nombres[x]< menor:
                menor = nombres[x]

        print (f"El nombre menor alfabeticamente es: {menor} ")
        estado = False

    except ValueError:
        print("Dato incorrecto")
    finally:
        print("App de nombres")