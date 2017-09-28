import turtle


def triangle(t, n, l):
    for i in range(3):
        t.fd(l)
        t.lt(120)
        if n != 1:
            triangle(t,n-1,l/2)
t = turtle.Turtle()
triangle(t,6, 600)
turtle.exitonclick()
