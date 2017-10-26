"""Contains FDL-related functions. Generally you only want `run`"""
import colorsys
from random import random

# overwrites built-in :(
def apply(ruleName, ruleDef, state):
    """Replaces every occurence of a rule in a state with the rules definition"""
    return list(map(
        lambda key: ruleDef if key == ruleName else key,
        state
    ))

def flatten(nested_list):
    """Flattens a list"""
    flattened = []
    for val in nested_list:
        if isinstance(val, (list, tuple)):
            flattened.extend(flatten(val))
        else:
            flattened.append(val)
    return flattened

def step(rules, state):
    """Takes a state and a dict of rules, applies rules to all states"""
    for ruleName, ruleDef in rules.items():
        state = apply(ruleName, ruleDef, state)

    return flatten(state)

def compute(depth, rules, state):
    """Repeatedly inserts rules into a state"""
    for _ in range(0, depth):
        state = step(rules, state)
    return state

def execute(trtl, length, cmd, args):
    """Executes a command on a turtle"""
    if cmd == "scale":
        return length * float(args[0])
    elif cmd == "nop":
        return None
    else:
        method = getattr(trtl, cmd)
        if cmd in ("fd", "bk", "forward", "backward"):
            args = [float(length)]
        method(*args)

def parse(fdl_file):
    """Parses an FDL file into a dictionary of format:
    {
        start: ["F"],
        length: 1,
        depth: 1,
        width: 1.0,
        color: ["rainbow"],
        rules: {
            "F": ["A", "B", "C"],
            "G": ["X, "Y", "Z"]
        },
        cmds: {
            "A": ("method_name", ["arg1", "arg2"])
        }
    }
    """
    file = open(fdl_file)
    data = {
        "3d": False,
        "length": 1,
        "depth": 1,
        "width": 1.0,
        "cmds": {},
        "rules": {},
        "color": ["rainbow"]
    }
    for line in file:
        split = line.strip().split(" ")
        cmd = split[0].lower()
        args = split[1:]
        if cmd in ("start", "color"): # list params
            data[cmd] = args
        elif cmd in ("depth", "length"): # int params
            data[cmd] = int(float(args[0]))
        elif cmd == "width": # float params
            data[cmd] = float(args[0])
        elif cmd == "3d": # boolean params
            data[cmd] = True
        elif cmd == "cmd":
            data["cmds"][args[0]] = (args[1], list(map(
                convert_str,
                args[2:]
            )))
        elif cmd == "rule" and args[1] == "->":
            # update our rule dict
            data["rules"][args[0]] = args[2:]
    return data

def convert_str(string):
    """Converts a string to whatever format matches first
    Currently only supports floats/integers"""
    try:
        if "." in string:
            return float(string)
        return int(string)
    except (ValueError, TypeError):
        pass
    return string

def run(trtl, fdl):
    data = parse(fdl)
    length = data["length"]
    # code to determine color and color loop length
    col = data["color"]
    colLen = 200
    if col:
        if len(col) >= 2:
            colLen = int(col[1])
        col = col[0]
    if col and col not in ("rainbow", "travelled"):
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
    dist = 0 # keep track of distance travelled in case color is "travelled"
    for cmdName in commands:
        cmd = data["cmds"][cmdName]
        if cmd[0] == "fd":
            dist += length
        elif cmd[0] == "bk":
            dist -= length

        # update colors if needed
        if col == "rainbow":
            # if "rainbow", pick hue based on distance from home
            trtl.pencolor(colorsys.hsv_to_rgb(trtl.distance(0, 0) % colLen / colLen, 1, 0.8))
        elif col == "travelled":
            # if "travelled", pick hue based on distance travelled
            trtl.pencolor(colorsys.hsv_to_rgb(dist % colLen / colLen, 1, 0.8))
        
        # actually execute the command
        result = execute(
            trtl=trtl,
            length=length,
            cmd=cmd[0],
            args=cmd[1]
        )
        # handle the special command "scale"
        if cmd[0] == "scale":
            length = result
