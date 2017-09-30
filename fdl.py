"""Contains FDL-related functions. Generally you only want `run`"""

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
        if isinstance(val, list):
            flattened.extend(flatten(val))
        else:
            flattened.append(val)
    return flattened

def step(rules, state):
    """Takes a state and a list of rules, applies rules to all states"""
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
        return length
    else:
        method = getattr(trtl, cmd)
        if cmd in ["fd", "bk"]:
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
        if cmd in ["start", "color"]: # list params
            data[cmd] = args
        elif cmd in ["depth", "length"]: # int params
            data[cmd] = int(float(args[0]))
        elif cmd == "width": # float params
            data[cmd] = float(args[0])
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
    """Converts a string to whatever format matches first"""
    try:
        if "." in string:
            return float(string)
        return int(string)
    except (ValueError, TypeError):
        pass
    return string
