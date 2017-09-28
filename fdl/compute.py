from step import step

def compute(depth, rules, state):
    """Repeatedly inserts rules into a state"""
    for i in range(0, depth):
        state = step(rules, state)
    return state

if __name__ == "__main__":
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
    success = True
    for i, test in enumerate(tests):
        val = compute(test[0], test[1], test[2])
        expect = test[3]
        if val != expect:
            success = False
            print("✕ Failed on test", i, val, "!=", expect)
        else:
            print("✓ Test", i)
