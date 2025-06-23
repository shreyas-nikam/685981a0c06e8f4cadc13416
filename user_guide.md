id: 685981a0c06e8f4cadc13416_user_guide
summary: Currency Exchange Rates User Guide
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# Budget vs. Actual Spending: A Codelab

This codelab guides you through a Streamlit application designed to help you track your spending against a set budget. By the end of this guide, you will understand how to input budget information, log your actual expenses, and visualize your spending habits to gain valuable insights into your financial performance. This app will help you understand key personal finance concepts.

## Understanding the Application's Core Concepts
Duration: 00:05

Before diving into the application, let's understand the core concepts it uses:

*   **Budget Variance:** This is the difference between the amount you budgeted for a specific category and the actual amount you spent.  A negative variance signals that you've overspent in that category.
*   **Percentage of Budget Spent:** This metric shows you what percentage of your budgeted amount you've actually spent in each category.
*   **Trend Analysis:** The application visualizes your spending over time, helping you identify spending patterns and trends. This is done using mini line charts that represent a simple moving average of your spending.

<aside class="positive">
<b>Why is this important?</b> Understanding these concepts is crucial for effective budgeting and financial management.  This application provides a practical way to apply these concepts to your own spending.
</aside>

## Navigating the Application: The Sidebar
Duration: 00:02

The application uses a sidebar for navigation.  You'll find a `Navigation` dropdown with two options:

*   **Dashboard:** This is where you'll see the summaries and visualizations of your budget data.
*   **Data Entry:**  This is where you'll input your budget categories and log your actual expenses.

Use the selectbox to switch between these two sections.

## Adding Budget Categories in the Data Entry Page
Duration: 00:05

Let's start by adding some budget categories:

1.  In the sidebar, select **Data Entry**.
2.  Find the **Add Budget Category** section.
3.  Enter a descriptive name for your category in the **Category Name** field (e.g., "Groceries", "Rent", "Entertainment").
4.  Enter the amount you've budgeted for this category in the **Budgeted Amount** field.
5.  Click the **Add Category** button.
6.  You will see a success message, and the category will be added to the current budget data table.

Repeat these steps to add all of your budget categories.

<aside class="positive">
<b>Tip:</b> Be specific with your categories for better tracking. Instead of "General Spending," consider breaking it down into "Dining Out," "Shopping," etc.
</aside>

## Logging Expenses in the Data Entry Page
Duration: 00:05

Now, let's log some expenses:

1.  In the **Data Entry** page, find the **Log Expense** section.
2.  Select the appropriate **Category** from the dropdown.  This dropdown will be populated with the categories you added in the previous step.
3.  Enter the **Amount Spent** in the corresponding field.
4.  Select the **Date** of the expense using the date picker.
5.  Click the **Log Expense** button.
6.  You will see a success message and the current budget data table will reflect the logged expense.

Repeat these steps to log all of your expenses.

<aside class="negative">
<b>Important:</b>  Ensure you select the correct category and date for each expense.  Incorrect entries will skew your data and affect the accuracy of your analysis.
</aside>

## Exploring the Dashboard: Visualizing Your Spending
Duration: 00:05

Now that you have some data entered, let's explore the **Dashboard**:

1.  In the sidebar, select **Dashboard**.

You should now see a dashboard containing the following elements:

*   **Budget Variance by Category (Bar Chart):** This chart visually represents the variance (Budgeted - Actual) for each category.  Bars above the line indicate that you spent less than budgeted, while bars below the line indicate overspending.
*   **Category Performance (Metrics):** This section displays key metrics for each category:
    *   The category name.
    *   The Variance amount.
    *   The Percentage Spent as a delta. The delta will be red (inverse) if you have overspent in that category.
*   **Spending Trends (Line Charts):** For each category, a line chart displays the spending trend over time, allowing you to visualize spending patterns.

<aside class="positive">
<b>Understanding the visuals:</b> Spend time analyzing the charts and metrics.  What categories are you overspending in?  Are there any noticeable trends in your spending?
</aside>

## Interpreting the Results and Taking Action
Duration: 00:03

The application provides you with the tools to understand your spending habits. Based on the information presented in the dashboard:

*   Identify areas where you are consistently overspending.
*   Analyze your spending trends to see if there are any recurring patterns.
*   Adjust your budget as needed to align with your financial goals.

By regularly using this application, you can gain better control over your finances and make informed spending decisions.
