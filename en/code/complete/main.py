from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

screen.colormode(255)
R = 0
G = 0
B = 255
turtle.color((R, G, B))

colours = [
    (255, 0, 0),     # red
    (255, 165, 0),   # orange
    (255, 255, 0),   # yellow
    (0, 255, 0),     # green
    (0, 127, 255),   # blue
    (0, 0, 255),     # dark blue
    (139, 0, 255)    # violet
]

for j in range(30):
    for i in range(2):
        turtle.forward(200)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.color(colours[i % len(colours)])
    turtle.right(10)