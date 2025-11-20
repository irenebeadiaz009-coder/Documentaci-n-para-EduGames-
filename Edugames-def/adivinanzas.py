aciertos = 0 #contador de los aciertos en las adivinanzas 
"""def usuarioinfo():
    nombre = input("Escriba su nombre: ")
    print(f"Bienvenido usuario {nombre.capitalize()} al juego de las adivinanzas, comenzemos!!!")
usuarioinfo()"""  
#una funcion por cada adivinanza
def adivinanza1():
    global aciertos
    print("1. Es un número impar, pero cuando se pone boca abajo se convierte en par.(escriba el digito ej: 1,2...)")
    respuesta = int(input("Escriba su respuesta de un digito: "))
    if respuesta == 9:
        print("Correcto!")
        aciertos += 1 #sumatoria de los aciertos
    else:
        print("Incorrecto, la respuesta correcta es: 9")
#adivinanza1()

def adivinanza2():
    global aciertos
    print("2. Corren más que los minutos, pero nunca llegan los primeros. ¿Quiénes son? ")
    respuesta = input("Escriba su respuesta de una sola palabra: ")
    if respuesta.lower() == "segundos":
        print("Correcto!")
        aciertos += 1
    else:
        print("Incorrecto, la respuesta correcta es: Segundos")
#adivinanza2()

def adivinanza3():
    global aciertos
    print("3. Hay un número que muy valiente se cree, pero cuando le quitas el cinturón, todo su valor pierde. ¿Quién es?")
    respuesta = int(input("Escriba su respuesta de un digito: "))
    if respuesta == 8:
        print("Correcto!")
        aciertos += 1
    else:
        print("Incorrecto, la respuesta correcta es: 8")
#adivinanza3()

def adivinanza4():
    global aciertos
    print("4.Soy un número de 3 cifras, la suma de estas es 18. La primera cifra es la mitad de la segunda y un tercio de la tercera. ¿Qué número soy?")
    respuesta = int(input("Escriba su respuesta de 3 digitos: "))
    if respuesta == 369:
        print("Correcto!")
        aciertos += 1
    else:
        print("Incorrecto, la respuesta correcta es: 369")
#adivinanza4()

def adivinanza5():
    global aciertos
    print("5.Número de 3 dígitos. El dígito que está en el medio es 4 veces mayor que el tercer y último dígito. Además, el primero es 3 unidades más pequeño que el segundo. ¿Qué número es?")
    respuesta = int(input("Escriba su respuesta de 3 digitos: "))
    if respuesta == 141:
        print("Correcto!")
        aciertos += 1
    else:
        print("Incorrecto, la respuesta correcta es: 141")
#adivinanza5()
#opcion a mitad de esta parte del juego por si el usuario desea terminar la partida o continuarla
def salirdeljuego():
    global aciertos
    opcion = input("¿Quieres seguir jugando? si/no:")
    if opcion.lower() == "no":
        print(f"Gracias por jugar, obtuviste {aciertos} de 5 adivinanzas acertadas.")

#salirdeljuego()
    

def adivinanza6():
    global aciertos
    print("6.¿Qué número es el único que si lo pones al revés es el mismo?")
    respuesta = int(input("Escriba su respuesta de 1 digito: "))
    if respuesta == 8:
        print("Correcto!")
        aciertos += 1
    else:
        print("Incorrecto, la respuesta correcta es: 8")
#adivinanza6()

def adivinanza7():
    global aciertos
    print("7.Tengo más de 3 lados y menos de 5. Tengo todos mis lados iguales. ¿Quién soy?")
    respuesta = input("Escriba su respuesta de 1 palabra: ")
    if respuesta.lower() == "cuadrado":
        print("Correcto!")
        aciertos += 1
    else:
        print("Incorrecto, la respuesta correcta es: cuadrado")
#adivinanza7()

def adivinanza8():
    global aciertos
    print("8.¿Cuál es el número que no tiene cuenta?")
    respuesta = int(input("Escriba su respuesta de 2 digitos: "))
    if respuesta == 50:
        print("Correcto!")
        aciertos += 1
    else:
        print("Incorrecto, la respuesta correcta es: 50")
#adivinanza8()

def adivinanza9():
    global aciertos
    print("9.¿Cuál es el número que al quitarle el 1 ya no vale nada?")
    respuesta = int(input("Escriba su respuesta de 2 digitos: "))
    if respuesta == 10:
        print("Correcto!")
        aciertos += 1
    else:
        print("Incorrecto, la respuesta correcta es: 10")
#adivinanza9()

def adivinanza10():
    global aciertos
    print("10.Blanca por dentro, verde por fuera; si quieres que te lo diga, espera.")
    respuesta = input("Escriba su respuesta de 2 digitos: ")
    if respuesta.lower() == "pera":
        print("Correcto!")
        aciertos += 1
    else:
        print("Incorrecto, la respuesta correcta es: pera")
#adivinanza10()
#final del juego junto con la suma total de aciertos que obtuvo 
def finaljuego():
    print ("Fin del juego, gracias por jugar!")
    print (f"Obtuviste {aciertos} de 10 adivinanzas acertadas.")
#finaljuego()
