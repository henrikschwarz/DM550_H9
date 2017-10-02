import turtle
t = turtle.Turtle()
def fern(x,d,d2,angle):
    t.fd(x)
    if d > 0 and d2 > 0:
        t.lt(angle)
        fern(x/1.5,d-1,d2-1,angle)
        t.rt(90)
        fern(x/1.5,d,d2-1,angle)
        t.rt(angle)
        fern(x/1.5,d-1,d2-1,angle)
        t.lt(90)
    t.bk(x)
def test_fern(x,d,angle): #d is depth
    turtle.tracer(100,12)
    d2 = d
    fern(x,d,d2,angle)
    turtle.update()
    turtle.exitonclick()
test_fern(100,3,93)