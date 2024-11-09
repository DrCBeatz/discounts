
# Product Discount Calculator

This repository provides a Python-based tool for calculating product costs for music suppliers using discount codes. 
Music suppliers often provide discounts via specific codes rather than listing final prices, and this tool calculates 
the actual dealer costs based on those codes.

## Features

- **Apply Discounts**: Apply various discount codes to a retail price to determine the dealer cost.
- **Profit Margin Calculation**: Calculate the profit margin between retail price and cost.
- **Discount Code Determination**: Determine which discount code was used to achieve a given dealer cost.
- **Flexible Rounding**: Round numbers to the nearest specified multiple, with options for custom rounding precision.

## Files

- **discounts.py**: Main module that includes all functions for calculating dealer costs, applying discounts, and determining profit margins.
- **test files**: Separate files for testing each function, including:
  - `test_apply_discount.py`: Tests for applying discounts using predefined price brackets.
  - `test_calculate_cost.py`: Tests for calculating dealer costs using discount codes.
  - `test_calculate_discount.py`: Tests for determining discount codes based on dealer cost.
  - `test_ceil.py`: Tests for the rounding function.
  - `test_profit_margin.py`: Tests for calculating profit margins.

- **.github/workflows/run-tests.yml**: GitHub Actions workflow file for running tests on every push to the main branch.

## Installation

### Requirements

- Python 3.9+
- Pipenv (for managing dependencies)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/discount-calculator.git
   cd discount-calculator
   ```

2. Install dependencies:
   ```bash
   pipenv install --dev
   ```

3. Run the tests:
   ```bash
   pipenv run pytest
   ```

## Usage

Import the functions from `discounts.py` to integrate discount calculation and margin analysis into your own applications:

```python
from discounts import calculate_cost, apply_discount, calculate_discount, profit_margin

# Calculate dealer cost with a discount code
dealer_cost = calculate_cost(retail=100, discount="B")

# Apply a custom discount rate directly
discounted_price = apply_discount(price=100, discount=0.5)

# Determine the profit margin
margin = profit_margin(revenue=200, cost=100)
```

## Testing

This project includes extensive tests for each function using `pytest`. The GitHub Actions workflow automatically runs 
the tests on each push to the main branch, ensuring code reliability.

To manually run the tests, use:

```bash
pipenv run pytest
```

## License

This project is open source and available under the MIT License.
