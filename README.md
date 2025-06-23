
# Budget vs. Actual Spending Dashboard

This Streamlit application allows users to track their budgeted spending against their actual expenses. 
Users can input budget categories, log actual expenses, and view summaries of their spending habits.

## Features

*   **Data Entry:** Add budget categories and log expenses.
*   **Dashboard:** Visualize budget variance and spending trends.
*   **Interactive Charts:** Use Plotly for interactive visualizations.
*   **Alerts:** Overspending categories are highlighted in red.

## How to Run

1.  Clone the repository.
2.  Install the required dependencies: `pip install -r requirements.txt`
3.  Run the application: `streamlit run app.py`

## Docker

To run the application in a Docker container:

1.  Build the image: `docker build -t budget-dashboard .`
2.  Run the container: `docker run -p 8501:8501 budget-dashboard`

