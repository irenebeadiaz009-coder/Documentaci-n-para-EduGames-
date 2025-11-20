#Este modulo sera para el juego de multiplicaciones 
#Los cambios que se le haran es para agregar la funcion def para asi importarlo al menu 

import random 

def multiplicaciones():
    """Este es el juego de multiplicaciones"""
    print("Bienvenido a multiplicaciones 🧠 🏋️‍♀️")  

    while True:
        puntos=0
        contador=0 
        
        dificultad=int(input(
            """Que quieres jugar?
1. Nivel basico: repasemos las tablas de multiplicacion 🧠
2. Nivel avanzado: veamos que tanto sabes 💪 🤓: """)) 
        
        #Nivel basico 
        if dificultad==1:
            for i in range(15): 
                num1=random.randint(2,12)
                num2=random.randint(2,12) 
                
                print(f"Cuanto es {num1}*{num2}?")
                respuesta=num1*num2
        
                resultado=int(input("Ingrese su respuesta: "))
                contador+=1
                if respuesta==resultado:
                    print("Correcto, vas excelente 🎉")
                    puntos+=1
                else:
                    print(f"Incorrecto, la respuesta correcta era {respuesta} 🤔") 
                    
                if contador==7:
                    eleccion=input("Quieres seguir jugando (si/no)? ").lower()
                    if eleccion=="si":
                        pass #el usuario seguira con las demas preguntas
                    else:
                        print("Gracias por jugar!! 🤗")
                        break
        
        #Nivel avanzado 
        elif dificultad==2:
            for i in range(15):
                num1=random.randint(2,20)
                num2=random.randint(2,20)
                
                print(f"Cuanto es {num1}*{num2}?")
                respuesta=num1*num2
        
                resultado=int(input("Ingrese su respuesta: "))
                contador+=1
            
                if respuesta==resultado:
                    print("Correcto, vas excelente 🎉")
                    puntos+=1
                else:
                    print(f"Incorrecto, la respuesta correcta era {respuesta} 🤔") 
        
                if contador==7:
                    eleccion=input("Quieres seguir jugando (si/no)? ").lower()
                    if eleccion=="si":
                        pass #el usuario seguira con las demas preguntas
                    else:
                        print("Gracias por jugar!! 🤗")
                        break
        else:
            print("La opcion no es valida 🤔")
            continue #asi va a volver al menu y muestra los puntos
            
        if puntos>=15:
            print(f"Excelente !!! alcanzaste el maximo puntaje, {puntos} puntos 🎉🎉")
        else:
            print(f"Sigue así, tu puedes !!! alcanzaste {puntos} puntos 💖")
    
        #Seguir jugando, ya sea el mismo nivel o el siguiente
        while True:
            seguir=int(input(
                """Quieres volver a jugar?
1. Nivel basico: repasemos las tablas de multiplicacion 🧠
2. Nivel avanzado: veamos que tanto sabes 💪 🤓 
3. Salir: """))
            if seguir==1:
                dificultad==1
                break
            elif seguir==2:
                dificultad==2
                break
            elif seguir==3:
                print("Gracias por jugar!! 💖")
                exit() #se sale por completo
            else:
                print("La opcion no es valida, elige otra vez!!")
                
#multiplicaciones() 
        