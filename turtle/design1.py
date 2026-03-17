
import turtle

start_x = -200
start_y = 0
num_line = 36
line_length = 400
angle = 170

turtle.speed(90)
turtle.penup()
turtle.goto(start_x, start_y)
turtle.pendown()

for x in range (num_line):

    turtle.forward(line_length)
    turtle.left(angle)

turtle.done()