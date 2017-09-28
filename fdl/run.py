#!/usr/bin/env python3

import turtle
import sys
import colorsys
from parse import parse
from compute import compute
from execute import execute
from random import random

RAINBOW_LEN = 200
def run(trtl, fdl):
    trtl.speed(0)
    data = parse(fdl)
    length = data["length"]
    col = data["color"]
    if col and col != "rainbow":
        col = data["color"]
        if col == "random":
            col = (random(), random(), random())
        trtl.pencolor(col)
    commands = compute(
        depth=data["depth"],
        rules=data["rules"],
        state=data["start"],
    )
    turtle.tracer(100)
    for cmdName in commands:
        cmd = data["cmds"][cmdName]
        if col == "rainbow":
            dist = trtl.distance(0, 0) % RAINBOW_LEN / RAINBOW_LEN
            trtl.pencolor(colorsys.hsv_to_rgb(dist, 1, 0.8))
        result = execute(
            trtl=trtl,
            length=length,
            cmd=cmd[0],
            args=cmd[1]
        )

        if cmd[0] == "scale":
            length = result
    turtle.update()
    turtle.mainloop()


if sys.argv[-1]:
    file = sys.argv[-1]
    if file[-4:] != ".fdl":
        file = file + ".fdl"
    run(turtle.Turtle(), "../files/"+file)
else:
    print("Specify file as last argument:")
    print("  $ run.py fern.fdl")
