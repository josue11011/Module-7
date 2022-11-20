# Program Name: Flowers
# Name: Josue Cifuentes
# Date: November 12, 2022
# Purpose of a Program: To create a flower
import turtle
def drawSquare(t,sz): #change name as either polygon or hexagon
    for i in range(6):
        t.forward(90)
        #t.left(300)
        t.left(60)
        


wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("pink")

#t = alex
sz = 20
for i in range(10):
   drawSquare(alex, sz)
   alex.right(36)

   #alex._rotate(45)
   #alex.pensize(3)
   #drawSquare(alex,sz)
   #sz = sz + 20
   #alex.penup()
   #alex.goto(alex.pos() + (-10, -10))
   #alex.pendown()
wn.mainloop()
wn.exitonclick()
