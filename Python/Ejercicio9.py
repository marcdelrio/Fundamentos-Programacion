def leer_edades(cantidad, nombre_turno):
    """Pide `cantidad` edades por teclado y devuelve la lista de enteros."""
    edades = []
    for i in range(1, cantidad + 1):
        while True:
            try:
                edad = int(input(f"Ingrese la edad {i} del turno {nombre_turno}: "))
                if edad <= 0:
                    raise ValueError
                edades.append(edad)
                break
            except ValueError:
                print("⚠️  Por favor ingrese un número entero positivo.")
    return edades


# 1. Leer las edades de cada turno
edades_mañana = leer_edades(5, "mañana")
edades_tarde  = leer_edades(6, "tarde")
edades_noche  = leer_edades(11, "noche")

# 2. Calcular los promedios
prom_mañana = sum(edades_mañana) / len(edades_mañana)
prom_tarde  = sum(edades_tarde)  / len(edades_tarde)
prom_noche  = sum(edades_noche)  / len(edades_noche)

# 3. Imprimir los promedios
print(f"\nPromedio turno mañana: {prom_mañana:.2f}")
print(f"Promedio turno tarde : {prom_tarde:.2f}")
print(f"Promedio turno noche : {prom_noche:.2f}")

# 4. Determinar cuál es mayor (considera empates)
promedios = {
    "mañana": prom_mañana,
    "tarde" : prom_tarde,
    "noche" : prom_noche
}
mayor_valor = max(promedios.values())
turnos_mayores = [turno for turno, prom in promedios.items() if prom == mayor_valor]

# 5. Mostrar resultado
if len(turnos_mayores) == 1:
    print(f"\n➡️  El turno con promedio de edad mayor es el turno **{turnos_mayores[0]}** ({mayor_valor:.2f} años).")
else:
    empates = ", ".join(turnos_mayores)
    print(f"\n➡️  Hay un empate. Los turnos con mayor promedio de edad son: {empates} ({mayor_valor:.2f} años).")
