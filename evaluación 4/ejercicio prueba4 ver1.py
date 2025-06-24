def mostrar_menu():
    print("\nTOTEM AUTOATENCIÓN CAFECONLECHE")
    print("1.- Comprar entrada a Cats.")
    print("2.- Cambio de función.")
    print("3.- Mostrar stock de funciones.")
    print("4.- Salir.")

def comprar_entrada(compradores, stock):
    print("\n-- Comprar entrada a Cats --")
    nombre = input("Nombre del comprador: ").strip()
    if nombre in compradores:
        print("Error: el nombre de comprador ya existe.")
        return
    print(f"Seleccione función:\n"
          f"1. Cats Día Viernes ({stock[1]} entradas)\n"
          f"2. Cats Día Sábado ({stock[2]} entradas)")
    sel = input("Función (1 ó 2): ").strip()
    if sel not in ("1", "2"):
        print("Error: opción de función inválida.")
        return
    func = int(sel)
    if stock[func] <= 0:
        print(f"Error: no hay entradas disponibles para la función {func}.")
        return
    compradores[nombre] = func
    stock[func] -= 1
    print(f"Entrada registrada en función {func}! Stock restantes:")
    for f in (1, 2):
        dia = "Viernes" if f == 1 else "Sábado"
        print(f"  Función {f} ({dia}): {stock[f]}")

def cambio_funcion(compradores, stock):
    print("\n-- Cambio de función --")
    nombre = input("Nombre del comprador: ").strip()
    if nombre not in compradores:
        print("Error: comprador no encontrado.")
        return
    orig = compradores[nombre]
    destino = 2 if orig == 1 else 1
    print(f"Cambiar de función {orig} a {destino}? (S/N): ", end="")
    resp = input().strip().lower()
    if resp != 's':
        print("Cambio cancelado.")
        return
    if stock[destino] <= 0:
        print("Error: no hay stock en la función destino.")
        return
    compradores[nombre] = destino
    stock[orig] += 1
    stock[destino] -= 1
    print(f"Cambio exitoso. Ahora está en función {destino}.")

def mostrar_stock(capacidades, stock):
    print("\n-- Stock de Funciones --")
    for f in (1, 2):
        dia = "Viernes" if f == 1 else "Sábado"
        vendidas = capacidades[f] - stock[f]
        print(f"Función {f} ({dia}): Disponibles {stock[f]}, Vendidas {vendidas}")

def main():
    capacidades = {1: 150, 2: 180}
    stock = dict(capacidades)
    compradores = {}
    while True:
        mostrar_menu()
        opc = input("Seleccione una opción: ").strip()
        if opc == '1':
            comprar_entrada(compradores, stock)
        elif opc == '2':
            cambio_funcion(compradores, stock)
        elif opc == '3':
            mostrar_stock(capacidades, stock)
        elif opc == '4':
            print("\nPrograma terminado...")
            break
        else:
            print("Debe ingresar una opción válida!!")

if __name__ == "__main__":
    estado = True
    while estado:
        try:
            main()
            estado = False
        except ValueError:
            print("Error en la aplicación.")
        finally:
            print("Gracias por usar la app.")
