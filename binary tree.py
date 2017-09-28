import turtle
bob = turtle.Turtle()
def line(x):
    bob.fd(x)
    bob.lt(180)
    bob.fd(x)
    bob.lt(180)

def branch(x, d, color, colorstep):
    bob.width(0.5 + 0.08 * d ** 2)
    bob.color([0, color, 0])
    newx = x * (7 / 10)
    angle = 30
    bob.fd(x)
    bob.lt(angle)
    if d != 0:  # left branch
        branch(newx, d - 1, color + colorstep, colorstep)
    else:
        line(newx)
    bob.rt(angle * 2)
    if d != 0:  # right branch
        branch(newx, d - 1, color + colorstep, colorstep)
    else:
        line(newx)
    bob.rt(180 - angle)
    bob.penup()
    bob.fd(x)
    bob.pendown()
    bob.rt(180)

def plantATree(x, d):
    color = 0.3
    colorstep = (1 - color) / d
    turtle.tracer(100, 16)
    # bob.speed(0)
    bob.lt(90)
    branch(x, d, color, colorstep)
    turtle.exitonclick()

plantATree(100, 12)
