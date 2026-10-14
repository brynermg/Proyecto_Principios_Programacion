# ============================================================
# Archivo: ejercicio1_recursos.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Integrantes: Bryner Moraga Gomez
# Fecha: 12/10/2026    Versión: 1.0
# Descripción: Calcula los recursos necesarios (combustible,
#              oxígeno, energía y provisiones) para una misión.
#              Estructura de control: secuencial.
# ============================================================

# ---------- Declaración de constantes ----------
# Valores fijos de la consigna; se declaran aquí para evitar
# "números mágicos" dentro de las fórmulas.
CONSUMO_COMBUSTIBLE_DIA = 8        # unidades de combustible por día de viaje
RESERVA_COMBUSTIBLE = 10           # reserva obligatoria para emergencias
TRAMOS_VIAJE = 2                   # ida + regreso (misma duración)
CONSUMO_OXIGENO_TRIPULANTE = 2     # oxígeno por tripulante por día
OXIGENO_EMERGENCIA = 5             # oxígeno adicional de emergencia
CONSUMO_ENERGIA_DIA = 5            # energía por día de viaje
ENERGIA_EXPLORACION = 10           # energía para operaciones de exploración
CONSUMO_PROVISIONES_TRIPULANTE = 1 # provisiones por tripulante por día
PROVISIONES_ADICIONALES = 3        # provisiones extra

# ---------- Entrada de datos ----------
nombre_mision = input("Ingrese el nombre de la misión: ")
cantidad_tripulantes = int(input("Ingrese la cantidad de tripulantes: "))
dias_viaje = int(input("Ingrese los días estimados para llegar al destino: "))

# ---------- Procesamiento ----------
# El regreso dura lo mismo que la ida, por eso ambos tramos
# usan los mismos días y el mismo consumo diario.
combustible_ida = dias_viaje * CONSUMO_COMBUSTIBLE_DIA
combustible_regreso = dias_viaje * CONSUMO_COMBUSTIBLE_DIA

# La reserva se suma porque la nave no debe llegar justa al regreso.
combustible_total = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE

# Oxígeno y provisiones dependen de la tripulación y de ambos tramos.
oxigeno_requerido = (dias_viaje * CONSUMO_OXIGENO_TRIPULANTE * TRAMOS_VIAJE
                     * cantidad_tripulantes + OXIGENO_EMERGENCIA)

# La energía depende solo de los días (la nave), no de la tripulación.
energia_requerida = (dias_viaje * CONSUMO_ENERGIA_DIA * TRAMOS_VIAJE
                     + ENERGIA_EXPLORACION)

provisiones_requeridas = (dias_viaje * cantidad_tripulantes
                          * CONSUMO_PROVISIONES_TRIPULANTE * TRAMOS_VIAJE
                          + PROVISIONES_ADICIONALES)

# ---------- Salida de resultados ----------
print()
print("Misión:", nombre_mision)
print("Tripulantes:", cantidad_tripulantes)
print("Duración estimada hasta el destino:", dias_viaje, "días")
print("Combustible para llegar:", combustible_ida, "unidades")
print("Combustible para regresar:", combustible_regreso, "unidades")
print("Reserva de combustible:", RESERVA_COMBUSTIBLE, "unidades")
print("Combustible total requerido:", combustible_total, "unidades")
print("Oxígeno requerido:", oxigeno_requerido, "unidades")
print("Energía requerida:", energia_requerida, "unidades")
print("Provisiones requeridas:", provisiones_requeridas, "unidades")
