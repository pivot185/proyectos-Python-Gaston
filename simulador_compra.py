print ("gorra azul - $500")
print ("gorra blanca - $450")
print ("gorra verde - $500")
print ("gorra roja - $450")

producto = input("elije tu producto:")
cantidad = int(input("cuantas quieres:"))

if producto == "gorra azul":
    precio = 500
elif producto == "gorra blanca":
    precio = 450
elif producto == "gorra verde":
    precio = 500
elif producto == "gorra roja":
    precio = 450
else:
    print("Ese producto no está disponible.")
    exit()
        
total = precio * cantidad
print(f"Compraste {cantidad} {producto}. Total a pagar: ${total}")
