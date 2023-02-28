import streamlit as st

from src.utils.load_data import load_data
from utils.config import LAYOUT, INITIAL_SIDEBAR_STATE

st.set_page_config(
    page_title="Capaité",
    layout=LAYOUT,
    initial_sidebar_state=INITIAL_SIDEBAR_STATE,
)

st.title("Vélib - La capacité des stations")

data = load_data()

min_capacity = st.select_slider("Selectionnez la capacité minimum",
                                options=data["Capacité de la station"].sort_values().drop_duplicates())
data_filtered = data[data['Capacité de la station'] >= min_capacity]

st.subheader("La carte des stations")

# TODO 6: Add map with filtered data (st.map)
st.map(data_filtered)
