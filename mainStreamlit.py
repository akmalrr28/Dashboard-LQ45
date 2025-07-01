import streamlit as st
import pandas as pd
import pygwalker as pyg
import streamlit.components.v1 as components

# Set page layout
st.set_page_config(page_title="Visualisasi Saham", layout="wide")

# Tambahkan komponen Streamlit
st.title("📊 Dashboard Saham")
st.markdown("Gunakan visualisasi interaktif dengan PyGWalker")

# Load data
df = pd.read_csv("./Cleaned/cleaned_saham_data.csv")

# Konversi pygwalker jadi HTML
html = pyg.to_html(df)

# Tampilkan dalam Streamlit sebagai komponen HTML
components.html(html, height=1000, scrolling=True)
