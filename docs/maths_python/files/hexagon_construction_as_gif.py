import turtle
import io
from PIL import Image
from pathlib import Path


def draw_centered_circle(t, centre=(0, 0), radius=10, penw=1, penc="black", fillc=None):
    t.pu()
    t.goto(centre)
    t.seth(0)
    t.fd(radius)
    t.seth(90)
    t.pensize(penw)
    t.pencolor(penc)
    t.pd()
    if fillc is not None:
        t.fillcolor(fillc)
        t.begin_fill()
    t.circle(radius)
    t.seth(0)
    if fillc is not None:
        t.end_fill()


def draw_circles(t, center, num_circles, radius, images):
    # do central circle
    draw_centered_circle(t, centre=center, radius=radius, penw=1, penc="black")
    # Capture the screen and add to images
    screen_img = turtle.getcanvas().postscript(colormode="color")
    img = Image.open(io.BytesIO(screen_img.encode("utf-8")))
    images.append(img)
    # surrounding overlapping circles
    angle_increment = 360 / num_circles
    for i in range(num_circles):
        t.pu()
        t.goto(center)
        t.seth(angle_increment * i)
        t.fd(radius)
        circ_center = t.pos()
        draw_centered_circle(t, centre=circ_center, radius=radius, penw=1, penc="red")

        # Capture the screen and add to images
        screen_img = turtle.getcanvas().postscript(colormode="color")
        img = Image.open(io.BytesIO(screen_img.encode("utf-8")))
        images.append(img)


def draw_hexagon(t, center, num_circles, radius, dot_size, images):
    # Draw dots at hexagon vertices
    t.penup()
    t.goto(center[0], center[1])
    t.pencolor("blue")
    draw_dot(t, t.pos(), dot_size)
    # Capture the screen and add to images
    screen_img = turtle.getcanvas().postscript(colormode="color")
    img = Image.open(io.BytesIO(screen_img.encode("utf-8")))
    images.append(img)

    # t.setheading(0)
    # t.penup()
    # t.forward(radius)
    # draw_dot(t, t.pos(), 15)
    # t.setheading(120)
    angle_increment = 360 / num_circles

    t.pu()
    t.goto(center)
    t.seth(0)
    t.fd(radius)

    draw_dot(t, t.pos(), dot_size)
    # Capture the screen and add to images
    screen_img = turtle.getcanvas().postscript(colormode="color")
    img = Image.open(io.BytesIO(screen_img.encode("utf-8")))
    images.append(img)

    for i in range(6):
        t.pu()
        t.goto(center)
        t.seth(angle_increment * (i + 1))
        t.fd(radius)

        draw_dot(t, t.pos(), dot_size)
        # Capture the screen and add to images
        screen_img = turtle.getcanvas().postscript(colormode="color")
        img = Image.open(io.BytesIO(screen_img.encode("utf-8")))
        images.append(img)

        t.left(240)
        t.fd(radius)
        # Capture the screen and add to images
        screen_img = turtle.getcanvas().postscript(colormode="color")
        img = Image.open(io.BytesIO(screen_img.encode("utf-8")))
        images.append(img)


def draw_dot(t, position, size):
    t.penup()
    t.goto(position)
    t.pendown()
    t.dot(size, "blue")


def main():
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    CIRCLE_RADIUS = 100
    NUM_CIRCLES = 6
    DOT_SIZE = 5  # 5mm dot size

    s = turtle.Screen()
    s.bgcolor("white")
    s.title("Hexagon Construction using Compass")
    s.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    s.tracer(1, 1)

    t = turtle.Turtle()
    t.speed(0)

    center = (0, 0)
    images = []

    t.hideturtle()

    draw_circles(t, center, NUM_CIRCLES, CIRCLE_RADIUS, images)

    draw_hexagon(t, center, NUM_CIRCLES, CIRCLE_RADIUS, DOT_SIZE, images)

    draw_dot(t, center, DOT_SIZE)
    screen_img = s.getcanvas().postscript(colormode="color")
    img = Image.open(io.BytesIO(screen_img.encode("utf-8")))
    images.append(img)

    currfile_dir = Path(__file__).parent.parent
    gif_path = currfile_dir / "gifs" / "hexagon_construction.gif"

    images[0].save(gif_path, save_all=True, append_images=images[1:], duration=500, loop=0, dpi=300)

    s.update()
    s.exitonclick()


if __name__ == "__main__":
    main()
