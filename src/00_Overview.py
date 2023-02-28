import streamlit as st

from src.utils.load_data import load_data
from utils.config import LOGO_PATH, LAYOUT, INITIAL_SIDEBAR_STATE, BANIERE_PATH

st.set_page_config(
    page_title="Velib",
    page_icon=LOGO_PATH,
    layout=LAYOUT,
    initial_sidebar_state=INITIAL_SIDEBAR_STATE,
)

margin_left, image_centered, margin_right = st.columns([3, 4, 3])
image_centered.image(BANIERE_PATH, use_column_width=True)
st.title("Vélib - Localisation des stations")

data = load_data()

# TODO 1: Add information with the number of stations in Paris using st.metric (with value and labels)

open_stations_percentage = round(len(data[data["Station en fonctionnement"] == "OUI"])/len(data) * 100, 2)
st.metric(value=f"{open_stations_percentage} %", label="Stations en fonctionnement")


# TODO 2: Affichez les deux metriques sur le nombre de stations à Paris et en dehors,
#  l'une à côté de l'autre (paris, outside_paris = st.columns(2) then metric)

stations_in_paris = len(data[data["Nom communes équipées"] == "Paris"])
stations_not_in_paris = len(data[data["Nom communes équipées"] != "Paris"])

paris, outside_paris = st.columns(2)
paris.metric(value=stations_in_paris, label="Nombre de stations à Paris")
outside_paris.metric(value=stations_not_in_paris, label="Nombre de stations en dehors de Paris")


# TODO 2: Add bar with number of stations in different cities using st.bar_chart
st.subheader("Nombre de stations en dehors de Paris")
nb_stations_by_commune = data[
    data["Nom communes équipées"] != "Paris"].groupby("Nom communes équipées")[
    'Identifiant station'].count()

st.bar_chart(nb_stations_by_commune)

# TODO 4: Add headers and subheaders

# TODO 5: Add a seperate page with raw data (copy the code below, name the page 02_Raw data)

st.subheader("Les données brutes")
if st.checkbox('Afficher les données'):
    st.write(data)
