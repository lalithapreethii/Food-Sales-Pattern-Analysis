import streamlit as st

# Page setup
st.set_page_config(page_title="Food Sales Dashboard", layout="wide")

# Title
st.title("📊 Food Sales Pattern Analysis Dashboard ")

# ✅ Your Power BI embed URL
powerbi_embed_url = "https://app.powerbi.com/view?r=eyJrIjoiNmU4ZWM4OTItMGJjMC00Njg3LWJjZjctMjA0Yzc2Nzc5MDZlIiwidCI6IjgwOGNjODNlLWE1NDYtNDdlNy1hMDNmLTczYTFlYmJhMjRmMyIsImMiOjEwfQ%3D%3D"

# Embed Power BI report
st.markdown(
    f"""
    <iframe 
        title="Food Sales Dashboard"
        width="100%" 
        height="850" 
        src="{powerbi_embed_url}" 
        frameborder="0" 
        allowFullScreen="true">
    </iframe>
    """,
    unsafe_allow_html=True
)
