id: 685981a0c06e8f4cadc13416_documentation
summary: Currency Exchange Rates Documentation
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# Budget vs. Actual Spending Tracker Codelab

This codelab guides you through a Streamlit application designed to track your budgeted spending against your actual expenses. This application provides a clear and visual way to monitor your financial health, identify overspending, and analyze spending trends.

**Why is this application important?**

Effective budgeting is crucial for financial stability. This application simplifies the process by:

*   Providing an intuitive interface for logging budget categories and expenses.
*   Calculating budget variances to highlight areas of over or under spending.
*   Visualizing spending trends over time to help you make informed financial decisions.

**Concepts Covered:**

*   **Streamlit:**  Building interactive web applications with Python.
*   **Data Visualization:**  Using Plotly to create informative charts.
*   **Session State:**  Managing data persistence across user interactions within a Streamlit app.
*   **DataFrames:**  Utilizing Pandas DataFrames for data storage and manipulation.

## Setting Up the Environment

Duration: 00:05

Before diving into the application, ensure you have the necessary libraries installed. Open your terminal and run the following command:

```bash
pip install streamlit pandas plotly
```

This command installs Streamlit, Pandas, and Plotly, which are the core dependencies for this project.

## Understanding the Application Structure

Duration: 00:10

The application consists of three main files:

*   `app.py`: This is the main application file. It handles the overall layout, navigation, and calls the functions from the other two modules.
*   `application_pages/dashboard.py`: This module contains the code for the dashboard page, which visualizes the budget data.
*   `application_pages/data_entry.py`: This module handles the data entry page, where users can input budget categories and log expenses.

Let's examine each file in detail.

## Exploring `app.py`

Duration: 00:15

Open `app.py` in your code editor. This file serves as the entry point for the Streamlit application.

```python
import streamlit as st

st.set_page_config(page_title="Budget vs. Actual Spending", layout="wide")
#st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg") #Removed non existent image
st.sidebar.divider()
st.title("Budget vs. Actual Spending")
st.divider()

st.markdown("""
In this lab, you can track budgeted spending against actual expenses. 
Input budget categories, log actual expenses, and visualize summaries of your spending habits.

**Core Concepts:**

*   **Budget Variance:**  The difference between the budgeted amount and the actual amount spent. A negative variance indicates overspending.
*   **Percentage of Budget Spent:**  The percentage of the budget that was spent in a specific category.
*   **Trend Analysis:**  Mini line charts visualize spending trends over time using a simple moving average.
""")

# Your code starts here
page = st.sidebar.selectbox(label="Navigation", options=["Dashboard", "Data Entry"])

if page == "Dashboard":
    from application_pages.dashboard import run_dashboard
    run_dashboard()
elif page == "Data Entry":
    from application_pages.data_entry import run_data_entry
    run_data_entry()
# Your code ends

st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "Any reproduction of this demonstration "
           "requires prior written consent from QuantUniversity.")
```

Here's a breakdown of the code:

*   `st.set_page_config()`: Configures the page title and layout.  `layout="wide"` ensures the application takes up the full width of the browser window.
*   `st.sidebar`: Creates a sidebar for navigation.
*   `st.title()`: Sets the main title of the application.
*   `st.markdown()`: Displays introductory text explaining the application's purpose and core concepts.
*   `st.sidebar.selectbox()`: Creates a dropdown menu in the sidebar to switch between the "Dashboard" and "Data Entry" pages.
*   Conditional Logic: Based on the selected page, the corresponding function (`run_dashboard()` or `run_data_entry()`) from the respective module is called.
*   `st.divider()`: Adds a visual divider to the page.
*   `st.write()` and `st.caption()`: Display copyright information and a disclaimer.

## Examining `application_pages/dashboard.py`

Duration: 00:20

Open `application_pages/dashboard.py`. This module generates the dashboard, providing visual insights into your spending data.

