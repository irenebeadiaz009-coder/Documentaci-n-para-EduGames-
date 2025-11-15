#Juego basico: sumas y resta 

#Cambios que se deben realizar: 
#no pueden haber respuestas negativas porque es un juego básico para chiquitos
# crear un bucle interno para la dificultad de edad
#Hacerlo más llamativo a la vista con emojis 

print("Bienvenido a sumas y restas")  
puntos=0

import random #la funcion import random es para traer algo random y no tenga que establecer en si las diferentes variables 

for i in range(20): #aquí esta diciendo que serán 20 preguntas, establece un rango de preguntas 
    num1= random.randint(1,20) # la función random.randint sirve para traer un numero random en este caso del 1 al 20
    num2= random.randint(1,20)
    if num1<num2: 
        num1, num2 = num2, num1 #de esta forma num1 siempre sera el mayor y no habrán respuestas negativas, ya que los niños de 5 a 10 no llegan a ese nivel 
    operacion= random.choice (["-", "+"])
    print(f"Cuanto es {num1} {operacion} {num2}?")
    if operacion== "+":
        respuesta= num1+num2
    else:
        respuesta= num1-num2 
        
    resultado=int(input("Ingresa su respuesta: ")) 
    
    if respuesta==resultado:
        print("Correcto")
        puntos+=1
    else:
        print(f"Incorrecto, la respuesta era {respuesta}")

#se pone aquí para que  el puntaje aparezca hasta el final    
if puntos >=20:
        print(f"FELICIDADES!!, obtuviste {puntos} puntos !!!")
else:
        print(f"Siguelo intentando, obtuviste {puntos} puntos") 
        


