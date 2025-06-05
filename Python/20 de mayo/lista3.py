estado = True
while estado:
    try:
        turnosAM = []
        turnosPM = []
        print("Ingrese los 4 sueldos del turno de mañana")
        for x in range(4):
            sueldo = int(input(f"Ingrese el sueldo {x+1}: "))
            turnosAM.append(sueldo)

        print("Ingrese los 4 sueldos del turno de tarde")
        for x in range (4):
            sueldo =int(input(f"Ingrese el sueldo {x+1}: "))
            turnosPM.append(sueldo)
        
        print(f"Los sueldos del turnos de mañana son {turnosAM}")
        print(f"Los sueldos del turnos de tarde son {turnosPM}")
    except ValueError:
        print("Dato incorrecto")
    finally:
        print("Programa Ejecutado")