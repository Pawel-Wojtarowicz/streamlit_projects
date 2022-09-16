import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import os
from streamlit.runtime.legacy_caching import clear_cache as clear_cache

# TODO: add possibility to load file with coordinates
# TODO: add possiblity to add markers without coordinates, just enter street name
# TODO: add more details to markers

st.title("Mushroom Map")
st.sidebar.success("Select project above.")
css_path = "styles\main.css"
abs_path = os.path.abspath(css_path)


with open(abs_path) as f:
    st.markdown("<style>{}</style>".format(f.read()),
                unsafe_allow_html=True)

if "mdf" not in st.session_state:
    st.session_state.mdf = pd.DataFrame(
        columns=["Label", "Latitude", "Longitude"])

map = folium.Map(location=[52.32, 19.42], zoom_start=6)

col1, col2, col3 = st.columns(3)
label = col1.text_input("Label")
latitude = col2.number_input("Latitude", step=1., format="%.7f")
longitude = col3.number_input("Longitude", step=1., format="%.7f")

col1, col2 = st.columns([1, 16])
with col1:
    run = st.button("Submit", key="Submit")
with col2:
    clear = st.button("Clear", key="Clear")
    clear_cache()

df_new = pd.DataFrame({"Label": label,
                       "Latitude": latitude,
                       "Longitude": longitude}, index=[label])

if run:
    st.session_state.mdf = pd.concat([st.session_state.mdf, df_new], axis=0)

if clear:
    st.session_state.mdf.drop(st.session_state.mdf.index, inplace=True)


col1, col2, col3 = st.columns([1.1, 0.1, 3])
with col1:
    hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """

    st.markdown(hide_table_row_index, unsafe_allow_html=True)
    st.table(st.session_state.mdf)

for i in range(0, len(st.session_state.mdf)):
    folium.Marker(location=[st.session_state.mdf.iloc[i]["Latitude"], st.session_state.mdf.iloc[i]
                  ["Longitude"]], popup=st.session_state.mdf.iloc[i]["Label"]).add_to(map)

with col3:
    st.data = st_folium(map, width=1000, height=500)
