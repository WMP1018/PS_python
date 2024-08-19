"""
Ejercicio proyecto 4: Gestión de tareas
"""

class Tarea:
    def __init__(self, titulo, descripcion, estado = "Pendiente"):
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado

def mostrar_menu():
    print("\nBienvenid@")
    print("Sistema de gestion de tareas\n")
    print("1. Agregar tareas")
    print("2. Mostrar tareas")
    print("3. Buscar tarea")
    print("4. Mostrar tareas por estado")
    print("5. Actualizar estado tarea")
    print("6. Actualizar descripción tarea")
    print("7. Eliminar tarea")
    print("8. Salir")
    
inventarioTareas = []

while True:
    mostrar_menu()
    try:
        opcion = int(input("\nPor favor ingrese el número correspondiente a la opción que desea ejecutar: "))                
        if opcion == 1:
            titulo = input("Ingrese el titulo de la tarea: ")
            descripcion = input("Ingrese la descripción de la tarea: ")
            tarea = Tarea(titulo, descripcion)
            inventarioTareas.append(tarea)
            print("Tarea agregada exitosamente con estado pendiente.")           
        elif opcion == 2:
            for c in inventarioTareas:
                print(f'Título: {c.titulo}, Descripción: {c.descripcion}, Estado: {c.estado}')                
        elif opcion == 3:
            titulo = input("Ingrese el titulo de la tarea que desea buscar: ").lower()
            encontrado = False  
            for c in inventarioTareas:
                if c.titulo.lower() == titulo:
                    print(f'Título: {c.titulo}, Descripción: {c.descripcion}, Estado: {c.estado}')
                    encontrado = True
                    break
            if not encontrado:
                print("Tarea no encontrada.")
        elif opcion == 4:
            estado = input("Por favor ingrese el estado por el que desea filtrar las tareas (Completada ó Pendiente): ").lower()
            if estado.lower() in("completada","pendiente"):
                for c in inventarioTareas:
                    if c.estado.lower() == estado:
                        print(f'Título: {c.titulo}, Descripción: {c.descripcion}, Estado: {c.estado}')
            else:
                print("El estado no corresponde a un estado valido.")
        elif opcion == 5:
            nombre = input("Ingrese el titulo de la tarea a la cual desea cambiar su estado a Completada: ").lower()
            encontrado = False            
            for c in inventarioTareas:
                if c.titulo.lower() == nombre:
                    encontrado = True
                    print(f'Título: {c.titulo}, Descripción: {c.descripcion}')
                    verificacion = input("¿Está seguro de cambiar el estado de la tarea a Completada? (S ó N): ").lower()
                    if verificacion == "s":
                        print("Estado de tarea cambiado.")
                        c.estado = "Completada"
                        break
                    elif verificacion == "n":
                        print("Acción cancelada.")
                        break
                    else:
                        print("Opcion no valida, el caracter ingresado no fue S o N (Si o No). Intente nuevamente")
            if not encontrado:
                print("Tarea no encontrada.")
        elif opcion == 6:
            nombre = input("Ingrese el titulo de la tarea a la cual desea cambiar su descripción: ").lower()
            encontrado = False            
            for c in inventarioTareas:
                if c.titulo.lower() == nombre:
                    encontrado = True
                    print("Información actual de la tarea")
                    print(f'Título: {c.titulo}, Descripción: {c.descripcion}, Estado: {c.estado}')
                    c.descripcion = input("Ingrese la nueva descripcion para la tarea: ")
                    print(f"Descripción actualizada para la tarea: {c.titulo}")
            if not encontrado:
                print("Tarea no encontrada.")
        elif opcion == 7:
            titulo = input("Ingrese el titulo de la tarea que desea eliminar: ").lower()
            for c in inventarioTareas:
                if c.titulo.lower() == titulo:
                    inventarioTareas.remove(c)
                    print("Tarea eliminado")
                    break
        if opcion == 8:
            print("Ha salido del programa")
            break   
    except ValueError:
            print('Entrada inválida. Por favor, ingresa un número.')
        