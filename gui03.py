from random import randint
from turtle import *

def main():
    setup(700, 400, 0, 0)
    penup()
    hideturtle()
    def punto(x, y):
        global randint
        print(randint)
        goto(randint(-225, 225), randint(-100, 100))
        dot(10, "black")
        ontimer(punto, 1000)
    
    def cuadro(x, y):
        goto(x - 5, y - 5)
        pendown()
        goto(x + 5, y - 5)
        goto(x + 5, y + 5)
        goto(x - 5, y + 5)
        goto(x - 5, y - 5)
        penup()

    onscreenclick(punto, 1)
    onscreenclick(cuadro, 3)
    ontimer(punto, 1000)
    done()


if(__name__=="__main__"):
    main()