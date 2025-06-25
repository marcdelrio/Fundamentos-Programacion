def main():
    capacidades = {1: 150, 2: 180}
    stock = capacidades.copy()
    compradores = {}  # nombre_comprador → función

    while True:
        # Menú principal
        print()
        print("TOTEM AUTOATENCIÓN CAFECONLECHE")
        print("1.- Comprar entrada a Cats.")
        print("2.- Cambio de función.")
        print("3.- Mostrar stock de funciones.")
        print("4.- Salir.")
        opcion = input("Seleccione una opción: ").strip()

        # 1. Comprar entrada
        if opcion == '1':
            print("-- Comprar entrada a Cats --")
            nombre_comprador = input("Nombre del comprador: ").strip()
            if nombre_comprador in compradores:
                print("Error: ese comprador ya existe.")
                continue

            # Mostrar funciones y stock
            print("Seleccione función:")
            print(f"1. Cats Día Viernes ({stock[1]} entradas)")
            print(f"2. Cats Día Sábado ({stock[2]} entradas)")
            seleccion_funcion = input("Función (1 ó 2): ").strip()
            if seleccion_funcion not in ('1', '2'):
                print("Error: opción de función inválida.")
                continue
            funcion = int(seleccion_funcion)

            # Verificar stock
            if stock[funcion] <= 0:
                print(f"Error: no hay más entradas en la función {funcion}.")
                continue

            # Registrar compra y mostrar stock restante
            compradores[nombre_comprador] = funcion
            stock[funcion] -= 1
            print(f"Entrada registrada en función {funcion}! Stock restantes:")
            print(f"  Función 1 (Viernes): {stock[1]}")
            print(f"  Función 2 (Sábado): {stock[2]}")
            continue

        # 2. Cambio de función
        if opcion == '2':
            print("-- Cambio de función --")
            nombre_comprador = input("Nombre del comprador: ").strip()
            if nombre_comprador not in compradores:
                print("Error: comprador no encontrado.")
                continue

            funcion_origen = compradores[nombre_comprador]
            funcion_destino = 2 if funcion_origen == 1 else 1
            confirmacion = input(
                f"Cambiar de función {funcion_origen} a {funcion_destino}? (S/N): "
            ).strip().lower()
            if confirmacion != 's':
                print("Cambio cancelado.")
                continue
            if stock[funcion_destino] <= 0:
                print("Error: no hay stock en la función destino.")
                continue

            compradores[nombre_comprador] = funcion_destino
            stock[funcion_origen] += 1
            stock[funcion_destino] -= 1
            print(f"Cambio exitoso. Ahora está en función {funcion_destino}.")
            continue

        # 3. Mostrar stock
        if opcion == '3':
            print("-- Stock de Funciones --")
            for numero_funcion in (1, 2):
                vendidas = capacidades[numero_funcion] - stock[numero_funcion]
                dia = "Viernes" if numero_funcion == 1 else "Sábado"
                print(
                    f"Función {numero_funcion} ({dia}): "
                    f"Disponibles {stock[numero_funcion]}, Vendidas {vendidas}"
                )
            continue

        # 4. Salir
        if opcion == '4':
            print("Programa terminado...")
            break

        # Opción inválida
        print("Debe ingresar una opción válida!!")


if __name__ == "__main__":
    continuar = True
    while continuar:
        try:
            main()
            continuar = False
        except ValueError:
            print("Error en la aplicación.")
        finally:
            print("Gracias por usar la app.")
