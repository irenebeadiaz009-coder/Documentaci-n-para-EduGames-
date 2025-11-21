#Juego de multiplicaciones 

#Este juego esta diseñado para niños de 11 a 17 años, seguirá la misma logica que el de sumas y restas 

#Se sigue decidiendo si poner de 5 a 25

print("Bienvenido a multiplicaciones 🧠 🏋️‍♀️")  
puntos=0
contador=0 


edad=int(input("Ingresa tu edad: ")) 

import random 

if edad>=11 and edad<=13:
    for i in range(20):
        num1=random.randint(2,12) #No se conto el núm 1 porque sería demasiado sencillo, el proposito es tenga cierto grado de dificultad 
        num2=random.randint(2,12)
        
        print(f"Cuanto es {num1} * {num2}?")
        respuesta=num1*num2
        
        resultado=int(input("Ingrese su respuesta? "))
        contador+=1
        
        if respuesta==resultado:
            print("Correcto, vas excelente 🎉")
            puntos+=1
        else:
            print(f"Incorrecto, la respuesta correcta era {respuesta} 🤔") 
        
        if contador == 10:
            if input("Quieres continuar aprendiendo (Si/No)?: ") == "si":
                "io"
            else:
                print(f"Gracias por jugar! 😊")
                break

if edad>=14 and edad <=17:
    for i in range(20):
        num1=random.randint(5,20)
        num2=random.randint(5,20) 
        
        print(f"Cuanto es {num1}*{num2}?")
        respuesta=num1*num2
        
        resultado=int(input("Ingrese su respuesta: "))
        contador+=1
        
        if respuesta==resultado:
            print("Felicidades, sigue asi !! 🎉")
            puntos+=1
        else:
            print(f"Incorrecto, la respuesta era {respuesta} 🤔")
        
        if contador==10:
            if input("Quieres continuar aprendiendo (Si/No)?: ") == "si":
                "io"
            else:
                print(f"Gracias por jugar! 😊")
                break #termina 
                        
if puntos>=20:
    print(f"Excelente !!! alcanzaste el maximo puntaje, {puntos} puntos 🎉🎉")
else:
    print(f"Sigue así, tu puedes !!! alcanzaste {puntos} puntos 💖")