def flatten(nested_list):
    """Flattens a list"""
    flattened = []
    for val in nested_list:
        if isinstance(val, list):
            flattened.extend(flatten(val))
        else:
            flattened.append(val)
    return flattened

if __name__ == "__main__":
    tests = (
        ([1, 2, [3, 4]], [1, 2, 3, 4]),
        ([1, 2, []], [1, 2]),
        ([], []),
        ([[1, 2], [3, 4]], [1, 2, 3, 4]),
        ([[[1], 2], 3], [1, 2, 3])
    )
    success = True
    for i, test in enumerate(tests):
        val = flatten(test[0])
        expect = test[1]
        if val != expect:
            success = False
            print("✕ Failed on test", i, val, "!=", expect)
        else:
            print("✓ Test", i)
