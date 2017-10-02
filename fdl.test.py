"""Tests fdl.py"""
from fdl import apply, step, compute, flatten, parse

print("== Apply")
tests = (
    (["A", "B"], ["F", "X", "Y"], [["A", "B"], "X", "Y"]),
    (["A", "B"], ["X", "Y", "F"], ["X", "Y", ["A", "B"]]),
    (["A", "B"], ["F"], [["A", "B"]]),
    (["A", "B"], ["X", "Y"], ["X", "Y"]),
    (["A", "B"], ["X", "F", "Y"], ["X", ["A", "B"], "Y"]),
    (list("FLFRFLF"), list("FRFRF"), [
        ["F", "L", "F", "R", "F", "L", "F"],
        "R",
        ["F", "L", "F", "R", "F", "L", "F"],
        "R",
        ["F", "L", "F", "R", "F", "L", "F"]
    ])
)
for i, test in enumerate(tests):
    val = apply("F", test[0], test[1])
    expect = test[2]
    if val != expect:
        print("✕ Failed on test", i, val, "!=", expect)
    else:
        print("✓ Test", i)


print("== Step")
tests = (
    ( # first test
        { # rules
            "F": ["A", "B"],
            "G": ["C", "D"]
        },
        list("FRGRF"), # state
        list("ABRCDRAB") # expected
    ),
    (
        {}, # rules
        list("FRGRF"), # state
        list("FRGRF") # expected
    ),
    (
        { # rules
            "F": ["A", "B"],
        },
        list("GRG"), # state
        list("GRG") # expected
    ),
)
for i, test in enumerate(tests):
    val = step(test[0], test[1])
    expect = test[2]
    if val != expect:
        print("✕ Failed on test", i, val, "!=", expect)
    else:
        print("✓ Test", i)


print("== Compute")
tests = (
    ( # first test
        3, # depth
        { # rules
            "F": ["A", "F", "B"],
            "G": ["F"]
        },
        list("FRG"), # state
        list("AAAFBBBRAAFBB") # expected
    ),
    (
        0, # depth
        { # rules
            "F": ["A", "F", "B"],
            "G": ["F"]
        },
        list("FRG"), # state
        list("FRG") # expected
    )
)
for i, test in enumerate(tests):
    val = compute(test[0], test[1], test[2])
    expect = test[3]
    if val != expect:
        print("✕ Failed on test", i, val, "!=", expect)
    else:
        print("✓ Test", i)


print("== Flatten")
tests = (
    ([1, 2, [3, 4]], [1, 2, 3, 4]),
    ([1, 2, []], [1, 2]),
    ([], []),
    ([[1, 2], [3, 4]], [1, 2, 3, 4]),
    ([[[1], 2], 3], [1, 2, 3])
)
for i, test in enumerate(tests):
    val = flatten(test[0])
    expect = test[1]
    if val != expect:
        print("✕ Failed on test", i, val, "!=", expect)
    else:
        print("✓ Test", i)


print("== Parse")
tests = (
    ( # first test
        "files/dragon.fdl",
        {
            "start": ["F", "X"],
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
