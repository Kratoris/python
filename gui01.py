from turtle import *

def main():
    setup(640, 480, 0, 0)
    title("Mi primer ventana")
    hideturtle()
    dot(10, 0, 0, 0)
    #el segundo setup limita el tamaño de la ventana creada en el primer setup, lo cual
    #tambien se puede hacer con screensize()
    setup(450, 150, 0, 0)
    done()
    return 0


if(__name__=="__main__"):
    main()