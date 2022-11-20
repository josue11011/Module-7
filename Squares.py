# Program Name: Squares
# Name: Josue Cifuentes
# Date: November 12, 2022
# Purpose of a Program: To create squares
import turtle
def drawSquare(t,sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)

#Use modular design
def main():
    wn = turtle.Screen()
    alex = turtle.Turtle()
    alex.color("blue")
    #t = alex
    sz = 20
    for i in range(5):
        alex.pensize(3)
        drawSquare(alex,sz)
        sz = sz + 20
        alex.penup()
        alex.goto(alex.pos() + (-10, -10))
        alex.pendown()
    
    wn.mainloop()
    wn.exitonclick()
main()
