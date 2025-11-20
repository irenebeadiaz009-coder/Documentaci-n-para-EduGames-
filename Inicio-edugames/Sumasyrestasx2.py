#Sumas y restas, con arreglos 

#El juego fue modificado para que la dificultad sea conforme a la edad del pequeño
#Ahora se tiene un sub-seccion dentro del juego, ya que dentro del rango de 5 a 10 años hay diferentes niveles de conocimiento

print("Bienvenido a sumas y restas 🧠 💪 💫")  
puntos=0
contador=0 


edad=int(input("Ingresa tu edad: ")) 

import random 

if edad >=5 and edad <=7: 
    for i in range(20):
        num1=random.randint(1,10)
        num2=random.randint(1,10)
        if num1<num2:
            num1,num2=num2,num1
        operacion=random.choice(["-", "+"])
        print(f"Cuanto es {num1} {operacion} {num2}?")
        
        if operacion=="+":
            respuesta=num1+num2
        else:
            respuesta=num1-num2
        
        resultado=int(input("Ingresa tu respuesta: ")) 
        contador += 1
        if respuesta==resultado:
            print("Correcto, vas super bien 🥳")
            puntos+=1
        else:
            print(f"Incorrecto,la respesta era {respuesta} 😓") 
        
        if contador == 10:
            if input("Quieres continuar aprendiendo (Si/No)?: ") == "si":
                "io"
            else:
                print(f"Gracias por jugar! 😊")
                break #se le pone esto por si el usuario desea salir del juego, esto sera preguntado hasta la pregunta 10 no se podrá antes 
            
elif edad >=8 and edad <=10: 
    for i in range(20):
        num1=random.randint(1,20)  
        num2=random.randint(1,20) 
        if num1<num2:
            num1,num2=num2,num1
        operacion=random.choice(["-", "+"])
        print(f"Cuanto es {num1} {operacion} {num2}?")
        
        if operacion=="+":
            respuesta=num1+num2
        else:
            respuesta=num1-num2
        
        resultado=int(input("Ingresa tu respuesta: ")) 
        contador += 1
        
        if respuesta==resultado:
            print("Correcto, vas super bien 🥳")
            puntos+=1
        else:
            print(f"Incorrecto,la respuesta era {respuesta} 😓") 
            
        if contador == 10:
            if input("Quieres continuar aprendiendo (Si/No)?: ") == "si":
                "io"
            else:
                print(f"Gracias por jugar! 😊")
                break
            
            
if puntos >=20:
        print(f"FELICIDADES 🎉🥳, obtuviste {puntos} puntos !!!")
else:
        print(f"Siguelo intentando, obtuviste {puntos} puntos 💫") 


        
        
    



