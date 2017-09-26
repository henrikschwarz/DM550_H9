import turtle

bob = turtle.Turtle()

def drawRightbranch(x,s): #x is depth, s is size

    for i in range(x):
        bob.fd(s)
        bob.rt(60)
        s = s/2
    return s
def climbBack(c,t,s): #how much we climb back, t = 0 if we turned right and 1 if left
    if t == 0:
        while c > 0:
            bob.lt(60)
            bob.fd(s)
            c = c-1
            s = s*2
    if t == 1:
        while c > 0:
            bob.lt(60)
            bob.fd(s)
            s = s*2
            c = c-1
    return s
def drawLeftBranch(x,s):
    for i in range(x):
        bob.fd(s)
        bob.lt(60)
        s = s/2
    return s


def plantATree(x,s):
    bob.lt(90)
    LenDep = drawLeftBranch(x,s)
    c = 1
    while c < x:
    #loop to climb back until depth 1
        climbBack(c,1,LenDep)
        LenDep = 2*LenDep
        c = c +1


plantATree(5,100)