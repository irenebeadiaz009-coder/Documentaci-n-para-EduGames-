juego_iniciado = True
while juego_iniciado:
    print("¡Bienvenido a EduGames! 💖 🤓 🧠")
    print("Aquí aprenderas mientras te diviertes. 🙌 😉") 
    edad = int(input( "1. Ingrese su edad: "))
    if edad <= 10:
        estacion1 = True
        while estacion1:
            juego_primer_rango = int(input("""Bienvenido a la estación 1 de aprendizaje
                                Juegos disponibles:
                1. Colorimetría.
                2. Sumas y restas.
                3. Salir de la estación.                  
            Ingrese el juego que desea (1 o 2): """))
            if juego_primer_rango == 1:
                print("""
                  ¡Bienvenido al juego de Colorimetría! 🎨
                  """)
                colorimetria = True
                while colorimetria: ##3. Los otros
                    dificultad = int(input("""Este juego tiene dos niveles: 
                                   1. Los colores primarios.
                                   2. Las combinaciones.
                                   3. Salir.
Para comenzar a jugar selecciona un nivel (1 o 2 ): """))
                    if dificultad == 1:
                        print("""
                      Bienvenido a "Los colores primarios". 
                    
¿Sabías que👀:
Los artistas llaman a los colores primarios como “los colores mágicos” 
porque mezclándolos de distintas formas pueden pintar todo el arcoíris. 🌈 
¡Así que, en realidad, el mundo entero está hecho de combinaciones de solo tres colores!

Por eso comencemos a aprender. Primero, lee la siguiente lista de colores:                      """)
                        lista1 = ("""1. Naranja 🟠
2. Azul 🔵
3. Rojo 🔴
4. Blanco ⚪
5. Amarillo 🟡""")
                        lista2 = ("""1. Azul 🔵
2. Rojo 🔴
3. Morado 🟣
4. Amarillo 🟡
5. Negro ⚫""")
                        lista3 = ("""1. Amarillo 🟡
2. Negro ⚫
3. Rojo 🔴
4. Blanco ⚪
5. Azul 🔵""")
                        listas = [lista1, lista2, lista3]
                        import random
                        lista_seleccionada = random.choice(listas)
                        print(lista_seleccionada)
                        pregunta = True
                        while pregunta:
                            respuesta = input("""De la lista anterior, escribe los nombres de los tres colores primarios
(Escribe los tres separados por comas): """).lower()
                            if "azul" in respuesta and "amarillo" in respuesta and "rojo" in respuesta:
                                print("""
                                  ¡Excelete trabajo! Esos son los colores primarios 💙 💛 ❤️ 
                                  """)
                                print("Haz completado exitosamente el nivel 1.")
                                print("Te invitamos a jugar nuestro siguiente nivel.")
                                pregunta = False                          
                            else:
                                print("Vuelve a intentarlo.")
                
                 
                    elif dificultad == 2:
                        print("""
                          Bienvenido a "Las combinaciones" 
                          Dato curioso 👀:
¡Los colores también pueden engañar a tus ojos! 😲 
Si pones un color junto a otro muy diferente, 
tu cerebro puede hacer que parezcan más brillantes o más oscuros de lo que realmente son. 😮✨
Por eso los artistas y diseñadores juegan con las combinaciones: 
¡usan los colores como si fueran magia para hacer que todo se vea más bonito! 🎨🧙

Por esto, comienza a practicar las combinaciones. 😉""")
                        combi = True
                        while combi: # Voy a crear diversas posibilidades de combinaciones.
                        # c = combinaciones
                            c1 = "Rojo 🔴 + Amarillo 🟡"
                            c2 = "Azul 🔵 + Amarillo 🟡"
                            c3 = "Rojo 🔴 + Azul 🔵"
                            c4 = "Blanco ⚪ + Rojo 🔴"
                            c5 = "Negro ⚫ + Blanco ⚪"
                            c6 = "Blanco ⚪ + Azul 🔵"
                            combinaciones = [c1, c2, c3, c4, c5, c6]
                            import random
                            c_seleccionada = random.choice(combinaciones)
                            print("Cuál es el resultado de la combinación de los siguientes colores:")
                            repetidas = []
                            repetidas.append(c_seleccionada)
                            if c_seleccionada is not repetidas:
                                print(c_seleccionada )
                            prueba = True
                            while prueba:
                                if c_seleccionada == c1:
                                    answer = input("Escribe el nombre del nuevo color que se crea al combinar los dos colores anteriores: ").lower()
                                    if answer == "anaranjado":
                                        print("Excelente, lo lograsté.")
                                        siguiente_p1 = int(input("""Ahora que acertaste, tenemos dos opciones para ti:
                                                         1. Probar otra combinación.
                                                         2. Probar otro nivel.
                                                         (Elige (1 o 2): """))
                                        if siguiente_p1 == 1:
                                            prueba = False
                                        elif siguiente_p1 == 2: 
                                            print("""Gracias por jugar "Las combinaciones".""")
                                            prueba = False
                                            combi = False
                                    else:
                                        print("vuelve a intentar")
                                elif c_seleccionada == c2:
                                    a2 = input("Escribe el nombre del nuevo color que se crea al combinar los dos colores anteriores: ").lower()
                                    if a2 == "verde":
                                        print("Excelente, lo lograsté.")
                                        siguiente_p2 = int(input("""Ahora que acertaste, tenemos dos opciones para ti:
                                                         1. Probar otra combinación.
                                                         2. Probar otro nivel
                                                         (Elige (1 o 2): """))
                                        if siguiente_p2 == 1:
                                            prueba = False
                                        elif siguiente_p2 == 2: 
                                            print("""Gracias por jugar "Las combinaciones".""")
                                            prueba = False
                                            combi = False
                                    else: 
                                        print("vuelve a intentar")
                                elif c_seleccionada == c3:
                                    a3 = input("Escribe el nombre del nuevo color que se crea al combinar los dos colores anteriores: ").lower()
                                    resp_3 = ["morado", "violeta"] #Aqui hay dos posibles respuestas.
                                    if a3.lower() in resp_3:
                                        print("Excelente, lo lograsté.")
                                        siguiente_p3 = int(input("""Ahora que acertaste, tenemos dos opciones para ti:
                                                         1. Probar otra combinación.
                                                         2. Probar otro nivel
                                                         (Elige (1 o 2): """))
                                        if siguiente_p3 == 1:
                                            prueba = False
                                        elif siguiente_p3 == 2: 
                                            print("""Gracias por jugar "Las combinaciones".""")
                                            prueba = False
                                            combi = False
                                    else: 
                                        print("vuelve a intentar")
                                elif c_seleccionada == c4:
                                    a4 = input("Escribe el nombre del nuevo color que se crea al combinar los dos colores anteriores: ").lower()
                                    if a4 == "rosado":
                                        print("Excelente, lo lograsté.")
                                        siguiente_p4 = int(input("""Ahora que acertaste, tenemos dos opciones para ti:
                                                         1. Probar otra combinación.
                                                         2. Probar otro nivel
                                                         (Elige (1 o 2): """))
                                        if siguiente_p4 == 1:
                                            prueba = False
                                        elif siguiente_p4 == 2: 
                                            print("""Gracias por jugar "Las combinaciones".""")
                                            prueba = False
                                            combi = False
                                elif c_seleccionada == c5:
                                    a5 = input("Escribe el nombre del nuevo color que se crea al combinar los dos colores anteriores: ").lower()
                                    if a5 == "gris":
                                        print("Excelente, lo lograsté.")
                                        siguiente_p5 = int(input("""Ahora que acertaste, tenemos dos opciones para ti:
                                                         1. Probar otra combinación.
                                                         2. Probar otro nivel
                                                         (Elige (1 o 2): """))
                                        if siguiente_p5 == 1:
                                            prueba = False
                                        elif siguiente_p5 == 2: 
                                            print("""Gracias por jugar "Las combinaciones".""")
                                            prueba = False
                                            combi = False
                                elif c_seleccionada == c6:
                                    a6 = input("Escribe el nombre del nuevo color que se crea al combinar los dos colores anteriores: ").lower()
                                    if a6 == "celeste":
                                        print("Excelente, lo lograsté.")
                                        siguiente_p6 = int(input("""Ahora que acertaste, tenemos dos opciones para ti:
                                                         1. Probar otra combinación.
                                                         2. Probar otro nivel
                                                         (Elige (1 o 2): """))
                                        if siguiente_p6 == 1:
                                            prueba = False
                                        elif siguiente_p6 == 2: 
                                            print("""Gracias por jugar "Las combinaciones".""")
                                            prueba = False
                                            combi = False
                    elif dificultad == 3:
                        colorimetria = False                        
            elif juego_primer_rango == 3:
                estacion1 = False
                                            
    else: 
        juego_iniciado = False