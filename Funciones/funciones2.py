def cuadrado(a):
    return a * a

def producto(a,b):
    return a * b

def errorException():
    return "Error: dato incorrecto"

def msgApp():
    return "Aplicacion de valores"

#Programa principal

estado = True
while estado:
    try:
        print("Calculadora de cuadrado de un número")
        numero = int(input("Ingrese el valor: "))
        print(f"El cuadrado de {numero} es {cuadrado(numero)}")

        print("Calculadora de producto dos números")
        numero1= int(input("Ingrese el primer valor: "))
        numero2= int(input("Ingrese el segundo valor: "))
        resultado = producto (numero1, numero2)
        print(f"El producto es {resultado}")
        estado = False
    except ValueError:
        print(errorException())
    finally:
        print(msgApp())
