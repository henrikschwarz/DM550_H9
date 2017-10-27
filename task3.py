import turtle


def draw_tree(t,d,l,w,s):
    if l < s:
        return # skip drawing if it is too small
    t.width(w*(d/2)) # width adjusted by dpeth (more depth, smaller fraction)
    t.color([0,0.2+(0.8/d),0])
    t.pendown() # drawing mode
    t.fd(l)
    if d > 1:
        t.lt(30) # turn to make first branch
        draw_tree(t,d-1,l*.7,w*.8,s) # call main function draw_tree
        t.rt(60) # turn to next branch
        draw_tree(t,d-1,l*.7,w*.8,s)
        t.lt(30)
    t.penup() # leave drawing mode
    t.lt(180) # return to starting point
    t.fd(l)
    t.lt(180)


t = turtle.Turtle() # turtle project
t.speed(0) # setting speed
t.lt(90) # move turtle to better starting point
t.penup() # stop drawing
t.bk(200)
t.pendown() # draw mode again
turtle.tracer(100,16) # faster drawing mode
draw_tree(t,14,150,2,1) # draw binary tree
turtle.exitonclick()