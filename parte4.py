# Diccionario inicial con estudiantes y calificaciones
estudiantes = {
    "Juan": 5.0,
    "Ana": 4.2,
    "Luis": 4.5
}

while True:
    nombre = input("Ingrese el nombre del estudiante (o 'salir' para finalizar): ")
    if nombre.lower() == "salir":
        break

    calificacion = float(input(f"Ingrese la calificación de {nombre}: "))

    # Verificar si el estudiante ya existe y actualizar su calificación
    if nombre in estudiantes:
        estudiantes[nombre] = calificacion
        print(f"Calificación actualizada: {nombre} ahora tiene {calificacion}")
    else:
        estudiantes[nombre] = calificacion
        print(f"Nuevo estudiante agregado: {nombre} con calificación {calificacion}")

# Mostrar todos los estudiantes y sus calificaciones
print("\nLista de estudiantes y calificaciones:")
for estudiante, nota in estudiantes.items():
    print(f"{estudiante}: {nota}")
