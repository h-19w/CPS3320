# Hit the Target Game
import turtle
import random

# Named constants
SCREEN_WIDTH = 600 # Screen width
SCREEN_HEIGHT = 600 # Screen height
TARGET_WIDTH = 25 # Width of the target
FORCE_FACTOR = 30 # Arbitrary force factor
PROJECTILE_SPEED = 1 # Projectile's animation speed
NORTH = 90 # Angle of north direction
SOUTH = 270 # Angle of south direction
EAST = 0 # Angle of east direction
WEST = 180 # Angle of west direction

# Setup the window.
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
turtle.shape("turtle")

def draw_target(target_x, target_y):
    """Draw the target at the specified location."""
    turtle.hideturtle()
    turtle.speed(0)
    turtle.penup()
    turtle.goto(target_x, target_y)
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

def get_random_target():
    """Generate random target location within screen bounds."""
    target_x = random.randint(-200, 200)
    target_y = random.randint(-200, 200)
    return target_x, target_y

# Draw the initial target
TARGET_LLEFT_X, TARGET_LLEFT_Y = get_random_target()
draw_target(TARGET_LLEFT_X, TARGET_LLEFT_Y)

# Game loop
while True:
    # Center the turtle.
    turtle.goto(0, 0)
    turtle.setheading(EAST)
    turtle.showturtle()
    turtle.speed(PROJECTILE_SPEED)

    # Get the angle and force from the user.
    angle = float(input("Enter the projectile's angle: "))
    force = float(input("Enter the launch force (1−10): "))

    # Calculate the distance.
    distance = force * FORCE_FACTOR

    # Set the heading.
    turtle.setheading(angle)

    # Launch the projectile.
    turtle.pendown()
    turtle.forward(distance)

    # Did it hit the target? (with a larger hitbox buffer for better hit detection)
    HITBOX_BUFFER = 12
    if (turtle.xcor() >= TARGET_LLEFT_X - HITBOX_BUFFER and
        turtle.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH + HITBOX_BUFFER) and
        turtle.ycor() >= TARGET_LLEFT_Y - HITBOX_BUFFER and
        turtle.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH + HITBOX_BUFFER)):
        print('Target hit!')
        hit = True
    else:
        print('You missed the target.')
        hit = False

    # Ask if the user wants to play again
    play_again = input("\nDo you want to try again? (y/n): ").strip().lower()
    
    # If they want to play again, clear and refresh
    if play_again == 'y':
        turtle.clear()
        # If they hit, generate a new random target location
        if hit:
            TARGET_LLEFT_X, TARGET_LLEFT_Y = get_random_target()
        # Redraw the target (either new location after hit, or same location after miss)
        draw_target(TARGET_LLEFT_X, TARGET_LLEFT_Y)
    else:
        # User chose not to play again, exit the game
        break

# Close the turtle window and release terminal control
turtle.Screen().bye()
