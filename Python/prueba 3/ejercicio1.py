estado = True
while estado:
    try:
        total_libros = int(input("Ingrese la cantidad de libros prestados: "))
        break
    except ValueError:
        print("Debes ingresar un número entero para la cantidad de libros.")

mas_de_15 = 0
igual_o_15 = 0
for x in range(total_libros):
    titulos = input("Ingrese el título del libro: ")
    while True: 
        try:
            dias = int(input(f"Ingrese los días de préstamo para {titulos}: " ))
            break
        except ValueError:
            print(" Debes ingresar un número entero para los días de préstamos.")

    if dias > 15:
        print("Prestamo por más de 15 días")
        mas_de_15 += 1
    else:
        print("Préstamo por 15 días o menos")
        igual_o_15 += 1

        estado = False

print(f"Se registraron {mas_de_15} libros con préstamo mayor a 15 días.")
print(f"Se registraron {igual_o_15} libros con préstamos menor o igual a 15 días.")