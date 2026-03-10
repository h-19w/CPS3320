# Hit the Target Game
import turtle

# Named constants
SCREEN_WIDTH = 600        # Screen width
SCREEN_HEIGHT = 600       # Screen height
TARGET_LEFT_X = 100       # Target's lower-left X
TARGET_LEFT_Y = 100       # Target's lower-left Y
TARGET_WIDTH = 25         # Width of the target
FORCE_FACTOR = 10         # Arbitrary force factor
PROJECTILE_SPEED = 1      # Speed of the projectile (not used in this simple version)
NORTH = 90          # Angle of north direction
SOUTH = 270         # Angle of south direction
EAST = 0            # Angle of east direction
WEST = 180          # Angle of west direction

# Set up the display window.
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
turtle.speed(0)
turtle.penup()
turtle.goto(TARGET_LEFT_X, TARGET_LEFT_Y)
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

# Center the turtle.
turtle.setposition(0, 0)
turtle.setheading(EAST)
turtle.showturtle()
turtle.speed(PROJECTILE_SPEED)

# Get the angle and force from the user.
angle = float(input("Enter the projectile angle: "))
force = float(input("Enter the launch force (1-10): "))

# Calculate the distance.
distance = force * FORCE_FACTOR

# Set the heading to the angle.
turtle.setheading(angle)
turtle.pendown()
turtle.forward(distance)

# Did it hit the target?
if (turtle.xcor() >= TARGET_LEFT_X and
    turtle.xcor() <= TARGET_LEFT_X + TARGET_WIDTH and
    turtle.ycor() >= TARGET_LEFT_Y and
    turtle.ycor() <= TARGET_LEFT_Y + TARGET_WIDTH):
    print("Target hit!")
else:
    print("Target missed!")

turtle.done()
