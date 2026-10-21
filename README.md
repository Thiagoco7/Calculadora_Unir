# Calculadora de promedios

Trabajo 1 - Sintaxis de Python.

Programa de consola que pide las materias con su calificación, calcula el promedio y muestra cuáles se aprobaron y cuáles no. También indica la materia con la nota más alta y la más baja.

Está hecho solo con funciones (programación estructurada), sin clases.

## Cómo ejecutarlo

Se necesita tener Python 3 instalado.

```
python calculadora_promedios.py
```

## Uso

1. Escribir el nombre de la materia.
2. Escribir la calificación (de 0 a 10). Se puede usar punto o coma para los decimales, por ejemplo `7.5` o `7,5`.
3. Responder `s` para agregar otra materia o `n` para terminar.

Si se deja el nombre de la materia vacío y se presiona Enter, también se termina el ingreso.

La nota mínima para aprobar es 5.0.

## Funciones

- `solicitar_calificacion()`: pide la nota y la valida (que sea número y que esté entre 0 y 10).
- `confirmar()`: pregunta si se quiere seguir agregando materias.
- `ingresar_calificaciones()`: guarda las materias y las notas en dos listas.
- `calcular_promedio(calificaciones)`: devuelve el promedio de las notas.
- `determinar_estado(calificaciones, umbral)`: separa las posiciones de las materias aprobadas y reprobadas.
- `encontrar_extremos(calificaciones)`: busca la posición de la nota más alta y la más baja.
- `mostrar_resumen(...)`: imprime el resumen final.
- `main()`: función principal que llama a las demás.

## Validaciones

- Si la nota no es un número, se vuelve a pedir.
- Si la nota es menor que 0 o mayor que 10, se vuelve a pedir.
- Si la respuesta a "agregar otra materia" no es `s` o `n`, se vuelve a preguntar.
- Si no se ingresa ninguna materia, el programa lo indica y termina sin hacer cálculos.

## Ejemplo

```
Materia: matematicas
Por favor, ingrese una calificación de (0 - 10): 7
 Desear agregar otra materia? Responda (S/N):s

Materia: ciencias
Por favor, ingrese una calificación de (0 - 10): 9
 Desear agregar otra materia? Responda (S/N):n

=============================================
            RESUMEN DE CALIFICACIONES
=============================================

Materias registradas:
  1. matematicas                7.00
  2. ciencias                   9.00

Promedio general: 8.00

Materias aprobadas (2):
  - matematicas (7.00)
  - ciencias (9.00)

Materias reprobadas (0):
  Ninguna

Mejor calificación: ciencias con 9.00
Peor calificación:  matematicas con 7.00
=============================================
```