```python
import streamlit as st
import pandas as pd
import plotly.express as px

def run_dashboard():
    st.header("Dashboard")

    # Load data from session state, if available
    if 'budget_data' not in st.session_state:
        st.session_state['budget_data'] = pd.DataFrame({
            'Category': [],
            'Budgeted': [],
            'Actual': [],
            'Date': []
        })
    
    budget_data = st.session_state['budget_data']
    
    if len(budget_data) == 0:
        st.write("No data available. Please add budget categories and log expenses in the Data Entry page.")
        return
        
    # Calculate Variance and Percentage Spent
    budget_data['Variance'] = budget_data['Budgeted'] - budget_data['Actual']
    budget_data['PercentageSpent'] = (budget_data['Actual'] / budget_data['Budgeted']) * 100

    # Summary Display (Bar Chart)
    fig = px.bar(budget_data, x="Category", y="Variance", title="Budget Variance by Category")
    st.plotly_chart(fig, use_container_width=True)

    # Metrics Display
    st.subheader("Category Performance")
    for category in budget_data['Category'].unique():
        category_data = budget_data[budget_data['Category'] == category]
        variance = category_data['Variance'].iloc[-1]
        percentage_spent = category_data['PercentageSpent'].iloc[-1]

        delta = f"{percentage_spent:.2f}%"

        if variance < 0:
            st.metric(label=category, value=f"{variance:.2f}", delta=delta, delta_color="inverse") #Red when overspending
        else:
            st.metric(label=category, value=f"{variance:.2f}", delta=delta)

    # Trend Analysis Charts
    st.subheader("Spending Trends")
    for category in budget_data['Category'].unique():
        category_data = budget_data[budget_data['Category'] == category].sort_values(by='Date')
        fig = px.line(category_data, x="Date", y="Actual", title=f"Spending Trend for {category}")
        st.plotly_chart(fig, use_container_width=True)
```

Key components of this module:

*   **Data Loading:**  It retrieves the `budget_data` DataFrame from the Streamlit session state.  If the data doesn't exist (first time the app is run), it initializes an empty DataFrame.
*   **Data Validation:** Checks if budget data exists. If not, prompts the user to enter data in the "Data Entry" page.
*   **Calculations:**
    *   Calculates the `Variance` (Budgeted - Actual).
    *   Calculates `PercentageSpent` (Actual / Budgeted * 100).
*   **Visualization:**
    *   Uses `plotly.express` to create a bar chart showing the budget variance by category.
    *   Uses `st.metric` to display key performance indicators (KPIs) for each category, including the variance and percentage spent. The `delta_color="inverse"` argument makes the delta red when overspending (negative variance).
    *   Generates line charts to visualize spending trends over time for each category.
*   `st.plotly_chart(fig, use_container_width=True)`: Renders the Plotly charts in the Streamlit app, ensuring they scale to fit the container width.

## Analyzing `application_pages/data_entry.py`

Duration: 00:20

Now, let's examine `application_pages/data_entry.py`. This module provides the user interface for entering and managing budget data.

```python
import streamlit as st
import pandas as pd
from datetime import datetime

def run_data_entry():
    st.header("Data Entry")

    # Initialize budget_data in session state if it doesn't exist
    if 'budget_data' not in st.session_state:
        st.session_state['budget_data'] = pd.DataFrame({
            'Category': [],
            'Budgeted': [],
            'Actual': [],
            'Date': []
        })

    # Budget Category Input Form
    st.subheader("Add Budget Category")
    category_name = st.text_input("Category Name")
    budgeted_amount = st.number_input("Budgeted Amount", value=0.0)
    if st.button("Add Category"):
        new_category = pd.DataFrame({
            'Category': [category_name],
            'Budgeted': [budgeted_amount],
            'Actual': [0.0],
            'Date': [datetime.now().strftime('%Y-%m-%d')]  # Use today's date for initial entry
        })
        st.session_state['budget_data'] = pd.concat([st.session_state['budget_data'], new_category], ignore_index=True)
        st.success(f"Category '{category_name}' added successfully!")

    # Expense Logging Form
    st.subheader("Log Expense")
    if len(st.session_state['budget_data']['Category'].unique()) > 0:
        category = st.selectbox("Category", st.session_state['budget_data']['Category'].unique())
        amount_spent = st.number_input("Amount Spent", value=0.0)
        date = st.date_input("Date")

        if st.button("Log Expense"):
            # Find the matching row and update the 'Actual' amount
            st.session_state['budget_data'].loc[st.session_state['budget_data']['Category'] == category, 'Actual'] += amount_spent
            st.session_state['budget_data'].loc[st.session_state['budget_data']['Category'] == category, 'Date'] = date.strftime('%Y-%m-%d')  # Update the date as well
            st.success(f"Expense logged for '{category}' on {date.strftime('%Y-%m-%d')}!")
    else:
        st.write("Please add a budget category first.")

    # Display current budget data
    st.subheader("Current Budget Data")
    st.dataframe(st.session_state['budget_data'])
```

