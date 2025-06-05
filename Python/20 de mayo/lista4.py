estado = True
while estado:
    try:
        personas = []
        
        print("Ingrese el nombre de 5 personas:")
        for x in range (5):
            nombre = input(f"Ingrese el nombre de la persona {x+1}: ")
            personas.append(nombre)

        #Buscar el menor
        menor = personas [0]
        for x in range (1,len(personas)):
            if personas[x] < menor:
                menor = personas[x]

        print(f"La lista de personas es {personas}:")
        print(f"La persona menor en orden alfabético es {menor}")
        
        estado = False
    except ValueError:
        print(f"Error: {ve}")
    finally:
        print("Programa terminado.")