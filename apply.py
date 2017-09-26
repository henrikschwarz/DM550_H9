# overwrites built-in :(
def apply(ruleName, ruleDef, state):
    """Replaces every occurence of a rule in a state with the rules definition"""
    return list(map(
        lambda key: ruleDef if key == ruleName else key,
        state
    ))

if __name__ == "__main__":
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
    success = True
    for i, test in enumerate(tests):
        val = apply("F", test[0], test[1])
        expect = test[2]
        if val != expect:
            success = False
            print("✕ Failed on test", i, val, "!=", expect)
        else:
            print("✓ Test", i)
