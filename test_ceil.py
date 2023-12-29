# test_ceil.py

from discounts import ceil
import pytest

# Define test cases for typical use
tests = [
    (10.75, 1, 11),       # Typical case, round up to next whole number
    (-10.75, 1, -10),     # Negative number, round up towards 0
    (10.75, 0.5, 11),     # Non-whole multiple
    (10, 5, 10),          # No rounding needed
]

# Define  error cases
error_tests = [
    (10, 0),  # Multiple is 0, should raise ValueError
]

# Test normal behavior
@pytest.mark.parametrize("x, s, expected", tests)
def test_ceil(x, s, expected):
    assert ceil(x, s) == expected

# Test error conditions
@pytest.mark.parametrize("x, s", error_tests)
def test_ceil_errors(x, s):
    with pytest.raises(ValueError):
        ceil(x, s)

# Run the tests
if __name__ == "__main__":
    pytest.main()
