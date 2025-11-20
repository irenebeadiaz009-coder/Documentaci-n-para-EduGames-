from colorimetria import colorimetria_funcion

# Bucle principal del juego, se repetirá mientras el usuario no decida salir
juego_iniciado = True
while juego_iniciado:
    print("¡Bienvenido a EduGames! 💖 🤓 🧠")
    print("Aquí aprenderás mientras te diviertes. 🙌 😉") 

    # Pedimos la edad para ubicar la estación que mide la dificultad de los juegos
    edad = int(input("1. Ingrese su edad: "))

    # Estación 1: pensada para niños de 10 años o menos
    if edad <= 10:
        colorimetria_funcion() 
        
        
        
        
        
        
