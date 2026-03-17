import turtle

turtle.speed(100)
turtle.hideturtle()
turtle.pensize(2)
turtle.penup()
turtle.goto(0, 0)
turtle.left(90)

square_length = 5

for x in range(100):
    turtle.pendown()
    turtle.forward(square_length)
    turtle.left(90)
    turtle.forward(square_length)
    turtle.left(90)
    turtle.forward(square_length)
    turtle.left(90)
    turtle.forward(square_length)
    turtle.left(90)
    square_length = square_length + 5
    turtle.penup()
    turtle.goto(0, 0)