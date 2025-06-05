estado = True
while estado:
    try:
        precio_liviano = 1000
        precio_normal = 2000
        bultos_livianos = 0
        bultos_normales = 0
        x = 1
        
        bulto = int(input("Ingrese el número de bultos: "))
        while x <=  bulto:
            peso = int(input(f"Ingrese el peso del bulto {x}: "))

            if peso >= 1 and peso <= 5:
                bultos_livianos +=1
            elif peso >= 6 and peso <= 10:
                bultos_normales += 1
            else:
                print("El peso ingresado está fuera del límite")
            x += 1

        total_livianos = bultos_livianos * precio_liviano
        total_normal = bultos_normales * precio_normal
        total = total_livianos + total_normal

        print(f"{bultos_livianos} Bultos livianos: ${total_livianos}")
        print(f"{bultos_normales} Bultos Normal: ${total_normal}")
        print(f"Valor total a pagar: ${total}")

        estado = False
    except ValueError:
        print("Los valores ingresados no son válidos")
        estado = True