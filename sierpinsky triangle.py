#sierpinsky triangle:

import turtle
bob = turtle.Turtle()

def triangle(x, d): #x is size of triangle, d is depth
colorlist = ["red", "blue", "green", "yellow"]
    if len(colorlist) < d:
        colorlist = colorlist*(d//4+1)
    for i in range(3):
        bob.fd(x)
        bob.lt(120)
        if d > 1:
            triangle(x/2, d-1)
triangle(100,3)