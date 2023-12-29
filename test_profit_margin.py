# test_profit_margin.py

from discounts import profit_margin
import pytest

# Define test cases for typical use
tests = [
    (200, 100, 50.0),           # 50% profit margin
    (500, 300, 40.0),           # 40% profit margin
    (1000, 1000, 0.0),          # 0% profit margin (break-even)
    (1000, 0, 100.0),           # 100% profit margin (no cost)
]

# Define error cases
error_tests = [
    ("not a number", 100),      # Non-numeric revenue
    (500, "not a number"),      # Non-numeric cost
    (0, 100),                   # Zero revenue
]

# Test normal behavior
@pytest.mark.parametrize("revenue, cost, expected", tests)
def test_profit_margin(revenue, cost, expected):
    assert profit_margin(revenue, cost) == expected

# Test error conditions
@pytest.mark.parametrize("revenue, cost", error_tests)
def test_profit_margin_errors(revenue, cost):
    with pytest.raises(ValueError):
        profit_margin(revenue, cost)

# Run the tests
if __name__ == "__main__":
    pytest.main()
