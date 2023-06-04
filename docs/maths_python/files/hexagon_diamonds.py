import turtle


def hexagon(t, length=50, start_pos=(0, 0), start_h=60, penw=1, penc="black", fillc=None):
    """Draw a square given side length, from centre left at 60 degrees, turning clockwise.

    Args:
        t (class turtle.Turtle): turtle instance.
        length (int, optional): side length. Defaults to 50.
        start_pos (tuple, optional): start position. Defaults to (0, 0).
        start_h (int, optional): initial heading. Defaults to 0.
        penw (int, optional): pensize. Defaults to 1.
        penc (str, optional): pencolor. Defaults to "black".
        fillc (str, optional): fillcolor. Defaults to None.

    """
    t.pu()
    t.goto(start_pos)
    t.pd()
    t.seth(start_h)

    t.pensize(penw)
    t.pencolor(penc)

    if fillc is not None:
        t.fillcolor(fillc)
        t.begin_fill()

    for _ in range(6):
        t.fd(length)
        t.rt(60)

    if fillc is not None:
        t.end_fill()
        

def tes_hexagon(t, screen_width, screen_height, side_length, start_h=0):
    slsqr3 = side_length * (3 ** 0.5)
    xrep = int(screen_width / side_length)
    yrep = int(screen_height / slsqr3) + 1
    print(yrep)
    for i in range(yrep):
        for j in range(xrep):
            start_pos = (-screen_width//2 + (j * 2 * side_length), screen_height//2 - (i * slsqr3))
            hexagon(t, length=side_length, start_pos=start_pos, start_h=start_h)


def main():
    SCREEN_WIDTH = 810
    SCREEN_HEIGHT = 610
    SIDE_LENGTH = 50
    START_H = 60


    # Set up the turtle screen
    s = turtle.Screen()
    s.bgcolor("white")
    s.title("hexagons and diamonds")
    s.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, startx=0, starty=0)
    s.tracer(0, 0)

    # Create a turtle object
    t = turtle.Turtle()
    t.speed(0) # Set the turtle's speed to the fastest
    t.ht()

    tes_hexagon(t, screen_width=SCREEN_WIDTH, screen_height=SCREEN_HEIGHT, side_length=SIDE_LENGTH, start_h=START_H)

    s.update()
    s.exitonclick()


if __name__ == "__main__":
    main()
