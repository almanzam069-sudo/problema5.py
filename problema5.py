# ==========================================
# PROBLEMA 5 - CONTROL DE HORAS TRABAJADAS
# ==========================================

# Matriz de recursos
recursos = [
    ["Carlos", 8, 8, 9, 8, 8],
    ["María", 7, 8, 7, 8, 7],
    ["Andrés", 10, 9, 9, 8, 9],
    ["Luisa", 8, 8, 8, 8, 8]
]

# Función para calcular total y clasificación
def calcular_horas(horas):

    total = sum(horas)

    if total > 40:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estándar"

    return total, clasificacion

# Título
print("===================================")
print(" REPORTE DE HORAS SEMANALES ")
print("===================================")

# Recorrer matriz
for recurso in recursos:

    nombre = recurso[0]

    horas_semana = recurso[1:]

    total, clasificacion = calcular_horas(horas_semana)

    print("Empleado:", nombre)
    print("Total horas:", total)
    print("Clasificación:", clasificacion)
    print("-----------------------------------")