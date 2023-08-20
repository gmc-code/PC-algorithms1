import turtle
import math
import random

def label_point(t, label, penc="black"):
    """Write a label next to a turtle's position.

    Args:
        t (turtle.Turtle): The turtle object.
        label (str): The text to write.
        penc (str): The color of the text. Defaults to "black".
    """
    t.penup()
    t.setx(t.xcor() - 12)
    t.sety(t.ycor() + 2)
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
    for i in range(int((360-extent)/4)): # Draw a dot at each point on the circle
        t.pd()
        t.circle(radius, extent=1)
        t.pu()
        t.circle(radius, extent=3)        
    

def angle_bisector(t, size, angle):
    # Input: An angle with vertex O and rays OA and OB
    # Draw the rays OA and OB first
    ray_length = 1.1*size  # This is the dsdie lengths
    angle_AOB = angle  # This is the angle between OA and OB=
    O = (0, 0) 
    label_point(t, "O", "red")
    draw_line(t, O, ray_length, 0, penc="black")  # Draw the ray OA
    label_point(t, "A", "black")
    draw_line(t, O, ray_length, angle_AOB, penc="black")  # Draw the ray OB
    label_point(t, "B", "black")

    # Step 1: Set the compass width to any convenient length and place the compass point at O
    compass_width = int(size/2)

    # Step 2: Draw an arc that intersects both rays OA and OB and label the intersection points as P and Q
    move_to(t, (compass_width, 0))
    P = t.pos()
    t.dot(5, "blue")
    label_point(t, "P", "blue")

    draw_centered_arc(
        t,
        centre=O,
        angle=0,
        radius=compass_width,
        extent=angle_AOB,
        penw=1,
        penc="red",
    )

    move_to(t, P)
    move_arc(t, centre=(0, 0), angle=0, radius=compass_width, extent=angle_AOB)
    Q = t.pos()
    t.dot(5, "blue")
    label_point(t, "Q", "blue")

    # Step 3: Without changing the compass width, place the compass point at P
    move_to(t, P)

    # Step 4: Draw an arc above the angle
    draw_centered_arc(
        t,
        centre=P,
        angle=0,
        radius=compass_width,
        extent=(1.2*angle_AOB),
        penw=1,
        penc="blue",
    )

    # Step 5: Without changing the compass width, place the compass point at Q
    move_to(t, Q)

    # Step 6: Draw an arc above the angle that intersects the arc drawn from P at R
    draw_centered_arc(
        t,
        centre=Q,
        angle=angle_AOB,
        radius=compass_width,
        extent=-(1.2*angle_AOB),
        penw=1,
        penc="blue",
    )

    move_to(t, P)
    move_arc(t, centre=P, angle=0, radius=compass_width, extent=angle_AOB)
    R = t.pos()
    t.dot(5, "green")
    label_point(t, "R", "green")

    # Step 7: Use the straightedge to draw a line segment from O through R
    move_to(t, O)
    draw_line(t, O, 1.5*t.distance(R[0], R[1]), t.towards(R), penc="green")
    # Step 8: OR is the angle bisector



def main():
    SCREEN_WIDTH = 810
    SCREEN_HEIGHT = 610
    SIZE = 220
    ANGLE = random.randint(40, 90)

    # Set up the turtle screen
    s = turtle.Screen()
    s.bgcolor("white")
    s.title("angle bisector")
    s.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, startx=0, starty=0)
    s.tracer(0, 0)

    # Create a turtle object
    t = turtle.Turtle()
    t.speed(0) # Set the turtle's speed to the fastest
    t.ht()

    angle_bisector(t, size=SIZE, angle=ANGLE)

    s.update()
    s.exitonclick()


if __name__ == "__main__":
    main()
