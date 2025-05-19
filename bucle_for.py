cant1 = 0
cant2 = 0
cant3 = 0
cant4 = 0

n = int(input("Cantidad de puntos a procesar: "))

for _ in range(n):
    x = int(input("Ingrese coordenada x: "))
    y = int(input("Ingrese coordenada y: "))

    if x > 0 and y > 0:
        cant1 += 1
    elif x < 0 and y > 0:
        cant2 += 1
    elif x < 0 and y < 0:
        cant3 += 1
    elif x > 0 and y < 0:
        cant4 += 1

print(f"Primer cuadrante: {cant1} puntos")
print(f"Segundo cuadrante: {cant2} puntos")
print(f"Tercer cuadrante: {cant3} puntos")
print(f"Cuarto cuadrante: {cant4} puntos")
