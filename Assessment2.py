import streamlit as st
import pandas as pd

st.title("📁 Simple CSV Processor")

# ---------- STEP CONTROL ----------
if "step" not in st.session_state:
    st.session_state.step = 1

# ---------- STEP 1: UPLOAD ----------
if st.session_state.step == 1:
    file = st.file_uploader("Upload CSV", type="csv")

    if file:
        df = pd.read_csv(file)
        st.session_state.df = df
        st.dataframe(df.head())

        if st.button("Next"):
            st.session_state.step = 2

# ---------- STEP 2: MAPPING ----------
elif st.session_state.step == 2:
    df = st.session_state.df
    cols = df.columns

    st.write("Map Columns")

    user = st.selectbox("User ID", cols)
    date = st.selectbox("Date", cols)
    amount = st.selectbox("Amount", cols)

    st.session_state.map = {"user": user, "date": date, "amount": amount}

    if st.button("Back"):
        st.session_state.step = 1
    if st.button("Next"):
        st.session_state.step = 3

# ---------- STEP 3: TRANSFORM ----------
elif st.session_state.step == 3:
    df = st.session_state.df.copy()
    m = st.session_state.map

    # Simple validation
    try:
        df[m["amount"]] = pd.to_numeric(df[m["amount"]])
        st.success("Amount OK")
    except:
        st.error("Amount Error")

    # Simple options
    if st.checkbox("Remove Duplicates"):
        df = df.drop_duplicates()

    if st.checkbox("Fill Nulls"):
        df = df.fillna("0")

    if st.checkbox("Multiply Amount"):
        num = st.number_input("Multiplier", 1.0)
        df["New_Amount"] = df[m["amount"]] * num

    st.session_state.df = df
    st.dataframe(df.head())

    if st.button("Back"):
        st.session_state.step = 2
    if st.button("Next"):
        st.session_state.step = 4

# ---------- STEP 4: DOWNLOAD ----------
elif st.session_state.step == 4:
    df = st.session_state.df

    st.dataframe(df.head())

    csv = df.to_csv(index=False)

    st.download_button("Download CSV", csv, "output.csv")

    if st.button("Back"):
        st.session_state.step = 3