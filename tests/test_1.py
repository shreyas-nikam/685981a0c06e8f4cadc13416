import pytest
from definition_b2b50a2d4595437fa16c3f90639e0cf1 import log_expense
from datetime import datetime, date
import pandas as pd

@pytest.mark.parametrize(
    "category, amount, expense_date, expected_exception",
    [
        # Valid inputs
        ("Groceries", 150.75, datetime(2024, 6, 1), None),
        ("Rent", 1200.00, datetime(2023, 12, 31), None),
        ("Entertainment", 0.0, datetime.today(), None),  # zero amount edge case
        ("Utilities", 0.01, datetime.now(), None),  # small positive amount
        ("Misc", 9999999.99, datetime(2022, 1, 1), None),  # very large amount

        # Edge cases: invalid category types
        (None, 100.0, datetime(2024, 1, 1), TypeError),
        (1234, 100.0, datetime(2024, 1, 1), TypeError),
        ([], 50.50, datetime(2024, 1, 1), TypeError),
        ({'cat': 'Food'}, 50.50, datetime(2024, 1, 1), TypeError),
        ("", 25.00, datetime(2024, 1, 1), None),  # empty string category, may be accepted depending on implementation

        # Edge cases: invalid amount types
        ("Groceries", "100", datetime(2024, 1, 1), TypeError),
        ("Groceries", None, datetime(2024, 1, 1), TypeError),
        ("Groceries", -50.0, datetime(2024, 1, 1), ValueError),  # negative amount usually invalid
        ("Groceries", [100], datetime(2024, 1, 1), TypeError),

        # Edge cases: invalid date types
        ("Groceries", 100.0, "2024-01-01", TypeError),
        ("Groceries", 100.0, None, TypeError),
        ("Groceries", 100.0, 123456, TypeError),
        ("Groceries", 100.0, date(2024, 6, 1), None),  # date (not datetime) should be accepted if documented
    ]
)
def test_log_expense(category, amount, expense_date, expected_exception):
    """
    Test log_expense function for various edge cases and valid inputs.
    Raises expected exceptions on invalid input types and values.
    """
    # Assuming log_expense modifies some global or external DataFrame or state,
    # to avoid side effects between tests, consider mocking or resetting state.
    # Here, tests assume isolated environment or function raises exceptions before modifying state.

    if expected_exception is not None:
        with pytest.raises(expected_exception):
            log_expense(category, amount, expense_date)
    else:
        # No exception expected
        try:
            log_expense(category, amount, expense_date)
        except Exception as e:
            pytest.fail(f"Unexpected exception raised: {e}")