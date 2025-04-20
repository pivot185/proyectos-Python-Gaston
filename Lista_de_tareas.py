tareas = [
    {"nombre": "Comprar pan", "completada": False},
    {"nombre": "Estudiar Python", "completada": True}
]

while True:
    print ("\nBienvemido a tu lista de tareas")
    print ("1- Agregar tarea")
    print ("2- Ver tareas")
    print ("3- Marcar tarea como completada")
    print ("4- Eliminar tareas completadas")
    print ("5- Salir")
    
    opcion = input ("Elije una opcion: ")

    if opcion == "1":
       tarea = input("Escribe la nueva tarea: ")
       nueva_tarea = {"nombre": tarea, "completada": False}
       tareas.append(nueva_tarea)
       print(f"Tarea agregada: {tarea}")
    elif opcion == "2":
        print("Tus tareas:")
        if not tareas:
            print("No hay tareas pendientes.")
        else:
             for i, tarea in enumerate(tareas, start=1):
                 estado = "✔️" if tarea["completada"] else "✖️"
                 print(f"{i}. {tarea['nombre']} [{estado}]")
        print ("Elejiste ver las tareas")
    elif opcion == "3":
         print("Tareas actuales:")
         for i, tarea in enumerate(tareas, start=1):
              estado = "✔️" if tarea["completada"] else "✖️"
              print(f"{i}. {tarea['nombre']} [{estado}]")

         numero = int(input("Escribí el número de la tarea que completaste: "))
         indice = numero - 1

         if 0 <= indice < len(tareas):
              tareas[indice]["completada"] = True
              print(f"Marcaste '{tareas[indice]['nombre']}' como completada.")
         else:
                print("Número inválido.")
    elif  opcion == "4":
          tareas = [tarea for tarea in tareas if not tarea["completada"]]
          print("Tareas completadas eliminadas.")
    elif opcion == "5":
        print ("Hasta luego")
        break
    else: 
         print ("Opcion Invalida. Intenta de nuevo.")
        
        
    
