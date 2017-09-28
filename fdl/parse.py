def parse(fdl_file):
    """Parses an FDL file into a dictionary of format:
    {
        start: ["F"],
        length: 1,
        depth: 1,
        color: "red",
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
        else:
            return int(string)
    except (ValueError, TypeError):
        pass
    return string

if __name__ == "__main__":
    tests = (
        ( # first test
            "../files/dragon.fdl",
            {
                "start": ["F", "X"],
                "length": 3,
                "depth": 13,
                "rules": {
                    "X": ["X", "R", "Y", "F"],
                    "Y": ["F", "X", "L", "Y"],
                },
                "cmds": {
                    "F": ("fd", []),
                    "X": ("nop", []),
                    "Y": ("nop", []),
                    "L": ("lt", [90]),
                    "R": ("rt", [90]),
                }
            }
        ),
    )
    success = True
    for i, test in enumerate(tests):
        val = parse(test[0])
        expect = test[1]
        if val != expect:
            success = False
            print("✕ Failed on test", i)
            for key in val:
                if key not in expect:
                    print("    Extra key:", key)
                elif val[key] != expect[key]:
                    print("    Different value:", key, val[key], "!=", expect[key])
            for key in expect2:
                if key not in val:
                    print("    Missing key:", key)
        else:
            print("✓ Test", i)
