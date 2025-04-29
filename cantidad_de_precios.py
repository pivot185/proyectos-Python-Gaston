precios = []

cantidad_de_precios = int(input("Ingrese cantidad de precios: "))
for i in range(cantidad_de_precios):
    precio = float(input("Ingrese el precio\n"))
    precios.append(precio)
    
print("\nLos precios ingresados son:")
for precio in precios:
    print(f"$ {precio}")

total = sum (precios)
print (f"\nEl total a pagar es: {round (total,2)}")
