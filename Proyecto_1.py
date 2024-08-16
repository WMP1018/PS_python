"""
Ejercicio proyecto 1: Calculadora
"""
# Definimos las funciones para cada operación
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

# Función principal de la calculadora
def calculadora():
    while True:
        # Mostramos el menú de opciones
        print("\n Calculadora Básica")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
        
        # Solicitamos al usuario que elija una operación
        opcion = input("Elige una operación (1/2/3/4/5): ")
        
        # Verificamos si el usuario quiere salir
        if opcion == '5':
            print("Gracias por usar la calculadora. ¡Hasta luego!")
            break
        
        # Verificamos si la opción es válida
        if opcion not in ['1', '2', '3', '4']:
            print("Opción no válida. Por favor, intenta de nuevo.")
            continue
        
        # Pedimos los dos números para realizar la operación
        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
        except ValueError:
            print("Error: Por favor, ingresa números válidos.")
            continue
        
        # Realizamos la operación según la opción elegida
        if opcion == '1':
            print("Resultado:", suma(num1, num2))
        elif opcion == '2':
            print("Resultado:", resta(num1, num2))
        elif opcion == '3':
            print("Resultado:", multiplicacion(num1, num2))
        elif opcion == '4':
            print("Resultado:", division(num1, num2))

# Iniciamos la calculadora
calculadora()