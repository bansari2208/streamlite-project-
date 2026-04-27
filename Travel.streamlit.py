import streamlit as st
import pandas as pd
import numpy as np
import datetime
st.set_page_config(page_title="Travel App",layout="wide")

st.title("🌍 Investment & Travel Planner")
st.divider()
st.subheader("Plan your dream vacation and smart investments")
st.write("Welcome to the *Smart Planning Portal* ✨ where you can analyze, filter, and plan your journey.")
st.success("✅ Welcome! Your planning journey starts here.")
st.divider()

st.sidebar.title("👤User Preferences")
user_level = st.sidebar.radio("🎓Select User Level",["Beginner", "Intermediate", "Advanced"])
continent = st.sidebar.selectbox("🌍Select Target Continent",["Asia", "Europe", "Africa", "North America", "South America", "Australia"])
interests = st.sidebar.multiselect("🛠️ Select Your Interests",["💻Tech", "💰Finance", "✈️Travel", "😋Food"])
budget = st.sidebar.slider("💸Investment Budget",min_value=0, max_value=10000, value=1000)

if not interests:
    st.sidebar.warning("⚠️ Please select at least one interest")

c1, c2 = st.columns(2)

start_date = c1.date_input("📅 Project Start Date",datetime.date.today())
c2.metric("💰 Selected Budget", f"₹ {budget}")

if budget == 0:
    st.warning("⚠️ Budget is 0. Please increase it to proceed.")
st.divider()

np.random.seed(42)

data = pd.DataFrame({
    "Date": pd.date_range(start="2024-01-01", periods=10),
    "Category": np.random.choice(["Asia", "Europe", "Africa"], 10),
    "Amount": np.random.randint(100, 1000, 10),
    "Status": np.random.choice(["Pending", "Completed"], 10),
    "Growth": np.random.uniform(1.0, 5.0, 10)
})

st.subheader("📊 Financial Data")


filtered_data = data[data["Category"] == continent]

if filtered_data.empty:
    st.info("No data available for selected continent.")
else:
    st.dataframe(filtered_data, use_container_width=True)

st.divider()

name = st.text_input("Enter your name:")

if st.button("🚀 Process Report"):
    if budget > 0:
        daily_budget = budget / 30

        st.write(f"### 📌 Summary")
        st.write(f"User *{name}* wants to travel to *{continent}* starting *{start_date}*.")
        st.write(f"💰 Daily Budget: ₹ {daily_budget:.2f}")

        st.balloons()
    else:
        st.error("❌ Cannot process report with zero budget.")