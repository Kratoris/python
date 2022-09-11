from turtle import *

def main():
    setup(700, 400, 0, 0)
    cadena = textinput("nombre", "Cúal es tu nombre")
    cadena = "Hola " + cadena
    write(cadena, False, "center", ("arial", 20, "bold italic"))
    hideturtle()
    mainloop()


if(__name__=="__main__"):
    main()