import streamlit as st
import polars as pl
from src.utils import scraper_utils

# This makes the web page wider and look more professional
st.set_page_config(layout="wide")
st.title("👕 Fit-Check: Find Your Perfect Match")
st.write("Welcome! Enter your details below to find clothes that actually fit.")

# --- SIDEBAR SETTINGS ---
st.sidebar.header("Your Measurements")

# 1. Gender Selection
gender = st.sidebar.selectbox("Gender", ["Men's", "Women's"])

# 2. Source Selection (Which websites to check)
st.sidebar.header("Data Sources")
use_ebay = st.sidebar.checkbox("eBay", value=True)
use_example = st.sidebar.checkbox("Example Store", value=True)

# We put the selected sources into a list to give to our 'Brain'
selected_sources = []
if use_ebay: selected_sources.append("eBay")
if use_example: selected_sources.append("Example")

# --- MAIN AREA ---
if st.button("Find My Fit!"):
    # We call the 'Brain' we built in Step 2
    # Note: We pass 0 for waist/inseam since we simplified those for now
    results_df = scraper_utils.scrape_data(selected_sources, gender, 0, 0)
        
    if not results_df.is_empty():
        st.success(f"Found {len(results_df)} items for you!")
        # Display the table
        st.dataframe(results_df, use_container_width=True)
    else:
        st.warning("No items found matching your criteria.")
