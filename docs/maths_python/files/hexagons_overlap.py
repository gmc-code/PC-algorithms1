import turtle


def draw_hexagon(t, x, y, side_length, start_h=0):
    t.penup()
    t.goto(x,y)
    t.seth(start_h)
    t.pendown()
    for i in range(6):
        t.forward(side_length)
        t.right(60)

def hexagonal_overlap(t, swidth, sheight, side_length, overlap_factor=0.75):
    vert_overlap_factor = overlap_factor
    hor_overlap_factor = overlap_factor * 2
    side_height = side_length * 3**0.5
    rows = int(sheight / (side_height * vert_overlap_factor))+2
    cols = int(swidth / (side_length * vert_overlap_factor))+1
    for i in range(rows):
        y = sheight//2 + (1-i) * side_height * vert_overlap_factor
        for j in range(cols):
            x = -swidth//2  + (j-1) * side_length * hor_overlap_factor
            if i % 2 == 1:
                x += side_length * vert_overlap_factor
            draw_hexagon(t, x, y, side_length)



s = turtle.Screen()
s.bgcolor("white")
s.title("draw_centered_regular_polygon")
s.setup(width=800, height=600, startx=None, starty=None)
s.tracer(0, 0)

t = turtle.Turtle()
t.speed(0)
t.ht()

hexagonal_overlap(t, 800, 600, 50, overlap_factor=0.75)

s.update()
s.exitonclick()