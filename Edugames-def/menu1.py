#Este modulo será el menu 

from colorimetria import colorimetria_funcion
from sumasyrestas import sumasyrestas
#from piedrapapelotijera import 
from multiplicaciones import multiplicaciones
#from preguntasdeculturageneral import 
#from adivinanzas import 

def menu():
    while True: 
        print("¡Bienvenido a EduGames! 💖 🤓 🧠") 
        print("Aquí aprenderas mientras te diviertes. 🙌 😉") 
        
        nombre=input("Dinos como te llamas 😊: ")
        print(f"Hola {nombre}, listo/a para divertirte y aprender!! 💖🎉")

        edad=int(input("Cuantos años tienes? 🤓: "))
        
#La primera opción 
        if edad >=5 and edad <=10:
            print("Bienvenido al nivel basico 🐣 💫")
            opcion=(int(input(
                """Juegos disponibles:
1. Colometría: aprenderas los colores y sus combinaciones 🎨 💖
2. Sumas y restas: aprende lo basico de las matematicas 🧠 💪
3. Salir: """))) 
        
        #Aqui se pondrán los juegos que van en este apartado
            if opcion==1:
                colorimetria_funcion() #conectamos el juego 
            elif opcion==2:
                sumasyrestas(edad) #conectamos el juego
            elif opcion==3:
                print("Regresemos al menu... 🤗")
                break
            else:
                print("La opcion no es valida")

#Nivel intermedio 

        elif edad >=11 and edad <=17:
            print("Bienvenido al nivel intermedio 🐤 💫")
            opcion=(int(input(
                """Juegos disponibles:
1. Piedra, papel o tijera: a ver quien es el mejor 📄 🪨 ✂️
2. Multiplicaciones: veamo que puedes hacer 🧠 🏋️‍♀️
3. Salir: """))) 

        #Aqui se pondrán los juegos que van en este apartado
        
            if opcion==1:
                "Piedra,papel,tijera"
            elif opcion==2: 
                multiplicaciones() #conectamos el juego 
            elif opcion==3:
                print("Regresemos al menu... 🤗")
                break
            else:
                print("La opcion no es valida")
#Nivel avanzado 
                
        elif edad >=18: 
            print("Bienvenido al nivel avanzado 🐥 💫")
            print(int(input(
                """Juegos disponibles:
1. Preguntas de cultura general: probemos tu conocimiento 🤓 🧠
2. Adivinanzas: ejercita tu mente 💭 🤔
3. Salir: """)))
        
        #Aqui se pondrán los juegos que van en este apartado
        


        else:
            print("Lo sentimos, Edugames es para mayores de 5 años 😭") 
            break 

menu()