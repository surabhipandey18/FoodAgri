import pandas as pd
import streamlit as st

# Load your merged dataset
df = pd.read_csv("merged_crop_data.csv")

# Standardize column (remove whitespace, lowercase)
df['label'] = df['label'].str.strip().str.lower()

# Title
st.title("🌾 Crop Info Lookup")

# User input
crop_name = st.text_input("Enter Crop Name (e.g., rice, banana, maize):").strip().lower()

if crop_name:
    results = df[df['label'] == crop_name]
    if not results.empty:
        st.success(f"Details found for crop: {crop_name.capitalize()}")
        st.dataframe(results)
    else:
        st.warning("Crop not found. Please check the spelling or try another crop.")
