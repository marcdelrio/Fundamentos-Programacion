estado = True
while estado:
    try:
        contador = 0
        num = int(input("Ingrese el número de triángulos: "))
        for x in range (num):
            base = int(input(f"Ingrese la base del triángulo {x + 1}: "))
            altura = int(input(f"Ingrese la altura del triángulo {x + 1} : "))
            superficie = (base * altura) /2


            if superficie > 12:
                contador = contador +1

            print(f"La superficie del triángulo {x+1} es: {superficie}")

        print(f"Hay {contador} triángulos con superficie mayor que 12")

        estado = False
    except:
        print("Los datos ingresados no son válidos")
        estado= True