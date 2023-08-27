import turtle
import math
import io
from PIL import Image
from pathlib import Path



currfile_dir_dir = Path(__file__).parent.parent         # Get the directory of the current script


def label_point(t, label, deltax=-12, deltay=2, penc="black"):
    """
    Write a label next to the current position of the turtle.

    Args:
        t (turtle.Turtle): The turtle object used for drawing.
        label (str): The text to be displayed as the label.
        deltax (int, optional): The horizontal offset from the turtle's position. Defaults to -12.
        deltay (int, optional): The vertical offset from the turtle's position. Defaults to 2.
        penc (str, optional): The color of the text. Defaults to "black".
    """
    t.penup()  # Lift the pen to avoid drawing while moving
    t.setx(t.xcor() + deltax)  # Move the turtle horizontally by deltax units
    t.sety(t.ycor() + deltay)  # Move the turtle vertically by deltay units
    t.pendown()  # Lower the pen to start drawing
    t.pencolor(penc)  # Set the pen color for the label
    t.write(label, font=("Arial", 12, "normal"))  # Display the label using the specified font



def move_to(t, point):
    """
    Move the turtle to a specified point without drawing.

    Args:
        t (turtle.Turtle): The turtle object used for drawing.
        point (tuple): The coordinates of the target point (x, y).
    """
    t.penup()  # Lift the pen to avoid drawing while moving
    t.goto(point)  # Move the turtle to the specified point


def move_arc(t, centre=(0, 0), angle=0, radius=10, extent=360):
    """
    Move the turtle along an arc with a given center, angle, radius, and extent.

    Args:
        t (turtle.Turtle): The turtle object used for drawing.
        centre (tuple, optional): The coordinates of the center of the arc (x, y). Defaults to (0, 0).
        angle (int, optional): The angle of the initial position of the turtle relative to the center. Defaults to 0.
        radius (int, optional): The radius of the arc. Defaults to 10.
        extent (int, optional): The angle of the arc that the turtle moves along. Defaults to 360.
    """
    move_to(t, centre)  # Move the turtle to the specified center
    t.seth(angle)  # Set the turtle's heading (angle) to the initial angle
    t.fd(radius)  # Move the turtle forward by the specified radius
    t.seth(angle + 90)  # Set the turtle's heading to be perpendicular to the initial angle
    t.circle(radius, extent=extent)  # Draw an arc with the specified radius and extent


def draw_line_points(t, point1, point2, penw=1, penc="black"):
    """
    Draw a straight line from a starting point (point1) to an ending point (point2) using the specified pen width and color.

    Args:
        t (turtle.Turtle): The turtle object used for drawing.
        point1 (tuple): The coordinates of the starting point (x, y).
        point2 (tuple): The coordinates of the ending point (x, y).
        penw (int, optional): The width of the line. Defaults to 1.
        penc (str, optional): The color of the line. Defaults to "black".
    """
    move_to(t, point1)  # Move the turtle to the starting point
    t.pendown()  # Put the pen down to start drawing
    t.pencolor(penc)  # Set the pen color
    t.pensize(penw)  # Set the pen width
    t.goto(point2)  # Draw a straight line to the ending point


def draw_centered_arc(t, centre=(0, 0), angle=0, radius=10, extent=360, penw=1, penc="black"):
    """
    Draw an arc with a given center, angle, radius, extent, pen width, and color.

    Args:
        t (turtle.Turtle): The turtle object used for drawing.
        centre (tuple, optional): The coordinates of the center of the arc (x, y). Defaults to (0, 0).
        angle (int, optional): The angle of the initial position of the turtle relative to the center. Defaults to 0.
        radius (int, optional): The radius of the arc. Defaults to 10.
        extent (int, optional): The angle of the arc that the turtle draws. Defaults to 360.
        penw (int, optional): The width of the pen. Defaults to 1.
        penc (str, optional): The color of the pen. Defaults to "black".
    """
    move_to(t, centre)  # Move the turtle to the specified center
    t.seth(angle)  # Set the turtle's heading (angle) to the initial angle
    t.pensize(penw)  # Set the pen width
    t.pencolor(penc)  # Set the pen color
    t.fd(radius)  # Move the turtle forward by the specified radius
    t.pd()  # Put the pen down to start drawing
    t.seth(angle + 90)  # Set the turtle's heading to be perpendicular to the initial angle
    t.circle(radius, extent=extent)  # Draw an arc with the specified radius and extent

    # Draw dots at regular intervals along the arc
    for i in range(int((360 - extent) / 60)):
        t.pd()  # Put the pen down to draw
        t.circle(radius, extent=45)  # Draw a small arc segment
        t.pu()  # Lift the pen to stop drawing
        t.circle(radius, extent=15)  # Move to the next position to draw a dot


