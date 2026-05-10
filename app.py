import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(page_title="SatOrbit Analyzer", page_icon="📡", layout="wide")

# Standard Cleanup CSS
st.markdown("""
    <style>
        #MainMenu, footer, header { visibility: hidden; }
        .block-container { padding: 0px; margin: 0px; max-width: 100%; }
        iframe { display: block; width: 100%; border: none; }
    </style>
""", unsafe_allow_html=True)

def render_app(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            html_data = f.read()
            
            # This script calculates the exact height of your content
            # so the "box" isn't bigger than the app itself.
            components.html(html_data, height=1000, scrolling=True)
    else:
        st.error("File not found.")

if __name__ == "__main__":
    render_app("satellite-analyzer.html")
