# 1) Validar sólo la cantidad de libros al inicio
while True:
    try:
        total_libros = int(input("Ingrese la cantidad de libros prestados: "))
        break
    except ValueError:
        print("Debe ingresar un número entero para la cantidad de libros.")

# 2) Inicializar contadores
mas_de_15   = 0
igual_o_15  = 0

# 3) Procesar cada libro
for _ in range(total_libros):
    titulo = input("Ingrese el título del libro: ")

    # ————— Aquí va la validación exclusiva de 'días' —————
    while True:
        try:
            dias = int(input(f"Ingrese los días de préstamo para \"{titulo}\": "))
            break
        except ValueError:
            print("Debe ingresar un número entero para los días de préstamo.")
    # ————————————————————————————————————————————————

    if dias > 15:
        print("Préstamo por más de 15 días.")
        mas_de_15 += 1
    else:
        print("Préstamo por 15 días o menos.")
        igual_o_15 += 1

# 4) Resumen final
print("\n===== Resumen de préstamos =====")
print(f"Se registraron {mas_de_15} libros con préstamo mayor a 15 días.")
print(f"Se registraron {igual_o_15} libros con préstamo menor o igual a 15 días.")
