import streamlit as st
import requests
import pandas as pd
import plotly.express as px

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="AI Expense Tracker", layout="centered")

st.title("💸 AI Expense Tracker")

# --- Form Input ---
with st.form("expense_form"):
    name = st.text_input("Expense Name")
    amount = st.number_input("Amount ($)", min_value=0.01, format="%.2f")
    category = st.selectbox("Category", ["Food", "Transport", "Shopping", "Bills", "Other"])
    submitted = st.form_submit_button("Add Expense")

    if submitted:
        if name and amount:
            response = requests.post(f"{API_URL}/expenses", json={
                "name": name,
                "amount": amount,
                "category": category
            })
            if response.status_code == 200:
                st.success("Expense added successfully!")
            else:
                st.error("Failed to add expense.")
        else:
            st.warning("Please fill all fields.")

st.markdown("---")

# --- Expense Table ---
st.subheader("📊 Expense Summary")

response = requests.get(f"{API_URL}/expenses")
if response.status_code == 200:
    data = response.json()
    if data:
        df = pd.DataFrame(data)
        st.dataframe(df[["name", "amount", "category"]])

        # --- Pie Chart ---
        fig = px.pie(df, names="category", values="amount", title="Expenses by Category")
        st.plotly_chart(fig)
    else:
        st.info("No expenses recorded yet.")
else:
    st.error("Failed to fetch expenses.")