Here's a breakdown:

*   **Session State Initialization:**  Similar to the dashboard, it initializes the `budget_data` DataFrame in the session state if it doesn't already exist.
*   **Add Budget Category Form:**
    *   `st.text_input()`: Allows the user to enter a category name.
    *   `st.number_input()`: Allows the user to enter a budgeted amount for the category.
    *   `st.button("Add Category")`: When clicked, creates a new row in the `budget_data` DataFrame with the entered category and budgeted amount.  The `Actual` amount is initialized to 0.0, and the `Date` is set to the current date.
    *   `st.success()`: Displays a success message after adding the category.
*   **Log Expense Form:**
    *   `st.selectbox()`: Allows the user to select a category from the existing categories in the `budget_data` DataFrame.
    *   `st.number_input()`: Allows the user to enter the amount spent.
    *   `st.date_input()`: Allows the user to select the date of the expense.
    *   `st.button("Log Expense")`: When clicked, updates the `Actual` amount for the selected category in the `budget_data` DataFrame.
    *   `st.success()`: Displays a success message after logging the expense.
*   **Data Display:**
    *   `st.dataframe()`: Displays the current `budget_data` DataFrame.

<aside class="positive">
    The use of <b>session state</b> is critical for maintaining data persistence across page changes in Streamlit. Without it, the data would be reset each time the user navigates between the "Dashboard" and "Data Entry" pages.
</aside>

## Running the Application

Duration: 00:05

To run the application, save all the files in the appropriate directory structure ( `app.py` in the root directory, and the two python files inside a directory named `application_pages`). Open your terminal, navigate to the directory containing `app.py`, and run the following command:

```bash
streamlit run app.py
```

This command will start the Streamlit server and open the application in your web browser.

## Using the Application

Duration: 00:15

1.  **Data Entry:** Navigate to the "Data Entry" page using the sidebar.
2.  **Add Budget Categories:** Enter a category name and a budgeted amount, and click "Add Category".  Repeat this for all your budget categories (e.g., "Rent", "Food", "Transportation").
3.  **Log Expenses:** Select a category, enter the amount spent, and select the date of the expense.  Click "Log Expense". Repeat this for all your expenses.
4.  **Dashboard:** Navigate to the "Dashboard" page using the sidebar.  You will see a bar chart visualizing the budget variance for each category, metric displays showing category performance, and line charts visualizing spending trends over time.

## Enhancements and Further Development

Duration: 00:10

This application provides a solid foundation for tracking your budget. Here are some potential enhancements:

*   **Data Persistence:** Implement data persistence using a database or file storage (e.g., CSV) to save the data between sessions. Currently, the data is lost when the Streamlit app is restarted.
*   **More Sophisticated Trend Analysis:** Implement moving averages or other statistical methods for smoother and more informative trend lines.
*   **User Authentication:** Add user authentication to allow multiple users to track their budgets separately.
*   **Customizable Date Ranges:** Allow users to select custom date ranges for the dashboard visualizations.
*   **Alerts:** Implement alerts to notify users when they are approaching or exceeding their budget in a particular category.
*   **Import/Export:** Add functionality to import and export data from/to CSV or other formats.

<aside class="positive">
    Consider using <b>Streamlit Cloud</b> for easy deployment and sharing of your application.
</aside>

## Conclusion

Duration: 00:05

Congratulations! You have successfully built a Streamlit application for tracking your budget vs. actual spending. This codelab covered the core concepts of Streamlit development, data visualization, and session state management. By understanding these concepts, you can build more sophisticated and interactive data-driven applications.  Remember to experiment with the code, explore the suggested enhancements, and tailor the application to your specific needs.
