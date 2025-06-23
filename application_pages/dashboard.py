
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
