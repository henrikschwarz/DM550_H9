import turtle


def triangle(t, d, l):
    for i in range(3): # draw triangle
        t.fd(l)
        t.lt(120)
        if d > 1:
            triangle(t,d-1,l/2) # draw smaller triangle

t = turtle.Turtle()
t.speed(0)
triangle(t,6, 500)
turtle.exitonclick()
