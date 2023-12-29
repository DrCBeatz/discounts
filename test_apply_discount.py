# test_apply_discount.py

from discounts import apply_discount, ceil
import pytest

# Define test cases
tests = [
    (19.99, 0.5, 19.99),      # Price below the first bracket, no discount
    (20, 0.5, ceil(20 * 0.5 / 0.68, 10) - 0.01),  # Price at the first bracket
    (49.99, 0.5, ceil(49.99 * 0.5 / 0.68, 10) - 0.01),  # Just below the second bracket
    (50, 0.5, ceil(50 * 0.5 / 0.68, 5) - 0.01),   # At the second bracket
    (100, 0.5, ceil(100 * 0.5 / 0.68, 10) - 0.01),  # At the third bracket
    (150, 0.5, ceil(150 * 0.5 / 0.68, 10) - 0.01),  # Above the third bracket
]

# Test function
@pytest.mark.parametrize("price, discount, expected", tests)
def test_apply_discount(price, discount, expected):
    assert apply_discount(price, discount) == pytest.approx(expected, 0.01)

# Run the tests
if __name__ == "__main__":
    pytest.main()
