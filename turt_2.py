import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle ")
screen.bgpic("turtle_image.png")

t = turtle.Turtle()
t.penup()
t.shape("turtle")
t.color("blue")
t.goto(-302, -213)
t.pendown()


# def get_coordinates(x, y):
#     print(f"Clicked at: ({x}, {y})")

# screen.onscreenclick(get_coordinates)

screen.mainloop()
