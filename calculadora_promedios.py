"""Trabajo 1: Sintaxis Python
Calculadora Promedios"""

UMBR_APRO = 5.0;

""" Funcion de Solicitud Calificación"""
def solicitar_calificacion():
    """Solicita calificación entre 0 y 10 """
    while True:
        ingresa = input("Por favor, ingrese una calificación de (0 - 10): ").strip()
        ingresa = ingresa.replace("," , ".")
        try:
            calificacion = float(ingresa)
        except ValueError:
            print("El número ingresado no es válido.")
            continue

        if 0 <= calificacion <= 10:
            return calificacion
        print(" La calificación ingresada no esta en el rando entre 0 y 10. ")

""" Funcion Confirmación"""
def confirmar():
    """Solicitud ingreso nuevas materias. Booleano."""
    while True:
        respuesta = input(" Desear agregar otra materia? Responda (S/N):").strip().lower()
        if respuesta == "s":
            return True
        if respuesta == "n":
            return False
        print(" La respuesta no es válida. (S/N)")

""" Ingreso de Calificaciones"""
def ingresar_calificaciones():
    """Solicita usuario materias y calificaciones."""
    materias = []
    calificaciones = []

    print("\nPor favor ingrese, los datos las materias.")
    print("Ingrese unicamente el nombre y presione Enter para terminar\n")

    while True:
        nombre = input("Materia: ").strip()

        if nombre == "":
            break

        calificacion = solicitar_calificacion()

        materias.append(nombre)
        calificaciones.append(calificacion)

        if not confirmar():
            break
        print()

    return materias, calificaciones

""" Calcula promedio"""
def calcular_promedio(calificaciones):
    """ Promedio de la lista. """
    if len(calificaciones) == 0:
        return 0
    return sum(calificaciones) / len(calificaciones)


""" determinar estados"""
def determinar_estado(calificaciones, umbral=5.0):
    """Devuelve aprobadas y reprobadas."""
    aprobadas = []
    reprobadas = []

    for i in range(len(calificaciones)):
        if calificaciones[i] >= umbral:
            aprobadas.append(i)
        else:
            reprobadas.append(i)

    return aprobadas, reprobadas

""" """
def encontrar_extremos(calificaciones):
    """Retorna la calificación más alta y la mas baja."""
    if len(calificaciones) == 0:
        return None, None

    indice_max = 0
    indice_min = 0

    for i in range(1, len(calificaciones)):
        if calificaciones[i] > calificaciones[indice_max]:
            indice_max = i
        if calificaciones[i] < calificaciones[indice_min]:
            indice_min = i

    return indice_max, indice_min


""" Desglose del resultado"""
def mostrar_resumen(materias, calificaciones, promedio,
                    aprobadas, reprobadas, indice_max, indice_min):
    print("\n" + "=" * 45)
    print("            RESUMEN DE CALIFICACIONES")
    print("=" * 45)

    print("\nMaterias registradas:")
    for i in range(len(materias)):
        print(f"  {i + 1}. {materias[i]:<25} {calificaciones[i]:>5.2f}")

    print(f"\nPromedio general: {promedio:.2f}")

    print(f"\nMaterias aprobadas ({len(aprobadas)}):")
    if aprobadas:
        for i in aprobadas:
            print(f"  - {materias[i]} ({calificaciones[i]:.2f})")
    else:
        print("  Ninguna")

    print(f"\nMaterias reprobadas ({len(reprobadas)}):")
    if reprobadas:
        for i in reprobadas:
            print(f"  - {materias[i]} ({calificaciones[i]:.2f})")
    else:
        print("  Ninguna")

    print(f"\nMejor calificación: {materias[indice_max]} con {calificaciones[indice_max]:.2f}")
    print(f"Peor calificación:  {materias[indice_min]} con {calificaciones[indice_min]:.2f}")
    print("=" * 45)


""" Funcion Principal """

def main():
    
    print("=" * 45)
    print("       CALCULADORA DE PROMEDIOS")
    print("=" * 45)

    materias, calificaciones = ingresar_calificaciones()

    if len(materias) == 0:
        print("\nNo se ingresó ninguna materia. No hay datos para mostrar.")
    else:
        promedio = calcular_promedio(calificaciones)
        aprobadas, reprobadas = determinar_estado(calificaciones, UMBR_APRO)
        indice_max, indice_min = encontrar_extremos(calificaciones)

        mostrar_resumen(materias, calificaciones, promedio,
                        aprobadas, reprobadas, indice_max, indice_min)

    print("\n¡Gracias por usar la calculadora de promedios! Hasta pronto.")

if __name__ == "__main__":
    main()
