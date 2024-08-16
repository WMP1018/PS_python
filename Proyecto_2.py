"""
Ejercicio proyecto 2: Gestion de contactos
"""

class Contacto: #Definimos las clase y el nombre de la clase
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono                  

def mostrar_menu():
    print("\n Gestion de contactos")
    print("1. Agregar contacto")
    print("2. Mostrar contacto")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")
    
libreta = []

while True:
    mostrar_menu()
    opcion = input("Elige una opcion: ")
    
    if opcion == "5":
        print("Ha salido del programa")
        break
    
    if opcion == "1":
        nombre = input("Ingresa el nombre del contacto: ")
        telefono = input("Ingresa el número de teléfono del contacto: ")
        contacto = Contacto(nombre, telefono)
        libreta.append(contacto)    #Se utiliza para agregar un elementos al final de la lista
        print("Contacto agregado exitosamente")
    elif opcion == "2":
        for c in libreta:
            print(f'Nombre: {c.nombre}, Telefono: {c.telefono}')
    elif opcion == "3":
        nombre = input("Ingrese el nombre que desea buscar: ")
        encontrado = False
        
        for c in libreta:
            if c.nombre == nombre:
                print(f'Nombre: {c.nombre}, Telefono: {c.telefono}')
                encontrado = True
                break
        if not encontrado:
            print("Contacto no encontrado.")            
    elif opcion == "4":
        nombre = input("Ingrese el nombre que desea eliminar: ")
        for c in libreta:
            if c.nombre == nombre:
                libreta.remove(c)
                print("Contacto eliminado")
                break
    else:
        print("Opcion no valida. Intente nuevamente")