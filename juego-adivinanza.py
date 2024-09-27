

import random


numero_secreto = random.randint(1,100) 
cant_intentos = 0
cant_max_intentos = 5
adivinado = False

print("Bienvenido al jeugo de adivinar el numero secreto!")

while not adivinado:
    if not cant_intentos < cant_max_intentos:
        print("game over, no has podido adivinar el numero dentro de los 5 intentos")
        break
    
    entrada = input("introduce un numero del 1 al 99: ") 
    numero = int(entrada) 

    if numero == numero_secreto: 
        print("felicidades has adivinado el numero secreto")
        adivinado = True 
    elif numero < numero_secreto: 
        print("el numero es mayor al ingresado")
    else: 
        print("el numero es menor al ingresado")
    
    cant_intentos += 1 

