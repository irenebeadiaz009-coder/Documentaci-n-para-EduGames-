def colorimetria_funcion():
    colorimetria = True

    # Bucle del menú de niveles dentro de Colorimetría
    while colorimetria: 
        dificultad = int(input("""Este juego tiene dos niveles: 
                                   1. Los colores primarios.
                                   2. Las combinaciones.
                                   3. Salir.
Para comenzar a jugar selecciona un nivel (1 o 2 ): """))
                    
                    # 
                    # NIVEL 1: COLORES PRIMARIOS
                    # 
        if dificultad == 1:
            print("""  
                              Bienvenido a "Los colores primarios". 
¿Sabías que👀:
Los artistas llaman a los colores primarios como “los colores mágicos” 
porque mezclándolos de distintas formas pueden pintar todo el arcoíris. 🌈 
¡Así que, en realidad, el mundo entero está hecho de combinaciones de solo tres colores!

Por eso comencemos a aprender. Primero, lee la siguiente lista de colores:""")

                        # Tres posibles listas que se muestran aleatoriamente
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

                        # Se guarda en una lista para seleccionar una al azar
            listas = [lista1, lista2, lista3]
            import random
            lista_seleccionada = random.choice(listas)
            print(lista_seleccionada)

                        # Bucle para validar la respuesta
            pregunta = True
            while pregunta:
                respuesta = input("""De la lista anterior, escribe los nombres de los tres colores primarios
(Escribe los tres separados por comas): """).lower()

                            # Validamos que los 3 colores primarios estén en la respuesta
                if "azul" in respuesta and "amarillo" in respuesta and "rojo" in respuesta:
                    print("""
                                  ¡Excelente trabajo! Esos son los colores primarios 💙 💛 ❤️ 
                                  """)
                    print("Haz completado exitosamente el nivel 1.")
                    print("Te invitamos a jugar nuestro siguiente nivel.")
                    pregunta = False    
                else:
                    print("Casi lo logras, buen intento.")
                    print("Vuelve a intentarlo. 💪")
                
                 
                    # 
                    # NIVEL 2: COMBINACIONES
                    
        elif dificultad == 2:
            print("""
                          Bienvenido a "Las combinaciones" 
                          Dato curioso 👀:
¡Los colores también pueden engañar a tus ojos! 😲 
Si pones un color junto a otro muy diferente, 
tu cerebro puede hacer que parezcan más brillantes o más oscuros de lo que realmente son. 😮✨

Por esto, comienza a practicar las combinaciones. 😉""")
                        

                        # Lista de todas las combinaciones posibles
            combinaciones = [
                            "Rojo 🔴 + Amarillo 🟡",
                            "Azul 🔵 + Amarillo 🟡",
                            "Rojo 🔴 + Azul 🔵",
                            "Blanco ⚪ + Rojo 🔴",
                            "Negro ⚫ + Blanco ⚪",
                            "Blanco ⚪ + Azul 🔵"]

                        # Bucle el nivel de combinaciones
            combi = True

            while combi:

                if len(combinaciones) == 0:
                    print("¡Ya respondiste todas las combinaciones disponibles! 🎉")
                    print("Regresando al menú de niveles... 🤓 😉")
                    print("GRACIAS POR JUGAR ESTE NIVEL. 🥹")
                    break

                import random
                c_seleccionada = random.choice(combinaciones)

                print("¿Cuál es el resultado de la combinación de los siguientes colores?")
                print(c_seleccionada)

                prueba = True
                while prueba:

                                
                                # COMBINACIÓN 1
                                # Rojo + Amarillo → Naranja
                                
                                # Se aceptan dos respuestas porque:
                                # - "Naranja" es el nombre del color
                                # - "Anaranjado" es otra forma de decirlo
                                
                    if c_seleccionada == "Rojo 🔴 + Amarillo 🟡":
                        answer = input("Escribe el nombre del nuevo color: ").lower()
                        if answer in ["naranja", "anaranjado"]:
                            print("Excelente, lo lograste. 🥹 🤗")
                            prueba = False
                            combinaciones.remove(c_seleccionada)
                        else:
                            print("Casi lo logras, buen intento.")
                            print("Vuelve a intentarlo. 💪")
                                        
                                # COMBINACIÓN 2: Verde
                    elif c_seleccionada == "Azul 🔵 + Amarillo 🟡":
                        a2 = input("Escribe el nombre del nuevo color: ").lower()
                        if a2 == "verde":
                            print("Excelente, lo lograste. 🥹 🤗")
                            prueba = False
                            combinaciones.remove(c_seleccionada)
                        else:
                            print("Casi lo logras, buen intento.")
                            print("Vuelve a intentarlo. 💪")

                                
                                # COMBINACIÓN 3
                                # Rojo + Azul → Morado o Violeta
                                
                                # Se aceptan dos respuestas porque:
                                # - Mucha gente dice "morado"
                                # - Otros usan "violeta", ambos son correctos
                                # - O purpura
                                
                    elif c_seleccionada == "Rojo 🔴 + Azul 🔵":
                        a3 = input("Escribe el nombre del nuevo color: ").lower()
                        if a3 in ["morado", "violeta", "púrpura"]:
                            print("Excelente, lo lograste. 🥹 🤗")
                            prueba = False
                            combinaciones.remove(c_seleccionada)
                        else:
                            print("Casi lo logras, buen intento.")
                            print("Vuelve a intentarlo. 💪")

                                
                                # COMBINACIÓN 4
                                # Blanco + Rojo → Rosado o Rosa
                                
                                # Se aceptan dos respuestas porque:
                                # - "Rosado" es el nombre técnico
                                # - "Rosa" es común 
                                
                    elif c_seleccionada == "Blanco ⚪ + Rojo 🔴":
                        a4 = input("Escribe el nombre del nuevo color: ").lower()
                        if a4 in ["rosado", "rosa"]:
                            print("Excelente, lo lograste. 🥹 🤗")
                            prueba = False
                            combinaciones.remove(c_seleccionada)
                        else:
                            print("Casi lo logras, buen intento.")
                            print("Vuelve a intentarlo. 💪")

                                # COMBINACIÓN 5: Gris
                    elif c_seleccionada == "Negro ⚫ + Blanco ⚪":
                        a5 = input("Escribe el nombre del nuevo color: ").lower()
                        if a5 == "gris":
                            print("Excelente, lo lograste. 🥹 🤗")
                            prueba = False
                            combinaciones.remove(c_seleccionada)
                        else:
                            print("Casi lo logras, buen intento.")
                            print("Vuelve a intentarlo. 💪")

                                # COMBINACIÓN 6: Celeste
                    elif c_seleccionada == "Blanco ⚪ + Azul 🔵":
                        a6 = input("Escribe el nombre del nuevo color: ").lower()
                        if a6 == "celeste":
                            print("Excelente, lo lograste. 🥹 🤗")
                            prueba = False
                            combinaciones.remove(c_seleccionada)
                        else:
                            print("Casi lo logras.")
                            print("Vuelve a intentarlo. 💪")

                            # Después de acertar se pregunta qué hacer
                siguiente = int(input("""
Ahora que acertaste, tenemos dos opciones para ti:
1. Probar otra combinación.
2. Probar otro nivel.
(Elige 1 o 2): """))

                if siguiente == 2:
                    print("""Gracias por jugar "Las combinaciones". Volviendo al menú...""")
                    combi = False
                                
        elif dificultad == 3:
            colorimetria = False    
                          

