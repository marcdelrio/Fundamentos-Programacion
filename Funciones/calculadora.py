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

estado = True
while estado:
    try:
        valor1 = int(input("Ingrese el primer valor: "))
        valor2 = int(input("Ingrese el segundo valor: "))

        print(f"La suma es {suma(valor1,valor2)}")
        print(f"La resta es {resta(valor1,valor2)}")
        print(f"El producto es {producto(valor1,valor2)}")
        print(f"La división es {division(valor1,valor2)}")

        estado = False
    except ValueError:
        print(errorException())
    finally:
        print(msgApp())