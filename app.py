import streamlit as st
import pandas as pd
import sqlite3

st.set_page_config(page_title="Competitor Insights", layout="wide")

st.title("B2B Competitor Insights Dashboard")
st.write("This dashboard shows live data extracted from competitor sites.")

# Connect to our database
try:
    conn = sqlite3.connect('b2b_data.db')
    df = pd.read_sql('SELECT * FROM competitor_prices', conn)
    conn.close()

    # Create two columns for a better look
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Price Distribution")
        st.bar_chart(df.set_index('Title')['Price_Cleaned'])

    with col2:
        st.subheader("Inventory Status")
        # Shows how many products are available
        st.write(df['Availability'].value_counts())

    st.subheader("Full Product Catalog")
    st.dataframe(df, use_container_width=True)

except Exception as e:
    st.error("Database not found. Please run main.py first to scrape data!")