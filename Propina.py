precio_bace = float(input("Ingrese el precio:\n"))
monto_propina = float(input("¿Cuánto % va a dejar de propina?\n"))

propina = precio_bace * (monto_propina / 100)
precio_total = precio_bace + propina

resultado = round(precio_total, 2)

print(f"El precio más propina es: {resultado}\n")
