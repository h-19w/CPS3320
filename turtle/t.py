import turtle

turtle.pensize(5)
turtle.speed(30)
turtle.penup() 
turtle.goto(0, -300)
turtle.pendown()
turtle.pencolor("red") # change pen color to red 
turtle.circle(30)
turtle.right(90)
turtle.pencolor("green") # change pen color to green
turtle.circle(30)
turtle.right(90)
turtle.pencolor("blue") # change pen color to blue
turtle.circle(30)
turtle.right(90)
turtle.pencolor("yellow") # change pen color to orange
turtle.circle(30)
turtle.penup()

t = turtle.Turtle()

t.goto(0, 100)
t.goto(-100, 0)
t.goto(0, 0)
t.goto(100, 0)
t.goto(0, -100)
t.goto(0, 0)



turtle.done()