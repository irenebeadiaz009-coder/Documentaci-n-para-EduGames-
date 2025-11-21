#EL juego piedra, papel o tigera
#se le puede agregar un sistema de puntos 

import random
opciones=["piedra","papel","tijera"]
print("Bienvenido al juego")

while True:
    jugador= input("Elige tu opción piedra, papel o tijera: ")
    if jugador not in opciones:
        print("Opción no válida intente de nuevo")
        continue
    computadora= random.choice(opciones) #Se usa para que la computadora elija una opcion de manera aleatoria 
    print(f"La computadora eligió {computadora}")
    
    if jugador==computadora: # Se utilizan condicionales para definir el impate victoria y derrota
        print("¡Empate!")
    elif (jugador=="piedra" and computadora=="tijera") or \
        (jugador=="papel" and computadora=="piedra") or \
        (jugador=="tijera" and computadora=="papel"):
        print("¡Ganaste!")
        
    else:
        print("Perdiste :(")
        
    continuar=input("¿Quieres seguir jugando?(1= SI, 2=NO ): ") #Se le pregunta al usuario si desea seguir jugando otra partida 
    if continuar!="1": #si la respuesta no es 1 el juego va a cerrar 
        print("Gracias por jugar hasta la próxima")
        break #El juego cierra, se acaba 
        


        
    