# Define a function to construct an equilateral triangle
def construct_equilateral_triangle_step(t, L, w, frame):
    # Hide the turtle
    t.hideturtle()
    A = (-L / 2, 0)
    B = (L / 2, 0)
    C = (0, L * math.sqrt(3) / 2)

    if frame == 0:
        # Draw the line segment AB
        draw_line_points(t, A, B, penw=w, penc="black")
    elif frame == 1:
        # Label the point A
        move_to(t, A)
        t.dot(5, "red")
        label_point(t, "A", deltax=-12, deltay=2, penc="red")
    elif frame == 2:
        # Label the point B
        move_to(t, B)
        t.dot(5, "blue")
        label_point(t, "B", deltax=12, deltay=2, penc="blue")
    elif frame == 3:
        # Draw the circle C1 with center A and radius L
        draw_centered_arc(t, A, angle=0, radius=L, extent=0, penw=w, penc="red")
    elif frame == 4:
        # Draw the circle C2 with center B and radius L
        draw_centered_arc(t, B, angle=120, radius=L, extent=0, penw=w, penc="blue")
        # Find the point C where C1 and C2 intersect
        # This can be done by using some trigonometry
        # The angle between AB and AC is 60 degrees
        # The distance from A to C is L
        # The x-coordinate of C is L * cos(60) = L/2
        # The y-coordinate of C is L * sin(60) = L * sqrt(3) / 2
    elif frame == 5:
        # Draw the line segment AC
        draw_line_points(t, A, C, penw=w, penc="red")
    elif frame == 6:
        # Draw the line segment BC
        draw_line_points(t, B, C, penw=w, penc="blue")
        # Label the point C
    elif frame == 7:
        t.dot(5, "green")
        label_point(t, "C", deltax=0, deltay=5, penc="green")


def wait_for_click(x, y):
    """
    Callback function to wait for a mouse click event.

    Args:
        x (float): The x-coordinate of the mouse click.
        y (float): The y-coordinate of the mouse click.
    """
    global continue_animation
    continue_animation = True


def main():
    """
    Main function to create an animated GIF of the step-by-step construction of an equilateral triangle.

    Note:
        This function sets up the turtle screen, waits for a mouse click to proceed to the next step,
        calls the `construct_equilateral_triangle_step` function to construct each step of the triangle,
        captures each frame as an image, and then saves the frames as an animated GIF.
    """
    global continue_animation
    SCREEN_WIDTH = 500
    SCREEN_HEIGHT = 400
    L = 100
    # Set up the turtle screen
    s = turtle.Screen()
    s.bgcolor("white")
    s.title("Equilateral Triangle Construction")
    s.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, startx=0, starty=0)
    s.tracer(1, 10)
    # Create a turtle object
    t = turtle.Turtle()
    t.speed(10)
    t.ht()
    images = []  # List to hold frames for the GIF
    # Wait for a mouse click before proceeding to the next step
    s.update()
    continue_animation = False
    while not continue_animation:
        s.onclick(wait_for_click)
        s.update()
    # Call the function to construct each step of the triangle
    for step in range(8):
        construct_equilateral_triangle_step(t, L, 1, step)
        # Capture the screen as an image and append it to the list
        screen_img = s.getcanvas().postscript(colormode="color")
        img = Image.open(io.BytesIO(screen_img.encode("utf-8")))
        images.append(img)
    # Define the path for the GIF
    gif_path = currfile_dir_dir / "gifs" / "construct_equilateral_triangle.gif"
    # Save the frames as a GIF
    images[0].save(gif_path, save_all=True, append_images=images[1:], duration=8000 / 8, loop=0, dpi=600)
    s.bye()                                                                                                                                  


if __name__ == "__main__":
    main()
