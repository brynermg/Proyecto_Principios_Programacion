# ============================================================
# Archivo: ejercicio2_combustible.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Integrantes: Bryner Moraga Gomez
# Fecha: 12/10/2026    Versión: 1.0
# Descripción: Verifica si la nave posee suficiente combustible
#              para ida, regreso y reserva, y advierte cuando el
#              margen adicional es bajo.
#              Estructura de control: condicional simple (if).
# ============================================================

# ---------- Declaración de constantes ----------
RESERVA_COMBUSTIBLE = 10    # reserva obligatoria para emergencias
MARGEN_MINIMO = 10          # por debajo de este margen se advierte

# ---------- Entrada de datos ----------
combustible_disponible = int(input("Ingrese el combustible disponible: "))
combustible_ida = int(input("Ingrese el combustible requerido para la ida: "))
combustible_regreso = int(input("Ingrese el combustible requerido para el regreso: "))

# ---------- Procesamiento ----------
# El total incluye el regreso y la reserva: llegar no es suficiente.
combustible_total = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE

# El adicional es lo que sobra después de cubrir todo lo requerido;
# puede ser negativo si el combustible no alcanza.
combustible_adicional = combustible_disponible - combustible_total

# ---------- Salida de resultados (siempre se muestran) ----------
print()
print("Combustible disponible:", combustible_disponible, "unidades")
print("Combustible requerido para llegar:", combustible_ida, "unidades")
print("Combustible requerido para regresar:", combustible_regreso, "unidades")
print("Reserva de emergencia:", RESERVA_COMBUSTIBLE, "unidades")
print("Combustible total requerido:", combustible_total, "unidades")
print("Combustible adicional:", combustible_adicional, "unidades")

# ---------- Decisión ----------
# Condicional simple: solo se actúa cuando el margen es menor que
# el mínimo (estrictamente menor; un margen de 10 no genera advertencia).
if combustible_adicional < MARGEN_MINIMO:
    print("Advertencia: el margen adicional de combustible es bajo.")
