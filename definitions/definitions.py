
from typing import Optional

_categories = set()

def add_category(category_name: Optional[str]) -> None:
    """
    Adds a new budget category to the internal set of budget categories.

    Args:
        category_name (str): The name of the budget category to add.

    Raises:
        TypeError: If category_name is not a string.
        ValueError: If category_name is empty or whitespace only.
        ValueError: If category_name already exists.
    """
    if not isinstance(category_name, str):
        raise TypeError("Category name must be a string.")
    name = category_name.strip()
    if not name:
        raise ValueError("Category name cannot be empty or whitespace.")
    if name in _categories:
        raise ValueError(f"Category '{name}' already exists.")
    _categories.add(name)

def reset_categories() -> None:
    """Resets the internal category store, used for testing setup/teardown."""
    _categories.clear()


from typing import Optional

_categories = set()

def add_category(category_name: Optional[str]) -> None:
    """
    Adds a new budget category to the internal set of budget categories.

    Args:
        category_name (str): The name of the budget category to add.

    Raises:
        TypeError: If category_name is not a string.
        ValueError: If category_name is empty or whitespace only.
        ValueError: If category_name already exists.
    """
    if not isinstance(category_name, str):
        raise TypeError("Category name must be a string.")
    name = category_name.strip()
    if not name:
        raise ValueError("Category name cannot be empty or whitespace.")
    if name in _categories:
        raise ValueError(f"Category '{name}' already exists.")
    _categories.add(name)

def reset_categories() -> None:
    """Resets the internal category store, used for testing setup/teardown."""
    _categories.clear()


from datetime import datetime, date
from typing import Union
import pandas as pd

_budget_data = pd.DataFrame(columns=["category", "amount", "date"])

def log_expense(category: str, amount: float, date_: Union[datetime, date]) -> None:
    """
    Logs an expense record in the budget data storage.

    Args:
        category (str): The budget category for the expense.
        amount (float): The amount spent (must be non-negative).
        date_ (datetime or date): The date when the expense occurred.

    Raises:
        TypeError: If any argument is of incorrect type.
        ValueError: If amount is negative.
    """
    if not isinstance(category, str):
        raise TypeError("category must be a string")
    if not (isinstance(amount, (float, int)) and not isinstance(amount, bool)):
        raise TypeError("amount must be a float or int")
    if amount < 0:
        raise ValueError("amount must be non-negative")
    if not isinstance(date_, (datetime, date)):
        raise TypeError("date must be a datetime or date instance")

    global _budget_data
    _budget_data = pd.concat([
        _budget_data,
        pd.DataFrame([{"category": category, "amount": float(amount), "date": pd.Timestamp(date_)}])
    ], ignore_index=True)


from datetime import datetime, date
from typing import Union
import pandas as pd

_budget_data = pd.DataFrame(columns=["category", "amount", "date"])

def log_expense(category: str, amount: float, date_: Union[datetime, date]) -> None:
    """
    Logs an expense record in the budget data storage.

    Args:
        category (str): The budget category for the expense.
        amount (float): The amount spent (must be non-negative).
        date_ (datetime or date): The date when the expense occurred.

    Raises:
        TypeError: If any argument is of incorrect type.
        ValueError: If amount is negative.
    """
    if not isinstance(category, str):
        raise TypeError("category must be a string")
    if not (isinstance(amount, (float, int)) and not isinstance(amount, bool)):
        raise TypeError("amount must be a float or int")
    if amount < 0:
        raise ValueError("amount must be non-negative")
    if not isinstance(date_, (datetime, date)):
        raise TypeError("date must be a datetime or date instance")

    global _budget_data
    _budget_data = pd.concat([
        _budget_data,
        pd.DataFrame([{"category": category, "amount": float(amount), "date": pd.Timestamp(date_)}])
    ], ignore_index=True)


from typing import List, Dict, Union

budget_data: List[Dict[str, Union[str, float, int, None]]] = []

def calculate_variance(category: str) -> float:
    """
    Calculates the budget variance for a specified budget category.

    The variance is computed as the sum of Budgeted amounts minus the sum of Actual amounts
    for all entries matching the given category in the global budget_data.

    Args:
        category (str): The budget category to calculate variance for.

    Returns:
        float: The variance value (BudgetedAmount - ActualAmount) showing overspending or underspending.

    Raises:
        TypeError: If category is not a non-empty string or budget_data entries are malformed.
        ValueError: If category is an empty string.
        KeyError: If budget_data entries lack required keys.
    """
    if not isinstance(category, str):
        raise TypeError("category must be a string")
    if not category:
        raise ValueError("category cannot be empty")
    if not isinstance(budget_data, list):
        raise TypeError("budget_data must be a list")

    budget_sum = 0.0
    actual_sum = 0.0
    found = False

    for entry in budget_data:
        if not isinstance(entry, dict):
            raise TypeError("Each entry in budget_data must be a dict")
        # Validate required keys presence
        if not all(k in entry for k in ("Category", "Budgeted", "Actual")):
            raise KeyError("Each entry must contain 'Category', 'Budgeted', and 'Actual' keys")

        cat = entry["Category"]
        bud = entry["Budgeted"]
        act = entry["Actual"]

        if not isinstance(cat, str):
            raise TypeError("Category value must be a string")
        if cat != category:
            continue

        if not isinstance(bud, (int, float)):
            raise TypeError("Budgeted value must be numeric")
        if not isinstance(act, (int, float)):
            raise TypeError("Actual value must be numeric")

        budget_sum += float(bud)
        actual_sum += float(act)
        found = True

    return float(budget_sum - actual_sum) if found else 0.0


