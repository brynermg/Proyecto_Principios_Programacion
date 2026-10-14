# ============================================================
# Archivo: ejercicio4_autorizacion.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Integrantes: Bryner Moraga Gomez
# Fecha: 12/10/2026    Versión: 1.0
# Descripción: Realiza la verificación general de recursos y
#              autoriza o rechaza el lanzamiento de la misión.
#              Estructura de control: condicional doble (if/else)
#              sin anidación, con condición compuesta.
# ============================================================

# ---------- Declaración de constantes ----------
RESERVA_COMBUSTIBLE = 10    # reserva obligatoria para emergencias

# ---------- Entrada de datos ----------
combustible_disponible = int(input("Ingrese el combustible disponible: "))
combustible_ida = int(input("Ingrese el combustible requerido para llegar al destino: "))
combustible_regreso = int(input("Ingrese el combustible requerido para regresar: "))
oxigeno_disponible = int(input("Ingrese el oxígeno disponible: "))
oxigeno_requerido = int(input("Ingrese el oxígeno requerido: "))
energia_disponible = int(input("Ingrese la energía disponible: "))
energia_requerida = int(input("Ingrese la energía requerida: "))
provisiones_disponibles = int(input("Ingrese las provisiones disponibles: "))
provisiones_requeridas = int(input("Ingrese las provisiones requeridas: "))

# ---------- Procesamiento ----------
# Se compara contra el total (ida + regreso + reserva) para que
# nunca se autorice una misión que solo tiene combustible para llegar.
combustible_total = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE

# ---------- Decisión y salida de resultados ----------
# Una sola condición compuesta con "and": basta que un recurso
# falte para rechazar. No se indica cuál recurso provocó el rechazo.
print()
print("Combustible total requerido:", combustible_total, "unidades")
if (combustible_disponible >= combustible_total
        and oxigeno_disponible >= oxigeno_requerido
        and energia_disponible >= energia_requerida
        and provisiones_disponibles >= provisiones_requeridas):
    print("Lanzamiento autorizado.")
else:
    print("Lanzamiento no autorizado. La misión debe ser revisada.")
