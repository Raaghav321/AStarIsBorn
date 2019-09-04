import turtle

turtle.speed(90)

turtle.bgcolor("lightblue")

def star(sidelength):
    for i in range(5):
        turtle.forward(sidelength)
        turtle.right(144)



def starSpiral():
    for i in range(60):
        star(i*5)
        turtle.right(5)

starSpiral()

turtle.penup()
turtle.goto(100,-200)
turtle.pendown()

starSpiral()

turtle.penup()
turtle.goto(-200,-200)
turtle.pendown()

starSpiral()

turtle.exitonclick()