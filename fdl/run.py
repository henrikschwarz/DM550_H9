#!/usr/bin/env python3

import turtle
import sys
import colorsys
from parse import parse
from compute import compute
from execute import execute
from random import random

def run(trtl, fdl):
    trtl.speed(0)
    data = parse(fdl)
    length = data["length"]
    col = data["color"]
    colLen = 200
    if col:
        if len(col) >= 2:
            colLen = int(col[1])
        col = col[0]
    if col and col not in ["rainbow", "travelled"]:
        if col == "random":
            col = (random(), random(), random())
        trtl.pencolor(col)
    trtl.pensize(data["width"])

    # expand the start into a list of commands
    commands = compute(
        depth=data["depth"],
        rules=data["rules"],
        state=data["start"],
    )

    # start drawing
    dist = 0
    turtle.tracer(100)
    for cmdName in commands:
        cmd = data["cmds"][cmdName]
        if cmd[0] == "fd":
            dist = dist + length
        elif cmd[0] == "bk":
            dist = dist - length

        # update colors if needed
        if col == "rainbow":
            trtl.pencolor(colorsys.hsv_to_rgb(trtl.distance(0, 0) % colLen / colLen, 1, 0.8))
        elif col == "travelled":
            trtl.pencolor(colorsys.hsv_to_rgb(dist % colLen / colLen, 1, 0.8))
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
