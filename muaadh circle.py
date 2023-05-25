import turtle

from itertools import cycle
colors = cycle(['yellow', 'blue', 'red', 'green', 'navy', 'pink'])


def draw_circle(size,angle,shift):
    turtle.bgcolor(next(colors))
    turtle.pencolor(next(colors))
    turtle.circle(size)
    turtle.right(angle)
    turtle.forward(shift)
    draw_circle(size+5, angle+1,shift+1)

turtle.bgcolor('pink')
turtle.speed('fast')
turtle.pensize(28)
draw_circle(30,0,1)
