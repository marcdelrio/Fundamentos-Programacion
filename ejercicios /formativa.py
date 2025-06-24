# Programa de gestión de turistas en Chile con validación global
turistas = {
    "001": ["John Doe", "Estados Unidos", "12-01-2024"],
    "002": ["Emily Smith", "Estados Unidos", "23-03-2024"],
    "012": ["Julian Martinez", "Argentina", "19-09-2023"],
    "014": ["Agustin Morales", "Argentina", "28-03-2024"],
    "005": ["Carlos Garcia", "Mexico", "10-05-2024"],
    "006": ["Maria Lopez", "Mexico", "08-12-2023"],
    "007": ["Joao Silva", "Brasil", "20-06-2024"],
    "003": ["Michael Brown", "Estados Unidos", "05-07-2023"],
    "004": ["Jessica Davis", "Estados Unidos", "15-11-2024"],
    "008": ["Ana Santos", "Brasil", "03-10-2023"],
    "010": ["Martin Fernandez", "Argentina", "13-02-2023"],
    "011": ["Sofia Gomez", "Argentina", "07-04-2024"],
}

def turistas_por_pais(pais_buscado):
    resultado = []
    for datos in turistas.values():
        nombre, pais, _ = datos
        if pais.lower() == pais_buscado.lower():
            resultado.append(nombre)
    if resultado:
        print("Turistas de", pais_buscado + ":", resultado)
    else:
        print(f"No hay turistas de {pais_buscado}.")

def turistas_por_mes(mes):
    total = len(turistas)
    contador = 0
    for datos in turistas.values():
        fecha = datos[2]  # "DD-MM-AAAA"
        mes_ingreso = int(fecha.split("-")[1])
        if mes_ingreso == mes:
            contador += 1
    porcentaje = round((contador / total) * 100, 1)
    return porcentaje

def eliminar_turista():
    nombre_buscado = input("Ingrese nombre del turista a eliminar: ").strip()
    clave_encontrada = None
    for clave, datos in turistas.items():
        if datos[0].lower() == nombre_buscado.lower():
            clave_encontrada = clave
            break
    if clave_encontrada:
        del turistas[clave_encontrada]
        print("Turista eliminado con éxito.")
    else:
        print("Turista no encontrado. No se pudo eliminar.")

def main():
    while True:
        print("\n*** MENÚ PRINCIPAL ***")
        print("1.- Turistas por país.")
        print("2.- Turista por mes.")
        print("3.- Eliminar turista.")
        print("4.- Salir.")
        opcion = input("Ingrese opción: ").strip()

        if opcion == "1":
            pais = input("Ingrese país a buscar: ").strip()
            turistas_por_pais(pais)

        elif opcion == "2":
            while True:
                mes_str = input("Ingrese mes a buscar (1-12): ").strip()
                mes = int(mes_str)  # Puede lanzar ValueError
                if 1 <= mes <= 12:
                    break
                print("Debe ingresar un valor entre 1 y 12.")
            pct = turistas_por_mes(mes)
            print(f"El {pct}% de los turistas ingresó en el mes {mes}.")

        elif opcion == "3":
            eliminar_turista()

        elif opcion == "4":
            print("Programa terminado...")
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
            # Captura cualquier conversión inválida a entero en entradas
            print("Error, el dato ingresado es erróneo. Por favor inténtalo de nuevo.")
        finally:
            print("Gracias por utilizar nuestro programa.")




