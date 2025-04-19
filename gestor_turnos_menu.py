import json


try:
    with open("turnos.json", "r") as archivo:
        turnos_reservados = json.load(archivo)
except FileNotFoundError:
    turnos_reservados = {}


horarios_disponibles = ["09:00", "10:00", "11:00", "12:00", "13:00"]


while True:
    print("\nBienvenido al sistema de turnos")
    print("1 - Reservar un turno")
    print("2 - Ver turnos reservados")
    print("3 - Cancelar un turno")
    print("4 - Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        print("\nHorarios disponibles:")
        for horario in horarios_disponibles:
            if horario not in turnos_reservados:
                print(horario)

        nombre = input("Ingrese su nombre: ")
        turno = input("Elija un horario: ")

        if turno in horarios_disponibles and turno not in turnos_reservados:
            turnos_reservados[turno] = nombre
            print(f"Turno reservado para {nombre} a las {turno}")

            with open("turnos.json", "w") as archivo:
                json.dump(turnos_reservados, archivo, indent=4)
        else:
            print("Ese horario no está disponible.")

    elif opcion == "2":
        if turnos_reservados:
            print("\nTurnos reservados:")
            for horario, nombre in turnos_reservados.items():
                print(f"{horario} - {nombre}")
        else:
            print("Todavía no hay turnos reservados.")

    elif opcion == "3":
        turno_a_cancelar = input("Ingrese el horario que desea cancelar: ")
        if turno_a_cancelar in turnos_reservados:
            del turnos_reservados[turno_a_cancelar]
            with open("turnos.json", "w") as archivo:
                json.dump(turnos_reservados, archivo, indent=4)
            print("Turno cancelado exitosamente.")
        else:
            print("Ese turno no está reservado.")

    elif opcion == "4":
        print("¡Hasta luego!")
        break

    else:
        print("Opción inválida. Intentá de nuevo.")
