# generates the city skyline using turtle graphics
import turtle
import random

# ------- Setup -------
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("City Skyline")
screen.setup(width=600, height=500)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()

def draw_rect(t, x, y, width, height, color):
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()
    t.penup()
def draw_buildings():
    buildings = [
        # (x, y, width, height)
        (-280, -200, 560, 80),   # ground strip
        (-200, -120, 100, 180),  # left building
        ( -80, -120, 120, 280),  # tall center-left
        (  60, -120,  60, 160),  # center gap filler
        ( 100, -120, 110, 200),  # center-right
        ( 210, -120,  80, 120),  # right building
    ]
    for (x, y, w, h) in buildings:
        draw_rect(t, x, y, w, h, "gray")
def draw_windows():
    windows = [
        # on left building
        (-185, 10),
        (-185, -30),
        # on tall center-left
        ( -60, 100),
        ( -60,  50),
        # on center-right
        ( 120,  30),
        ( 120, -20),
        # on right building
        ( 220, -30),
        # ground level window
        ( -30, -150),
    ]
    for (wx, wy) in windows:
        draw_rect(t, wx, wy, 20, 20, "white")
def draw_stars(n=40):
    # buildings occupy roughly y > -200 and x in building zones
    # easiest: just place stars in upper portion of screen
    for _ in range(n):
        x = random.randint(-280, 280)
        y = random.randint(-50, 240)   # above the tallest building top ~140
        # skip if likely inside a building (rough check)
        if y < 160 and -200 < x < 290:
            y = random.randint(160, 240)
        t.goto(x, y)
        t.dot(3, "white")
def main():
    draw_stars()
    draw_buildings()
    draw_windows()

main()
turtle.done()