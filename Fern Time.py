import turtle
def fern(t,x,d,angle,color,colorstep,s):
    t.color([0,color,0])
    if x < s: # s is speed
        return
    t.fd(x)
    if d > 0:
        t.lt(angle)
        fern(t,x/2.8,d-1,angle,color,colorstep,s)
        t.rt(90)
        fern(t,x/1.3,d-1,angle,color+colorstep,colorstep,s)
        t.rt(angle)
        fern(t,x/2.8,d-1,angle,color,colorstep,s)
        t.lt(90)
    t.bk(x)
def run_fern(x,d,angle,speed2=0.3): #d is depth
    t = turtle.Turtle()
    """ Add speed as an optional last argument to increase drawing speed with graph details as tradeoff (set to 0.3)"""
    turtle.tracer(250,100)
    color = 0.3
    s = speed2
    colorstep = (1 - color) / d
    fern(t,x,d,angle,color,colorstep,s)
    turtle.update()
    turtle.exitonclick()
run_fern(100,12,98,0.3)