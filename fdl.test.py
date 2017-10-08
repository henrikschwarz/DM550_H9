"""Tests fdl.py"""
from fdl import apply, step, compute, flatten, parse
def test(func, tests):
    """
    Executes a number of tests on a function.
    `tests` is a list of lists, each representing one test.
    The test lists are in the format [args, expected_outp]
    """
    success = True
    for i, test in enumerate(tests):
        val = func(*test[0])
        expect = test[1]
        if val != expect:
            print("✕ Failed on test", i, val, "!=", expect)
            success = False
        else:
            print("✓ Test",i)
    return success

print("== Apply")
test(apply, (
    (("F", ["A", "B"], ["F", "X", "Y"]),
        [["A", "B"], "X", "Y"]),
    (("F", ["A", "B"], ["X", "Y", "F"]),
        ["X", "Y", ["A", "B"]]),
    (("F", ["A", "B"], ["F"]),
        [["A", "B"]]),
    (("F", ["A", "B"], ["X", "Y"]),
        ["X", "Y"]),
    (("F", ["A", "B"], ["X", "F", "Y"]),
        ["X", ["A", "B"], "Y"]),
    (("F", list("FLFRFLF"), list("FRFRF")), [
        ["F", "L", "F", "R", "F", "L", "F"],
        "R",
        ["F", "L", "F", "R", "F", "L", "F"],
        "R",
        ["F", "L", "F", "R", "F", "L", "F"]
    ])
))

print("== Step")
test(step, (
    (
        (
            {
                "F": ["A", "B"],
                "G": ["C", "D"]
            },
            list("FRGRF"),
        ),
        list("ABRCDRAB")
    ),
    (
        (
            {},
            list("FRGRF"),
        ),
        list("FRGRF")
    ),
    (
        (
            {
                "F": ["A", "B"],
            },
            list("GRG"),
        ),
        list("GRG")
    ),
))

print("== Compute")
test(compute, (
    (
        (
            3, # depth
            { # rules
                "F": ["A", "F", "B"],
                "G": ["F"]
            },
            list("FRG"), # state
        ),
        list("AAAFBBBRAAFBB") # expected
    ),
    (
        (
            0,
            {
                "F": ["A", "F", "B"],
                "G": ["F"]
            },
            list("FRG"),
        ),
        list("FRG")
    )
))


print("== Flatten")
test(flatten, (
    [[[1, 2, [3, 4]]], [1, 2, 3, 4]],
    [[[1, 2, []]], [1, 2]],
    [[[]], []],
    [[[[1, 2], [3, 4]]], [1, 2, 3, 4]],
    [[[[[1], 2], 3]], [1, 2, 3]]
))

print("== Parse")
tests = (
    ( # first test
        "files/dragon.fdl",
        {
            "start": ["F", "X"],
            "3d": False,
            "length": 3,
            "depth": 13,
            "width": 1,
            "color": ["rainbow"],
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
for i, test in enumerate(tests):
    val = parse(test[0])
    expect = test[1]
    if val != expect:
        print("✕ Failed on test", i)
        for key in val:
            if key not in expect:
                print("    Extra key:", key)
            elif val[key] != expect[key]:
                print("    Different value:", key, val[key], "!=", expect[key])
        for key in expect:
            if key not in val:
                print("    Missing key:", key)
    else:
        print("✓ Test", i)
