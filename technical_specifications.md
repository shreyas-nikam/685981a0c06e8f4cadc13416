
# Technical Specifications for Budget vs. Actual Spending Dashboard Streamlit Application

## Overview
This document outlines the technical specifications for a Streamlit application designed to help users track their budgeted spending against their actual expenses. The application will allow users to input budget categories, log actual expenses, and view summaries of their spending habits.  It is related to budgeting, which is the practice of planning income and expenses in advance. By contrasting expected vs. real spending, users see how well they stick to their financial goals, reinforcing the importance of proactive money management.

## Step-by-Step Development Process
1.  **Set up Streamlit Environment:** Ensure Streamlit is installed (`pip install streamlit`). Create a new Python file (e.g., `budget_dashboard.py`) and import the necessary libraries (Streamlit, Pandas, etc.).
2.  **Define Data Structures:** Determine the data structures needed to store budget categories and expenses (e.g., a Pandas DataFrame).
3.  **Implement Input Forms:** Create Streamlit input forms for users to define budget categories and log expenses, using Streamlit widgets like `st.text_input` and `st.number_input`.
4.  **Implement Data Storage:**  Add functions to store the data entered by the user. Use session state in Streamlit to persist values between user interactions.
5.  **Calculate Summaries:** Write functions to calculate the difference between budgeted and actual amounts for each category.
6.  **Implement Visualizations:** Use Streamlit's charting capabilities (e.g., `st.bar_chart`, `st.line_chart`) to display summaries and trend analyses.
7.  **Implement Alerts:** Add logic to highlight overspending categories in red.
8.  **Implement Trend Analysis:** Implement mini line charts for each category to visualize spending trends over time.
9.  **Develop User Interface:** Organise all Streamlit input forms, summaries, visualizations and alerts into a clean, user-friendly one-page design.
10. **Add Documentation:** Add inline documentation and tooltips using Streamlit's help features (`st.help`) to guide the user through data exploration.

## Core Concepts and Mathematical Foundations

### Budget Variance Formula
The budget variance is the difference between the budgeted amount and the actual amount spent. It is calculated as:
$$
Variance = BudgetedAmount - ActualAmount
$$
Where:
- $Variance$: Budget Variance
- $BudgetedAmount$: Amount allocated in the budget
- $ActualAmount$: Amount actually spent

This formula shows whether a budget category is overspent (negative variance) or underspent (positive variance).

### Percentage of Budget Spent
This calculates the percentage of the budget that was spent in a specific category.
$$
PercentageSpent = rac{ActualAmount}{BudgetedAmount} * 100
$$
Where:
- $PercentageSpent$: Percentage of the budget spent.
- $ActualAmount$: Amount actually spent.
- $BudgetedAmount$: Amount allocated in the budget.

This formula provides a relative measure of spending compared to the allocated budget.

### Time Series Analysis
Mini line charts visualising trend of spending will utilise time series data. For a given budget category, a simple moving average will be employed to smooth out fluctuations and identify a trend.
$$
SMA_{t} = rac{\sum_{i=t-n+1}^{t} P_i}{n}
$$
Where:
- $SMA_t$: Simple Moving Average at time $t$
- $P_i$: Data point at time $i$
- $n$: Number of periods in the moving average

This calculation smooths the data to make trends clearer.

## Required Libraries and Dependencies

*   **Streamlit (version >= 1.0):** Used for creating the user interface and handling user interactions.
*   **Pandas (version >= 1.0):**  Used for data manipulation and storage.
*   **Plotly (Optional):** To improve chart interactivity and design

```python
import streamlit as st
import pandas as pd
import plotly.express as px #optional
```

## Implementation Details

### Data Structures

*   `budget_categories`: A list of strings representing the budget categories (e.g., `['Rent', 'Groceries', 'Entertainment']`).
*   `budget_data`: A Pandas DataFrame storing the following information:
    *   `Category` (string): Budget category.
    *   `Budgeted` (float): Budgeted amount for the category.
    *   `Actual` (float): Actual amount spent for the category.
    *   `Date` (datetime): Date of the transaction

### Functions

*   `add_category(category_name)`: Adds a new category to the `budget_categories` list.
*   `log_expense(category, amount, date)`: Logs an expense in the `budget_data` DataFrame.
*   `calculate_variance(category)`: Calculates the budget variance for a given category.
*   `calculate_percentage_spent(category)`: Calculates the percentage of the budget spent in a given category.
*   `create_trend_chart(category)`: Creates a mini line chart showing spending trends for a given category over time.

### Alerts
Overspending will be indicated when the `Variance` calculated using the `Budget Variance Formula` is less than zero. These categories will be highlighted in red using `st.markdown` and custom CSS.

## User Interface Components

*   **Budget Category Input Form:**
    *   `st.text_input("Category Name")`:  For entering the name of a new budget category.
    *   `st.button("Add Category")`:  To add the new category to the list.
    *   `st.number_input("Budgeted Amount")`: For adding the budgeted amount for the new category.
*   **Expense Logging Form:**
    *   `st.selectbox("Category", budget_categories)`:  A dropdown to select the budget category for the expense.
    *   `st.number_input("Amount Spent")`:  For entering the amount spent.
    *   `st.date_input("Date")`: To record the date of the expense.
    *   `st.button("Log Expense")`:  To log the expense.
*   **Summary Display:**
    *   `st.bar_chart(data=summary_data, x="Category", y="Variance")`: A bar chart showing the budget variance for each category.
    *   `st.metric(label=category, value=variance, delta=percentage_spent)`: Metrics displaying each category's variance and percentage spent.
*   **Trend Analysis Charts:**
    *   `st.line_chart(data=category_data, x="Date", y="Amount")`: Mini line charts showing the spending trend for each category over time.



### Appendix Code

```code
1+ sa
f
1+
Sd
1) -1 = (1+10%) ×
f
1+5%
-1~10% +5%-2% ≈ 13%

%ARAUD ≈ %A SAUD + %A PHKD-%∆PAUD ≈ +5% +5% -2% ≈ +8%
HKD
HKD

1.  15885 +
(-
+80.9
10,000
=
1.  15885+ 0.00809
=
2.  16694

1.  15885+ 0.00809
2.  15885

3.  15885
= (1.16694) 1 = +0.698%
4.  15885

5.  6535 (1.05
=
6.  0273

F₁= Sfid (1+1)

if-id
Ffld-Sfid = Sfid 1+ist

(;
666,326,1187 +0.03003300
666,326,1184 326,111 +0.02003300
9.  6555 (326,111
FTM - 5, 10 - 1,10
=
1.  6555 (326,111 326,111
Ffid-Sfid =
1.  6555
(
27,523,788 +0.030076-10761
1.  020027,523,788
= 0.0014

1.  6555
(
27,523,788
27,523,78800 - 0,127 +0.030076-10761
2.  020027,523,788
Fid-Spa
1.  8752 + 5-14-14
2.  9.23 25

```