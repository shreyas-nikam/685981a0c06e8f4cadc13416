
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
