#Ingresar 5 numeros y posteriormente ingresar si desea sumarlos o restarlos entre si.

#Ingresar los 5 números por separado
n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))
n3 = float(input("Ingrese el tercer número: "))
n4 = float(input("Ingrese el cuarto número: "))
n5 = float(input("Ingrese el quinto número: "))

#Elegir la operación
operacion = input("Ingrese 'S' para sumar o 'R' para restar: ").upper()

#Ejecutar operación
if operacion == 'S':
    resultado = n1 + n2 + n3 + n4 + n5
    print("El resultado de la suma es:", resultado)
elif operacion == 'R':
    resultado = n1 - n2 - n3 - n4 - n5
    print("El resultado de la resta es:", resultado)
else:
    print("Opción inválida. Debe ingresar 'S' o 'R'.")