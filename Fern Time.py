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
def warnings(x,d,angle,s):
    if s * 50 > x:
        print("WARNING: Your input value of s is relatively high compared to x this sacrifices a lot of details"
              " for very little speed. Try values of s around x/100 or lower.")
    if angle < 75 or angle > 105:
        print("WARNING: large values of d has practically no effect on the branches visible to the eye."
              + '\n' + "Furthermore it causes issues with the color parameter, and could cause slow drawing speeds when paired with low values of s")
    if d > 20:
        print("WARNING: large values of d has practically no effect on the branches visible to the eye."
              + '\n' + "Furthermore it causes issues with the color parameter, and could cause slow drawing speeds when paired with low values of s")
    else:
        return
def run_fern(x,d,angle,s=0.3): #d is depth
    t = turtle.Turtle()
    """ Add speed as an optional last argument to increase drawing speed with graph details as tradeoff (set to 0.3)"""
    turtle.tracer(250,100)
    color = 0.3
    colorstep = (1 - color) / d
    fern(t,x,d,angle,color,colorstep,s)
    turtle.update()
    turtle.exitonclick()
    warnings(x,d,angle,s)
run_fern(100,21,98,3)



