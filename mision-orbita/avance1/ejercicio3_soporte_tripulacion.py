# ============================================================
# Archivo: ejercicio3_soporte_tripulacion.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Integrantes: Bryner Moraga Gomez
# Fecha: 12/10/2026    Versión: 1.0
# Descripción: Verifica si la nave tiene oxígeno y provisiones
#              suficientes para mantener a la tripulación.
#              Estructura de control: condicional doble (if/else).
# ============================================================

# ---------- Declaración de constantes ----------
# Este ejercicio no requiere constantes: solo compara valores
# disponibles contra valores requeridos ingresados por el usuario.

# ---------- Entrada de datos ----------
oxigeno_disponible = int(input("Ingrese el oxígeno disponible: "))
oxigeno_requerido = int(input("Ingrese el oxígeno requerido: "))
provisiones_disponibles = int(input("Ingrese las provisiones disponibles: "))
provisiones_requeridas = int(input("Ingrese las provisiones requeridas: "))

# ---------- Decisión y salida de resultados ----------
# Se usa "and" porque la tripulación necesita AMBOS recursos;
# ">=" porque tener exactamente lo requerido sí es suficiente.
# No se indica cuál recurso falla, según la consigna.
print()
if oxigeno_disponible >= oxigeno_requerido and provisiones_disponibles >= provisiones_requeridas:
    print("La nave posee recursos suficientes para la tripulación.")
else:
    print("La nave no posee recursos suficientes para la tripulación.")
