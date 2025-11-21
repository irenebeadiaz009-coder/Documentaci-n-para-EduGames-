#Este modulo es del juego sumasyrestas
#El codigo se modifico un poco para agregar la funcion def 
#Agregando funciones por si el usuario quiere seguir jugando 

import random

def sumasyrestas(edad):
    """Juego de sumas y restas"""
    print("Bienvenido a sumas y restas 🧠 💪 💫")  
    
    while True:
        puntos=0
        contador=0 
        
        #Nivel para los de 5-7
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
                    seguir=input("Quieres continuar aprendiendo (si/no)?: ").lower()
                    if seguir=="si":
                        pass #continuar, la persona sigue jugando
                    else:
                        print("Gracias por jugar! 😊")
                        break
        
        #Nivel para los de 8-10
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
                    seguir=input("Quieres continuar aprendiendo (si/no)?: ").lower()
                    if seguir=="si":
                        pass #continuar, la persona sigue jugando
                    else:
                        print(f"Gracias por jugar! 😊")
                        break
            
            
        if puntos >=20:
            print(f"FELICIDADES 🎉🥳, obtuviste {puntos} puntos !!!")
        else:
            print(f"Siguelo intentando, obtuviste {puntos} puntos 💫") 
            
        #Si el usuario quiere volver a jugar 
        
        seguir= input("Quieres volver a jugar? (si/no): ").lower()
        if seguir !="si":
            print("Gracias por jugar!! 💖")
            break 


