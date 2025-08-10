import turtle  # importing library

# Set up the screen
my_wn = turtle.Screen()
my_wn.bgcolor("light blue")  # screen background color
my_wn.title("Turtle")

# Create turtle object
my_pen = turtle.Turtle()
size = 10  # initial size

# Infinite loop to draw squares with increasing size
while True:
    for i in range(4):
        my_pen.forward(size)
        my_pen.left(90)
    size += 5  # increase size for next square
