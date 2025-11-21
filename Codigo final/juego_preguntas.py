import random

# Lista de preguntas con respuesta y pistas

preguntas = [
    {
        "pregunta": "¿Cuál es el país más grande del mundo?",
        "respuesta": "rusia",
        "pistas": ["Está en Europa y Asia", "Es famoso por el Kremlin"]
    },
    {
        "pregunta": "¿Cuál es el océano más profundo?",
        "respuesta": "pacifico",
        "pistas": ["Está entre Asia y América", "Su fosa más profunda es la Fosa de las Marianas"]
    },
    {
        "pregunta": "¿Quién escribió 'Don Quijote de la Mancha'?",
        "respuesta": "miguel de cervantes",
        "pistas": ["Es un autor español", "Vivió en el Siglo de Oro"]
    },
    {
        "pregunta": "¿Cuál es el planeta más grande del sistema solar?",
        "respuesta": "jupiter",
        "pistas": ["Es un gigante gaseoso", "Tiene una gran mancha roja"]
    },
    {
        "pregunta": "¿En qué continente se encuentra Egipto?",
        "respuesta": "africa",
        "pistas": ["Está al norte", "Es atravesado por el río Nilo"]
    },
    {
        "pregunta": "¿Cuál es el metal más ligero?",
        "respuesta": "litio",
        "pistas": ["Está en las baterías", "Es un metal alcalino"]
    },
    {
        "pregunta": "¿En qué país se originaron los Juegos Olímpicos?",
        "respuesta": "grecia",
        "pistas": ["Está en Europa", "Cuna de la filosofía occidental"]
    },
    {
        "pregunta": "¿Cuál es el río más largo del mundo?",
        "respuesta": "nilo",
        "pistas": ["Está en África", "Pasa por Egipto"]
    },
    {
        "pregunta": "¿Qué idioma tiene más hablantes nativos?",
        "respuesta": "mandarin",
        "pistas": ["Se habla en Asia", "Es el idioma principal de China"]
    },
    {
        "pregunta": "¿Qué científico propuso la teoría de la relatividad?",
        "respuesta": "albert einstein",
        "pistas": ["Nació en Alemania", "Ecuación famosa: E=mc^2"]
    },
    {
        "pregunta": "¿Cuál es la capital de Francia?",
        "respuesta": "paris",
        "pistas": ["Tiene una torre famosa", "Ciudad del amor"]
    },
    {
        "pregunta": "¿Cuántos continentes hay en el mundo?",
        "respuesta": "7",
        "pistas": ["Son más de cinco", "Incluyen Asia y África"]
    },
    {
        "pregunta": "¿Quién pintó la Mona Lisa?",
        "respuesta": "leonardo da vinci",
        "pistas": ["Fue inventor y artista italiano", "Vivió en el Renacimiento"]
    },
    {
        "pregunta": "¿Cuál es el animal terrestre más rápido?",
        "respuesta": "guepardo",
        "pistas": ["Vive en África", "Corre más de 100 km/h"]
    },
    {
        "pregunta": "¿Qué gas necesitan las plantas para hacer fotosíntesis?",
        "respuesta": "dioxido de carbono",
        "pistas": ["Es un gas", "Los humanos lo exhalan"]
    },
    {
        "pregunta": "¿Cuál es el país con más población en el mundo?",
        "respuesta": "china",
        "pistas": ["Está en Asia", "Su idioma principal es el mandarín"]
    },
    {
        "pregunta": "¿Qué país ganó la Copa Mundial de FIFA 2010?",
        "respuesta": "españa",
        "pistas": ["Equipo europeo", "Su camiseta principal es roja"]
    },
    {
        "pregunta": "¿Cuál es el órgano que bombea sangre en el cuerpo humano?",
        "respuesta": "corazon",
        "pistas": ["Es vital", "Late sin parar"]
    },
    {
        "pregunta": "¿Qué instrumento mide la temperatura?",
        "respuesta": "termometro",
        "pistas": ["Se usa en medicina", "Tiene grados"]
    },
    {
        "pregunta": "¿En qué país se encuentra la torre inclinada de Pisa?",
        "respuesta": "italia",
        "pistas": ["Está en Europa", "Famoso por la pasta"]
    }
]
#print()

#print("Bienvenido al juego de preguntas de cultura general! 🧐")
def jugar():
    puntaje = 0
    continuar = True

    while continuar:
        print("-")
        print("-")
        print("-")
        pregunta = random.choice(preguntas)
        print(f"Pregunta: {pregunta["pregunta"]} 🤔")
        

        intentos = 0
        correcta = pregunta["respuesta"].lower()

        while intentos < 3:  # 1 intento inicial + 2 pistas
            respuesta = input("Tu respuesta: ").lower()
            print()

            if respuesta == "salir":
                continuar = False
                break

            if respuesta == correcta:
                print("Excelente! Sabes mucho 😎")
                print()
                puntaje += 1
                break
            else:
                if intentos < 2:
                    print("Pista 🥶:", pregunta["pistas"][intentos])
                    
                else:
                    print("Lo siento, las pistas e intentos para responder esta pregunta se acabaron 🤕.")
                    print(f"La respuesta correcta era: {correcta} 👀")
                    print()
                intentos += 1

        if not continuar:
            break
        
        
        if puntaje > 7:
            salir = input("¿Deseas continuar jugando? (si/no): ").lower()
            if salir != "si":
                continuar = False

    print("\nTu puntaje total fue:", puntaje)
    print("Muchas gracias por haber jugado. Te esperamos pronto 📖.")


