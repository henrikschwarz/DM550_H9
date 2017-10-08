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
def run_fern(x,d,angle,s=0.3): #d is depth
    if s*50 > x:
        print("WARNING: Your input value of s is relatively high compared to x this sacrifices alot of details"
              " for very little speed. Try values of s around x/100 or lower.")
    if angle < 75 or angle > 105:
        print("WARNING: to create more fern like output, try values of angle around 80-100")
    t = turtle.Turtle()
    """ Add speed as an optional last argument to increase drawing speed with graph details as tradeoff (set to 0.3)"""
    turtle.tracer(250,100)
    color = 0.3
    colorstep = (1 - color) / d
    fern(t,x,d,angle,color,colorstep,s)
    turtle.update()
    turtle.exitonclick()
run_fern(100,12,106)