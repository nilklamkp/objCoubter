import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="Inventory Object Counter", layout="wide")

html = Path(__file__).with_name("inventory-object-counter.html").read_text(encoding="utf-8")
components.html(html, height=1600, scrolling=True)
