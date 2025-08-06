#Generador de numeros aleatorios
import random

arr = list(range(1, 10_000))  # Genera los números del 1 al 10.000
random.shuffle(arr)  # Mezcla aleatoriamente los números

print(arr)  # Muestra la lista desordenada