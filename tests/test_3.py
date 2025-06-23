import pytest
from definition_e52f97996f3e41688ac11e8dc556aece import calculate_percentage_spent

@pytest.mark.parametrize("category, budget_data, expected", [
    # Normal cases with proper budget and actual amounts
    (
        "Rent",
        [
            {"Category": "Rent", "Budgeted": 1000.0, "Actual": 800.0},
            {"Category": "Groceries", "Budgeted": 300.0, "Actual": 350.0}
        ],
        80.0
    ),
    (
        "Groceries",
        [
            {"Category": "Rent", "Budgeted": 1000.0, "Actual": 800.0},
            {"Category": "Groceries", "Budgeted": 300.0, "Actual": 350.0}
        ],
        pytest.approx(116.6666667, 0.0001)
    ),
    (
        "Entertainment",
        [
            {"Category": "Entertainment", "Budgeted": 200.0, "Actual": 0.0}
        ],
        0.0
    ),

    # Edge case: Zero budgeted amount (should handle division, expect 0 or some convention)
    (
        "Misc",
        [
            {"Category": "Misc", "Budgeted": 0.0, "Actual": 50.0}
        ],
        0.0  # Assuming function returns 0.0 or raises error. We will check both below.
    ),

    # Edge case: Category not found (expect error)
    (
        "NonExisting",
        [
            {"Category": "Rent", "Budgeted": 1000.0, "Actual": 800.0}
        ],
        KeyError
    ),

    # Edge case: Empty budget data (expect error)
    (
        "Rent",
        [],
        KeyError
    ),

    # Test for floats with many decimals
    (
        "Utilities",
        [
            {"Category": "Utilities", "Budgeted": 123.456789, "Actual": 100.123456}
        ],
        pytest.approx((100.123456 / 123.456789) * 100, 0.0001)
    ),

    # Edge case: Negative actual spending (possible refunds or corrections)
    (
        "Refund",
        [
            {"Category": "Refund", "Budgeted": 100.0, "Actual": -50.0}
        ],
        -50.0
    ),

    # Edge case: Negative budgeted amount (invalid data, expect error or specific handling)
    (
        "InvalidBudget",
        [
            {"Category": "InvalidBudget", "Budgeted": -100.0, "Actual": 50.0}
        ],
        ValueError
    ),

    # Edge case: Non-string category input (invalid, expect TypeError)
    (
        123,
        [
            {"Category": "Rent", "Budgeted": 1000.0, "Actual": 800.0}
        ],
        TypeError
    ),

    # Edge case: None as category (invalid, expect TypeError or ValueError)
    (
        None,
        [
            {"Category": "Rent", "Budgeted": 1000.0, "Actual": 800.0}
        ],
        TypeError
    )
])
def test_calculate_percentage_spent(category, budget_data, expected):
    """
    Test calculate_percentage_spent for various input categories and budget_data.

    Note: As the original function stub does not define an API for budget data,
    this test assumes the function or environment provides a way to set/access
    budget and actual amounts for categories. Here, we emulate it by patching or
    monkeypatching inside the test if needed.

    In practice, the actual implementation details of calculate_percentage_spent
    would influence how to prepare the data and call this function.
    """

    # Prepare a way to inject or mock budget_data access
    # Since we don't have the actual module implementation, we set a global or attribute.

    # Using a monkeypatch or patch for budget data is ideal, but here we simulate:
    import builtins

    # Backup original attribute if exists
    orig_attr = getattr(definition_e52f97996f3e41688ac11e8dc556aece, "budget_data", None)
    try:
        setattr(definition_e52f97996f3e41688ac11e8dc556aece, "budget_data", budget_data)

        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                calculate_percentage_spent(category)
        else:
            result = calculate_percentage_spent(category)
            # Because of floating point calculations, use approx for floats
            if isinstance(expected, float) or isinstance(expected, pytest.approx.__class__):
                assert pytest.approx(result, rel=1e-4) == expected
            else:
                assert result == expected
    finally:
        # Restore original attribute
        if orig_attr is None:
            delattr(definition_e52f97996f3e41688ac11e8dc556aece, "budget_data")
        else:
            setattr(definition_e52f97996f3e41688ac11e8dc556aece, "budget_data", orig_attr)