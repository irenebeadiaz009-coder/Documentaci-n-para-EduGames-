#EL juego piedra, papel o tigera
#se le puede agregar un sistema de puntos 

import random

def inicio():
    opciones=["piedra","papel","tijera"]
    print("Bienvenido al juego")
    
    while True:
        jugador= input("Elige tu opción piedra, papel o tijera: ") 
        if jugador not in opciones:
            print("Opción no válida intente de nuevo")
            continue
        computadora= random.choice(opciones)
        print(f"La computadora eligió {computadora}")
    
        if jugador==computadora:
            print("¡Empate!")
        elif (jugador=="piedra" and computadora=="tijera") or \
            (jugador=="papel" and computadora=="piedra") or \
                (jugador=="tijera" and computadora=="papel"):
                    print("¡Ganaste!")
        
        else:
            print("Perdiste :(")
            
        continuar=input("¿Quieres seguir jugando?(1= SI, 2=NO ): ")
        if continuar!="1":
            print("Gracias por jugar hasta la próxima")
            break
    
        

        
    