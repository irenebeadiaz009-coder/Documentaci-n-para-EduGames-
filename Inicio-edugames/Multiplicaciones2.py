#Juego de multiplicaciones 

#Le hare una modificacion para que no vaya por diferentes rangos de edades sino que por nivel de dificultad 

import random #traemos datos aleatorios (se importan)

print("Bienvenido a multiplicaciones 🧠 🏋️‍♀️")
puntos=0
contador=0 

dificultad=int(input("""Que quieres jugar?
                     1. Nivel basico: repasemos las tablas de multiplicacion 🧠
                     2. Nivel avanzado: veamos que tanto sabes 💪 🤓: """)) 

if dificultad==1:
    for i in range(15): #se cambio a 15 preguntas para no hacer demasiadas multiplicaciones
        num1=random.randint(2,12) #se elijen numeros al azar de 2 a 12 
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

if puntos>=15:
    print(f"Excelente !!! alcanzaste el maximo puntaje, {puntos} puntos 🎉🎉")
else:
    print(f"Sigue así, tu puedes !!! alcanzaste {puntos} puntos 💖")
    
#Seguir jugando, ya sea el mismo nivel o el siguiente
while True:
    seguir=int(input("""Quieres volver a jugar?
                 1. Nivel basico: repasemos las tablas de multiplicacion 🧠
                 2. Nivel avanzado: veamos que tanto sabes 💪 🤓 
                 3. Salir: """))
    if seguir==1:
        dificultad=1
        break
    elif seguir==2:
        dificultad=2
        break
    elif seguir==3:
        print("Gracias por jugar!! 💖")
        exit() #se sale por completo
    else:
        print("La opcion no es valida, elige otra vez!!")
    