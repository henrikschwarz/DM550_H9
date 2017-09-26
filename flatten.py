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
        if flatten(test[0]) != test[1]:
            success = False
            print("✕ Failed on test", i, flatten(test[0]), "!=", test[1])
        else:
            print("✓ Test", i)
