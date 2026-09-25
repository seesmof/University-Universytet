def f(x: int) -> int:
    return x * 2


tests = [
    (2, 4),
    (4, 8),
    (10, 20),
]
for test in tests:
    test_input, expected_output = test
    output = f(test_input)
    assert output == expected_output, f"Failed for {test_input}."
print("All tests ran well.")
