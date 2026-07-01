import streamlit as st # type: ignore
import pandas as pd

st.title("Amazon Product Analyzer")

df = pd.read_csv(
    "../data/processed/clean_products.csv"
)

st.dataframe(df)

st.bar_chart(df["Price"])