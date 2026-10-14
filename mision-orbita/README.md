# Misión Órbita — Simulador de exploración espacial en Python

Proyecto del curso **SOFT-01 Principios de Programación 1** (Sección SCV6, periodo C3-2026),
Universidad CENFOTEC. Docente: Verónica Mora Lezcano.

## Descripción

Simulador básico para preparar misiones de exploración. Este **Avance 1 — Preparación de la misión**
contiene cuatro algoritmos independientes:

| Archivo | Propósito | Estructura de control |
|---|---|---|
| `avance1/ejercicio1_recursos.py` | Calcula combustible, oxígeno, energía y provisiones | Secuencial |
| `avance1/ejercicio2_combustible.py` | Verifica el combustible y advierte si el margen es bajo | Condicional simple (`if`) |
| `avance1/ejercicio3_soporte_tripulacion.py` | Verifica oxígeno y provisiones para la tripulación | Condicional doble (`if/else`) |
| `avance1/ejercicio4_autorizacion.py` | Autoriza o rechaza el lanzamiento | Condicional doble sin anidación |

## Integrantes

- Bryner Moraga Gomez

## Requisitos y ejecución

Python 3.10 o superior. No se usan librerías externas.

```bash
cd avance1
python ejercicio1_recursos.py
python ejercicio2_combustible.py
python ejercicio3_soporte_tripulacion.py
python ejercicio4_autorizacion.py
```

Cada programa solicita los datos por consola (valores enteros positivos) y muestra los resultados.

## Convenciones y estilos

- Variables en minúscula con `snake_case` y nombres descriptivos.
- Constantes en `MAYÚSCULAS` declaradas al inicio de cada archivo; sin números mágicos en las fórmulas.
- Indentación de 4 espacios, espacios alrededor de operadores y líneas en blanco entre bloques.
- Cada archivo inicia con un encabezado (archivo, curso, integrantes, fecha, versión, descripción)
  y cada bloque lógico (constantes, entrada, procesamiento, decisión, salida) lleva un comentario.
- Restricciones del avance: sin ciclos, colecciones, funciones propias (`def`), módulos,
  archivos, POO, condicionales anidadas ni `elif`.
- Mensajes de commit descriptivos en español (ej.: "Agrega validación de combustible de regreso en ejercicio 4").

## Estructura

```
mision-orbita/
├── README.md
├── avance1/
│   ├── ejercicio1_recursos.py
│   ├── ejercicio2_combustible.py
│   ├── ejercicio3_soporte_tripulacion.py
│   └── ejercicio4_autorizacion.py
└── documentacion/
    └── avance1.pdf
```
