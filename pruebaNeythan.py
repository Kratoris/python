from turtle import *

def main():
    setup(1366, 720, 0, 0)
    title("Ventana ejemplativa")
    nombre = textinput("Nombre", "¿Cuál es su nombre?")
    edad = numinput("Edad", "¿Cuál es su edad?", 1, 0, 120)
    write(edad, True , "right")
    write (nombre, True, "left")
    done()
    return 0


if(__name__=="__main__"):
    main()
# import insert_text : hi world 