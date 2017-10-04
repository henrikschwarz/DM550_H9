#!/usr/bin/env python3

import turtle
import sys
from turtles.resizingturtle import ResizingTurtle
from fdl import run

if sys.argv[-1] != __file__ or True:
    file = sys.argv[-1]
    print("possible inputs are dragon, fern, koch, sierpinski, sierpinski2, snowflaske, spiral and tree")
    file = str(input("type filename")) #"fern"

    if file[-4:] != ".fdl":
        file = file + ".fdl"
    #print(file)
    trtl = ResizingTurtle()
    trtl.speed(0)
    turtle.tracer(100)
    run(trtl, "files/"+file)
    turtle.update()
    turtle.mainloop()
else:
    print("Specify file as last argument:")
    print("  $ " + " ".join(sys.argv) + " fern.fdl")
    print("  $ " + " ".join(sys.argv) + " fern")
