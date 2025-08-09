import streamlit as st

st.set_page_config(page_title="Viva PR War Room", layout="wide")

st.title("Viva PR War Room – Scenario Tool")
st.write("Welcome! This is your live scenario planning tool.")

scenario = st.text_area("Enter a scenario")
if st.button("Analyse"):
    st.write(f"Analysis for: **{scenario}**")
    st.write("→ Here we would run the analysis logic and display insights.")
