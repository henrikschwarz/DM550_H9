#sierpinsky triangle:

import turtle
bob = turtle.Turtle()

def triangle(x, d): #x is size of triangle, d is depth
    for i in range(3):
        bob.fd(x)
        bob.lt(120)
        if d > 1:
            triangle(x/2, d-1)
bob.speed(0)
triangle(100,8)
turtle.exitonclick()
