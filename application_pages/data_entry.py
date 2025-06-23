
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
