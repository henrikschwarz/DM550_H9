from apply import apply
from flatten import flatten

def step(rules, state):
    """Takes a state and a list of rules, applies rules to all states"""
    for ruleName, ruleDef in rules.items():
        state = apply(ruleName, ruleDef, state)

    return flatten(state)

if __name__ == "__main__":
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
    success = True
    for i, test in enumerate(tests):
        val = step(test[0], test[1])
        expect = test[2]
        if val != expect:
            success = False
            print("✕ Failed on test", i, val, "!=", expect)
        else:
            print("✓ Test", i)
