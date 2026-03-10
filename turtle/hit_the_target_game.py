import turtle

SCREEN_WIDTH = 600 # screen width
SCREEN_HEIGHT = 600 # screen height
TARGET_LLEFT_X = 100 # target's lower-left x-coordinate
TARGET_LLEFT_Y = 250 # target's lower-left y-coordinate
TARGET_WIDTH = 25 # target width
FORCE_FACTOR = 30 # arbitrary force factor
PROJECTILE_SPEED = 1 # projectile's animation speed 
NORTH = 90  # angle of north direction
SOUTH = 270 # angle of south direction
EAST = 0 # angle of east direction
WEST = 180 # angle of west direction

turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGET_WIDTH)
turtle.setheading(WEST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_WIDTH)
turtle.penup()

turtle.goto(0, 0)
turtle.setheading(EAST)
turtle.showturtle()
turtle.speed(PROJECTILE_SPEED)

angle = float(input("Enter the projectile's angle: "))
force = float(input("Enter the launch force (1−10): "))

distance = force * FORCE_FACTOR
turtle.setheading(angle)

turtle.pendown()
turtle.forward(distance)


if (turtle.xcor() >= TARGET_LLEFT_X and 
    turtle.xcor() <= TARGET_LLEFT_X + TARGET_WIDTH and
    turtle.ycor() >= TARGET_LLEFT_Y and 
    turtle.ycor() <= TARGET_LLEFT_Y + TARGET_WIDTH):
    print("Target hit!")
else:
    print("Target missed!")

turtle.done()