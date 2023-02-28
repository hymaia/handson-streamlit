import pandas as pd
import streamlit as st


@st.cache
def load_data():
    data = pd.read_csv("data/velib-disponibilite-en-temps-reel.csv", sep=";")
    data[['LAT', 'LON']] = data['Coordonnées géographiques'].str.split(',', expand=True)
    data['LAT'] = data['LAT'].astype(float)
    data['LON'] = data['LON'].astype(float)
    return data
