import turtle
import math
import random


def label_point(t, label, deltax=-12, deltay=2, penc="black"):
    """Write a label next to a turtle's position.

    Args:
        t (turtle.Turtle): The turtle object.
        label (str): The text to write.
        deltax (int): The horizontal offset from the turtle's position. Defaults to -12.
        deltay (int): The vertical offset from the turtle's position. Defaults to 2.
        penc (str): The color of the text. Defaults to "black".
    """
    t.penup()
    t.setx(t.xcor() + deltax)
    t.sety(t.ycor() + deltay)
    t.pendown()
    t.pencolor(penc)
    t.write(label, font=("Arial", 12, "normal"))


# Define a function to move the turtle to a point (x, y) with the penup
def move_to(t, point):
    """Move the turtle to a given point without drawing.

    Args:
        t (turtle.Turtle): The turtle object.
        point (tuple): The coordinates of the point as (x, y).
    """
    t.penup()
    t.goto(point)


def move_arc(t, centre=(0, 0), angle=0, radius=10, extent=360):
    """Move the turtle along an arc with a given centre, angle and radius.

    Args:
        t (turtle.Turtle): The turtle object.
        centre (tuple): The coordinates of the centre of the arc as (x, y). Defaults to (0, 0).
        angle (int): The angle of the initial position of the turtle relative to the centre. Defaults to 0.
        radius (int): The radius of the arc. Defaults to 10.
        extent (int): The angle of the arc that the turtle moves along. Defaults to 360.
    """
    move_to(t, centre)
    t.seth(angle)
    t.fd(radius)
    t.seth(angle + 90)
    t.circle(radius, extent=extent)


def draw_line(t, point, length, direction, penc="black"):
    """Draw a straight line from a given point with a given length, direction and colour.

    Args:
        t (turtle.Turtle): The turtle object.
        point (tuple): The coordinates of the starting point as (x, y).
        length (int): The length of the line.
        direction (int): The direction of the line in degrees.
        penc (str): The color of the line. Defaults to "black".
    """
    move_to(t, point)
    t.setheading(direction)
    t.pendown()
    t.pencolor(penc)
    t.forward(length)


def draw_centered_arc(t, centre=(0, 0), angle=0, radius=10, extent=360, penw=1, penc="black"):
    """Draw an arc with a given centre, angle, radius, extent, pen width and color.

    Args:
        t (turtle.Turtle): The turtle object.
        centre (tuple): The coordinates of the centre of the arc as (x, y). Defaults to (0, 0).
        angle (int): The angle of the initial position of the turtle relative to the centre. Defaults to 0.
        radius (int): The radius of the arc. Defaults to 10.
        extent (int): The angle of the arc that the turtle draws. Defaults to 360.
        penw (int): The width of the pen. Defaults to 1.
        penc (str): The color of the pen. Defaults to "black".
    """
    move_to(t, centre)
    t.seth(angle)
    t.pensize(penw)
    t.pencolor(penc)
    t.fd(radius)
    t.pd()
    t.seth(angle + 90)
    t.circle(radius, extent=extent)
    for i in range(int((360 - extent) / 4)):  # Draw a dot at each point on the circle
        t.pd()
        t.circle(radius, extent=1)
        t.pu()
        t.circle(radius, extent=3)


# Define a function to construct an equilateral triangle
def construct_equilateral_triangle(t, L):
    # Hide the turtle
    t.hideturtle()
    # Draw the line segment AB
    draw_line(t, (-L / 2, 0), L, 0)

    # Label the point A
    move_to(t, (-L / 2, 0))
    t.dot(5, "red")
    label_point(t, "A", deltax=-12, deltay=2, penc="red")
    
    # Label the point B
    move_to(t, (L / 2, 0))
    t.dot(5, "blue")
    label_point(t, "B", deltax=12, deltay=2, penc="blue")

    # Draw the circle C1 with center A and radius L
    draw_centered_arc(t, (-L / 2, 0), angle=0, radius=L, extent=0, penw=1, penc="red")
    # Draw the circle C2 with center B and radius L
    draw_centered_arc(t, (L / 2, 0), angle=120, radius=L, extent=0, penw=1, penc="blue")
    # Find the point C where C1 and C2 intersect
    # This can be done by using some trigonometry
    # The angle between AB and AC is 60 degrees
    # The distance from A to C is L
    # The x-coordinate of C is L * cos(60) = L/2
    # The y-coordinate of C is L * sin(60) = L * sqrt(3) / 2
    C = (L / 2, L * math.sqrt(3) / 2)
    # Draw the line segment AC
    draw_line(t, (-L / 2, 0), L, 60, penc="red")
    # Draw the line segment BC
    draw_line(t, (L / 2, 0), L, 120, penc="blue")
    # Label the point C
    t.dot(5, "green")
    label_point(t, "C", deltax=0, deltay=5, penc="green")



def main():
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    L = 100

    # Set up the turtle screen
    s = turtle.Screen()
    s.bgcolor("white")
    s.title("equilateral triangle construction")
    s.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, startx=0, starty=0)
    s.tracer(1, 1)

    # Create a turtle object
    t = turtle.Turtle()
    t.speed(10) # Set the turtle's speed to the fastest
    t.ht()


    # Call the function to construct the triangle
    construct_equilateral_triangle(t, L)

    s.update()
    s.exitonclick()


if __name__ == "__main__":
    main()