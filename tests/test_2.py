import pytest
from definition_35608eece5164d429e463dbd8cdb91c5 import calculate_variance

@pytest.mark.parametrize("category, budget_data, expected", [
    # Typical cases
    ("Rent", 
     [{"Category": "Rent", "Budgeted": 1000.0, "Actual": 900.0}], 
     100.0),
    ("Groceries", 
     [{"Category": "Groceries", "Budgeted": 500.0, "Actual": 600.0}], 
     -100.0),
    # Multiple entries with summation of budget and actual
    ("Entertainment", 
     [
        {"Category": "Entertainment", "Budgeted": 300.0, "Actual": 250.0},
        {"Category": "Entertainment", "Budgeted": 200.0, "Actual": 300.0}
     ], 
     (300.0 + 200.0) - (250.0 + 300.0)),  # 500 - 550 = -50
    # Category with zero budgeted (actual > 0)
    ("Misc", 
     [{"Category": "Misc", "Budgeted": 0.0, "Actual": 50.0}], 
     0.0 - 50.0),
    # Category not present in budget_data 
    ("Utilities", [], 0.0),
    # Budgeted and Actual both zero
    ("Empty", 
     [{"Category": "Empty", "Budgeted": 0.0, "Actual": 0.0}], 
     0.0),
    # Budgeted present but no actual recorded (assumed 0 actual)
    ("Savings", 
     [{"Category": "Savings", "Budgeted": 1000.0, "Actual": 0.0}], 
     1000.0),
    # Actual present but no budget category (budget assumed 0)
    ("Unexpected", 
     [{"Category": "Unexpected", "Budgeted": 0.0, "Actual": 300.0}], 
     -300.0),
])
def test_calculate_variance(category, budget_data, expected, monkeypatch):
    """
    We assume calculate_variance internally fetches or has access to the budget_data.
    Since we don't have actual implementation, we monkeypatch the data source or provide
    budget_data as part of a global or module attribute the function reads from.
    """
    # Setup patch for budget data storage if applicable
    # For this test, let's assume calculate_variance uses a global or module level data variable
    # monkeypatch the module's budget_data or storage attribute accordingly
    
    # We mock the module variable 'budget_data' with the test data
    import definition_35608eece5164d429e463dbd8cdb91c5 as mod
    original_data = getattr(mod, "budget_data", None)
    setattr(mod, "budget_data", budget_data)
    
    try:
        result = calculate_variance(category)
        assert isinstance(result, float)
        assert pytest.approx(result, abs=1e-6) == expected
    finally:
        # Restore original data
        setattr(mod, "budget_data", original_data)


@pytest.mark.parametrize("invalid_category", [
    None,
    123,
    12.5,
    [],
    {},
    True,
    "",
])
def test_calculate_variance_invalid_category(invalid_category):
    import definition_35608eece5164d429e463dbd8cdb91c5 as mod
    # Assign some default budget_data to avoid unrelated errors
    setattr(mod, "budget_data", [{"Category": "Test", "Budgeted": 100, "Actual": 50}])
    
    with pytest.raises((TypeError, ValueError)):
        calculate_variance(invalid_category)

@pytest.mark.parametrize("budget_data", [
    # Malformed budget_data entries
    [{"Category": "Test", "Budgeted": "100", "Actual": 50}],  # Budgeted is str
    [{"Category": "Test", "Budgeted": 100, "Actual": "50"}],  # Actual is str
    [{"Category": "Test"}],  # Missing Budgeted and Actual
    [{}],                   # Empty dict
    None,                   # None in list
])
def test_calculate_variance_malformed_budget_data(budget_data):
    import definition_35608eece5164d429e463dbd8cdb91c5 as mod
    setattr(mod, "budget_data", budget_data if budget_data is not None else [])
    
    with pytest.raises((TypeError, ValueError, KeyError)):
        calculate_variance("Test")


@pytest.mark.parametrize("category", [
    "NonExistingCategory",
    "AnotherCategory"
])
def test_calculate_variance_category_not_in_data(category):
    # Empty budget_data means no categories present
    import definition_35608eece5164d429e463dbd8cdb91c5 as mod
    setattr(mod, "budget_data", [])
    
    result = calculate_variance(category)
    assert isinstance(result, float)
    assert result == 0.0  # Expect zero variance when category not found


def test_calculate_variance_with_large_numbers():
    category = "LargeBudget"
    budget_data = [
        {"Category": category, "Budgeted": 1e9, "Actual": 5e8},
        {"Category": category, "Budgeted": 2e9, "Actual": 1.5e9}
    ]
    import definition_35608eece5164d429e463dbd8cdb91c5 as mod
    setattr(mod, "budget_data", budget_data)
    expected = (1e9 + 2e9) - (5e8 + 1.5e9)  # 3e9 - 2e9 = 1e9
    
    result = calculate_variance(category)
    assert pytest.approx(result, rel=1e-9) == expected

def test_calculate_variance_with_negative_values():
    category = "NegativeTest"
    budget_data = [
        {"Category": category, "Budgeted": -500.0, "Actual": -200.0},
        {"Category": category, "Budgeted": -300.0, "Actual": -400.0}
    ]
    import definition_35608eece5164d429e463dbd8cdb91c5 as mod
    setattr(mod, "budget_data", budget_data)
    expected = (-500.0 + -300.0) - (-200.0 + -400.0)  # -800 - (-600) = -200
    
    result = calculate_variance(category)
    assert pytest.approx(result, abs=1e-6) == expected