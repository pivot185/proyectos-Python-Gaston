def celsius_a_fahrenheit(c):
    f = (c * 9 / 5) + 32
    return f

numero = float(input("Ingresá la temperatura en Celsius: "))
resultado = celsius_a_fahrenheit(numero)
print("La temperatura en Fahrenheit es:", resultado)
