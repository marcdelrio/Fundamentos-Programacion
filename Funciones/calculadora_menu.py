def suma (a,b):
    return a + b 

def resta (a,b):
    return a - b

def producto(a,b):
    return a * b

def division(a,b):
    if b == 0:
        return "No se puede dividir por 0."
    return a/b

def errorException():
    return "Error: dato incorrecto"

def msgApp():
    return "Aplicación de operaciones básicas"

def menu():
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Multiplicar")
    print("4.- Dividir")
    print("5.- Salir")

def solicitar():
    opcion = int(input("Seleccione una opción: "))
    while opcion < 1 or opcion > 5:
        opcion = int(input("La opción no es válida. Intente nuevamente."))
    return opcion

# def valores():
#     valor1 = int(input("Ingrese el primer valor: "))
#     valor2 = int(input("Ingrese el segundo valor: "))

estado = True
while estado:
    try:
        valor1 = int(input("Ingrese el primer valor: "))
        valor2 = int(input("Ingrese el segundo valor: "))

    
        menu()
        op = solicitar()
        if op == 1:
            print(f"La suma es {suma(valor1,valor2)}")
        elif op == 2:
            print(f"La resta es {resta(valor1,valor2)}")
        elif op == 3:
            print(f"El producto es {producto(valor1,valor2)}")
        elif op == 4:
            print(f"La división es {division(valor1,valor2)}")
        elif op == 5:
            print("Gracias por usar nuestra App")
            estado = False
        else:
            print("Opción no válida.")
        
    except ValueError:
        print(errorException())
    finally:
        print(msgApp())