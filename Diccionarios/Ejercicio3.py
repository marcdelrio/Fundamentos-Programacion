def cargar():
    personas = {}
    print("Registre 3 personas")
    for x in range(3):
        numero = input(f"Ingrese el número de documento de la persona {x+1}: ")
        nombre = input(f"Registre el nombre de la persona con número {numero}: ")
        personas[numero] = nombre
    return personas

def mostrar(personas):
    print("Lista de personas")
    for persona in personas:
        print(persona,personas[persona])
    
def busqueda(personas):
    numero = input("Ingrese el número de la persona que busca: ")
    if numero in personas:
        print(f"El nombre de la persona es {personas[numero]}")
    else:
        print("No hay una persona registrada con este número.")

estado = True
while estado:
    try:
        personas = cargar()
        mostrar(personas)
        busqueda(personas)
        estado = False
    except ValueError:
        print("Error en la aplicación.")
    finally:
        print("Gracias por usar la app")
             