import turtle

t = turtle.Turtle()
t.speed(100)
t.hideturtle()
t.pensize(5)

t.penup(); t.goto(0, -30); t.pendown(); t.circle(30)

t.penup(); t.goto(0, 0); t.pendown(); t.goto(0, 160)
t.penup(); t.goto(0, 0); t.pendown(); t.goto(0, -160)
t.penup(); t.goto(-160, 0); t.pendown(); t.goto(160, 0)
t.penup(); t.goto(0, -160); t.pendown(); t.goto(0, -160)

t.penup(); t.goto(-25, 170); t.write("North", font=("Arial Bold", 14, "normal"))
t.penup(); t.goto(-25, -190); t.write("South", font=("Arial Bold", 14, "normal"))
t.penup(); t.goto(170, -8); t.write("East", font=("Arial Bold", 14, "normal"))
t.penup(); t.goto(-210, -8); t.write("West", font=("Arial Bold", 14, "normal"))

turtle.done()