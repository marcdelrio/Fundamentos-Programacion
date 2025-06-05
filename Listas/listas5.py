#Ejericio ordenamiento de datos en listas
estado = True
sueldos = []
while estado:
    try:
        print("Ingrese 5 sueldos")
        for x in range (5):
            sueldo = int(input(f"Ingrese el sueldo {x+1}:"))

            while sueldo <= 0:
                sueldo = int(input(f"El sueldo ingresado no es valido. Intente nuevamente:"))
            sueldos.append(sueldo)

#Generamos el proceso de ordenamiento
        print(f"La lista de sueldos ingresados es: {sueldos}")

        for k in range (4):
            for x in range (4):
                if sueldos[x] > sueldos[x+1]:
                    aux = sueldos[x]
                    sueldos[x] = sueldos[x+1]
                    sueldos[x+1] = aux
        print (f"La lista ordenada es: {sueldos}")
        estado = False
    except ValueError:
        print("Error: dato incorrecto.")
    finally:
        print("App lista ordenada")