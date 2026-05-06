
num1 =input("Ingrese el primer número: ")
num2 =input("Ingrese el segundo número: ")

num1 = float(num1)
num2 = float(num2)
salir = True

while(salir):
    print("Seleccione la operación a realizar:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Nuevos valores")
    print("6. Salir")
    operation = input("Ingrese el número de la operación (1/2/3/4): ")

    if operation == '1':
        print(num1 + num2)
    elif operation == '2':
        print(num1 - num2)
    elif operation == '3':
        print(num1 * num2)
    elif operation == '4':
        print(num1 / num2)
    elif operation == '5':
        num1 =input("Ingrese el primer número: ")
        num2 =input("Ingrese el segundo número: ")

        num1 = float(num1)
        num2 = float(num2)
    elif operation == '6':
        salir = False
print("Suerte en su dia Sr.De la Cruz")