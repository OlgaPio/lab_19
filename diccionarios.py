# Diccionario con nombres de estudiantes y calificaciones
calificaciones = {
    "Juan": 5.0,
    "Ana": 4.2,
    "Luis": 4.5
}

# Encontrar estudiante con la calificación más alta
nombre_max = max(calificaciones, key=calificaciones.get)
print(f"El estudiante con la calificación más alta es {nombre_max} con una calificación de {calificaciones[nombre_max]}.")
