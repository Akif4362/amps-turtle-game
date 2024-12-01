import turtle
from PIL import Image

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Maze Game")


maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]


maze_turtle = turtle.Turtle()
maze_turtle.penup()
maze_turtle.color("green", "green")
maze_turtle.shape("turtle")
maze_turtle.speed(0)

start_x = 340
start_y = -360

def draw_cell(x, y):
    maze_turtle.goto(x, y)
    maze_turtle.pendown()
    maze_turtle.begin_fill()
    maze_turtle.forward(50)
    maze_turtle.left(90)
    maze_turtle.forward(50)
    maze_turtle.left(90)
    maze_turtle.forward(50)
    maze_turtle.left(90)
    maze_turtle.forward(50)
    maze_turtle.left(90)
    maze_turtle.end_fill()
    maze_turtle.penup()

for row_id, row in enumerate(maze):
    for column_id, cell in enumerate(row):
        x = start_x - row_id * 50
        y = start_y + column_id * 50

        if cell == 1:
            maze_turtle.goto(x, y)
            maze_turtle.pendown()
            maze_turtle.begin_fill()
            for _ in range(4):
                maze_turtle.forward(50)
                maze_turtle.left(90)

            maze_turtle.end_fill()
            maze_turtle.penup()
            
maze_turtle.hideturtle()

canvas = screen.getcanvas()
canvas.postscript(file="turtle_image.ps", colormode='color')

img = Image.open("turtle_image.ps")
img.save("turtle_image.png")

screen.mainloop()