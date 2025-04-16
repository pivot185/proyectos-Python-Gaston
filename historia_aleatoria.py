import random

def contar_historia():
    nombre = input("Escribe un nombre:")
    lugar = input("Escribe un lugar:")
    objeto = input("Escribe un objeto:")
    animal = input("Escribe un animal:")
    verbo = input("Escribe un verbo:")

    seleccion = random.randint(1, 3)
    
    if seleccion == 1:
        print("Un día,", nombre, "fue a", lugar, "con su", objeto + ".")
        print("De repente apareció un", animal, "y empezó a", verbo + ".")
        print("¡Fue una locura!")

    elif seleccion == 2:
        print(nombre, "estaba caminando por", lugar, "cuando encontró un", objeto + ".")
        print("Sin darse cuenta, un", animal, "lo miraba mientras", verbo + ".")
        print("Todo fue muy extraño...")

    elif seleccion == 3:
        print("Había una vez un", animal, "que sabía", verbo + ".")
        print("Un día conoció a", nombre, "en", lugar, "y le regaló un", objeto + ".")
        print("Desde entonces, fueron amigos para siempre.")

agrge historia aleatoria
con input y random
