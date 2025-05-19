# Determinar si un número es par o impar
num = int(input("Ingrese un número: "))
if num % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

# Determinar si un número tiene uno, dos o tres dígitos
numero = int(input("Ingrese un número positivo entre 1 y 999: "))
if 1 <= numero <= 9:
    print("El número tiene un dígito.")
elif 10 <= numero <= 99:
    print("El número tiene dos dígitos.")
elif 100 <= numero <= 999:
    print("El número tiene tres dígitos.")
else:
    print("El número ingresado no es válido.")
