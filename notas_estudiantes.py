estudiantes=[]

usuario = int(input("Cuantos usuarios quiere ingresar:\n"))
for i in range (usuario):
    nombre = input("Ingrese el nombre:\n")
    nota = float(input("Ingrese la nota:\n"))
    estudiante = {"nombre": nombre, "nota": nota}
    estudiantes.append(estudiante)

print("\n------Lista de notas-----")
for est in estudiantes:
    print(f"{est ['nombre']} - Nota: {round(est ['nota'],2)}")
        