from typing import Any, Dict, List


def calculate_percentage_spent(category: str) -> float:
    """
    Calculates the percentage of the budget spent in the specified category.

    Expects a list of budget dictionaries injected as 'budget_data' attribute on this function:
    [{'Category': str, 'Budgeted': float, 'Actual': float}, ...]

    Args:
        category (str): The budget category to calculate the percentage for.

    Returns:
        float: The percentage of budget spent, computed as (ActualAmount / BudgetedAmount) * 100.

    Raises:
        TypeError: If category is not a string.
        KeyError: If the category is not found or budget data is empty.
        ValueError: If the budgeted amount is negative or budgeted/actual are not numeric.
    """
    if not isinstance(category, str):
        raise TypeError("Category must be a string")

    budget_data: List[Dict[str, Any]] = getattr(calculate_percentage_spent, "budget_data", None)
    if not budget_data:
        raise KeyError("Budget data is empty or not set")

    for item in budget_data:
        if item.get("Category") == category:
            budgeted = item.get("Budgeted")
            actual = item.get("Actual")

            if not isinstance(budgeted, (int, float)):
                raise ValueError("Budgeted amount must be numeric")
            if not isinstance(actual, (int, float)):
                raise ValueError("Actual amount must be numeric")
            if budgeted < 0:
                raise ValueError("Budgeted amount cannot be negative")
            if budgeted == 0:
                return 0.0

            return (actual / budgeted) * 100

    raise KeyError(f"Category '{category}' not found in budget data")


from typing import Optional
import pandas as pd
import plotly.graph_objs as go


def _get_budget_data_for_category(category: str) -> pd.DataFrame:
    """
    Simulates retrieval of budget data filtered by category (case-insensitive, stripped).

    Args:
        category (str): Category name to filter by.

    Returns:
        pd.DataFrame: DataFrame with columns ['Category', 'Budgeted', 'Actual', 'Date'] filtered by category.
                      Returns empty DataFrame if no match or empty category.
    """
    sample_data = pd.DataFrame({
        "Category": ["Groceries"] * 5 + ["Utilities"] * 3 + ["Rent", "Entertainment"],
        "Budgeted": [100] * 5 + [50] * 3 + [1200, 200],
        "Actual": [90, 110, 95, 85, 100, 45, 55, 60, 1150, 180],
        "Date": pd.to_datetime([
            "2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04", "2023-01-05",
            "2023-02-01", "2023-02-08", "2023-02-15",
            "2023-03-01", "2023-03-03"
        ])
    })
    cat = category.strip().casefold()
    if not cat:
        return pd.DataFrame(columns=sample_data.columns)
    return sample_data[sample_data["Category"].str.casefold() == cat].copy()


def create_trend_chart(category: Optional[str]) -> go.Figure:
    """
    Creates a mini line chart visualizing spending trends over time for a given category.

    Args:
        category (str): The budget category for which to generate the trend chart.

    Returns:
        go.Figure: Plotly figure object showing actual and smoothed spending trends.

    Raises:
        TypeError: If category is not a string.
    """
    if not isinstance(category, str):
        raise TypeError("Category must be a string")

    cat = category.strip()

    df = _get_budget_data_for_category(cat)

    fig = go.Figure()
    fig.update_layout(
        template="plotly_white",
        height=300,
        margin=dict(l=30, r=30, t=40, b=30),
        legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
        xaxis_title="Date",
        yaxis_title="Amount",
        title=f"Spending Trend: '{cat or '(empty)'}'"
    )

    if df.empty or "Actual" not in df.columns or "Date" not in df.columns:
        fig.add_annotation(
            text="No data available",
            xref="paper", yref="paper",
            showarrow=False,
            font=dict(size=14, color="gray")
        )
        return fig

    df = df.sort_values("Date")
    df["Smoothed"] = df["Actual"].rolling(window=3, min_periods=1).mean()

    fig.add_trace(go.Scatter(
        x=df["Date"], y=df["Actual"],
        mode="lines+markers",
        name="Actual",
        line=dict(color="blue", width=2),
        marker=dict(size=6)
    ))

    fig.add_trace(go.Scatter(
        x=df["Date"], y=df["Smoothed"],
        mode="lines",
        name="Smoothed",
        line=dict(color="orange", width=2, dash="dash")
    ))

    return fig
