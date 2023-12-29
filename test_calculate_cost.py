# test_calculate_cost.py

from discounts import calculate_cost, discount_codes
import pytest

# Define test cases for typical use
tests = [
    (100, "A", 100 * discount_codes["A"]),  # Typical case with default discount
    (100, "B", 100 * discount_codes["B"]),  # Typical case with non-default discount
    (0, "A", 0),                            # Edge case with 0 price
    (100, "B25+5", 100 * discount_codes["B25+5"]),  # Test a compound discount
]

# Define error cases
error_tests = [
    (100, "Z"),  # Non-existent discount code
]

# Test normal behavior
@pytest.mark.parametrize("retail, discount, expected", tests)
def test_calculate_cost(retail, discount, expected):
    assert calculate_cost(retail, discount) == pytest.approx(expected, 0.01)

# Test error conditions
@pytest.mark.parametrize("retail, discount", error_tests)
def test_calculate_cost_errors(retail, discount):
    with pytest.raises(ValueError):
        calculate_cost(retail, discount)

# Run the tests
if __name__ == "__main__":
    pytest.main()
