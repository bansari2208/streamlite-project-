import streamlit as st
import time
from datetime import date

st.set_page_config(page_title="Food App", layout="centered")

st.title("🍕 Food App")
st.subheader("👤User Info")

# ---- NAME ----
name = st.text_input("Name", placeholder="First   Middle   Last")

city = st.selectbox("City", ["Vadodara", "Mumbai", "Valsad", "Gandhinagar"])

department = st.text_input("Department")
gender = st.radio("Gender", ["Male", "Female", "Other"], key="gender_radio")

# ---- FOOD ----
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🍔 Food Items")
    selected_food = st.multiselect(
        "Select Food Items",
        ["Sandwich", "Pizza", "Fries", "Nachos", "Salad", "Pasta"]
    )

with col2:
    st.markdown("### 🥤 Beverages")
    beverages = st.multiselect(
        "Select Beverages",
        ["Coke", "Juice", "Tea", "Coffee"]
    )

# ---- PERSONAL INFO ----
st.subheader("ℹ️ Personal Info")

st.sidebar.subheader("🍴 Order Details")
orders = st.sidebar.slider("🔢 Number of Orders", 1, 10, 1)

dob = st.date_input("Date of Birth")


# ---- AUDIO ----
st.subheader("🔉 Audio Message")
audio_message = st.audio_input("Record your message")

if audio_message:
    st.success("✅ Message recorded successfully")
    st.audio(audio_message)

# ---- FEEDBACK ----
st.subheader("👍 Feedback")
feedback = st.text_area("Feedback / Extra Comments")

# ---- AGREEMENT ----
agree = st.checkbox("I agree", key="agree")

# ---- SINGLE BUTTON ----
if st.button("🚀 Place Order", use_container_width=True):

    if not name:
        st.warning("⚠️ Please enter your name")

    elif not agree:
        st.error("❌ Please accept terms & conditions")

    elif not selected_food:
        st.warning("🍽️ Please select at least one food item")

    else:
        with st.spinner("Placing your order..."):
            time.sleep(2)

        st.success(f"🎉 Order placed successfully, {name}!")
        st.toast("🛍️ Your food is on the way 🚴‍♂️")
        st.balloons()
        st.snow()

