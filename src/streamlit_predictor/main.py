import streamlit as st
from streamlit_sortables import sort_items

original_items = ["A", "B", "C"]
sorted_items = sort_items(original_items)

st.write(f"Original items: {original_items}")
st.write(f"Sorted items: {sorted_items}")
