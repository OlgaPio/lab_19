n = int(input("Cuántos empleados tiene la empresa: "))
conta1 = 0
conta2 = 0
gastos = 0

x = 1
while x <= n:
    sueldo = float(input(f"Ingrese el sueldo del empleado {x}: "))
    gastos += sueldo

    if 1000000 <= sueldo <= 3000000:
        conta1 += 1
    elif sueldo > 3000000:
        conta2 += 1

    x += 1

print(f"Empleados con sueldo entre $1.000.000 y $3.000.000: {conta1}")
print(f"Empleados con sueldo mayor a $3.000.000: {conta2}")
print(f"Total que gasta la empresa en sueldos: ${gastos}")
