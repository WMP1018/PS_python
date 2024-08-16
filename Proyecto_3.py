"""
Ejercicio proyecto 3: Gestion de inventarios
"""

class Producto: 
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

def mostrar_menu():
    print("\n Sistema de inventarios")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Actualizar cantidad producto")
    print("5. Eliminar producto")
    print("6. Salir")
    
inventario = []
        
while True:
    mostrar_menu()    
    opcion = input("Elige una opcion del menu ")
           
    if opcion == "6":
        print("Ha salido del programa")
        break
    
    if opcion == "1":
        nombre = input("Ingresa el nombre del producto: ")
        try:
            cantidad = int(input("Ingresa la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(nombre, cantidad, precio)
            inventario.append(producto)
            print("Producto agregado exitosamente.")
        except ValueError:
            print("Error: Entrada no valida")
    elif opcion == "2":
        for c in inventario:
            print(f'Nombre: {c.nombre}, Cantidad: {c.cantidad}, Precio: {c.precio}')
    elif opcion == "3":
        nombre = input("Ingrese el nombre del producto que desea buscar: ")
        encontrado = False
        
        for c in inventario:
            if c.nombre == nombre:
                print(f'Nombre: {c.nombre}, Cantidad: {c.cantidad}, Precio: {c.precio}')
                encontrado = True
                break
        if not encontrado:
            print("Producto no encontrado.")
    elif opcion == "4":
        nombre = input("Ingrese el nombre del producto al que desea actualizar la cantidad: ")
        encontrado = False
        
        for c in inventario:
            if c.nombre == nombre:
                print("Información actual del inventario")
                print(f'Nombre: {c.nombre}, Cantidad: {c.cantidad}, Precio: {c.precio}')
                try:
                    c.cantidad = int(input("Ingresa la cantidad del producto: "))
                    print("Información luego de actualizar la cantidad en el inventario")
                    print(f'Nombre: {c.nombre}, Cantidad: {c.cantidad}, Precio: {c.precio}')
                except ValueError:
                    print("Error: Entrada no valida")
                encontrado = True
                break
        if not encontrado:
            print("Producto no encontrado.")
    elif opcion == "5":
        nombre = input("Ingrese el nombre que desea eliminar: ")
        for c in inventario:
            if c.nombre == nombre:
                inventario.remove(c)
                print("Producto eliminado")
                break
    else:
        print("Opcion no valida. Intente nuevamente")