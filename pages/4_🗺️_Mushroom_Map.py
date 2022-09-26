from turtle import onclick
from webbrowser import get
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import os
from streamlit.runtime.legacy_caching import clear_cache as clear_cache


# TODO: add possiblity to add markers without coordinates, just enter street name
st.title("Mushroom Map")
st.sidebar.success("Select project above.")
css_path = "styles\main.css"
abs_path = os.path.abspath(css_path)


# ------SESSION STATE
if "mdf" not in st.session_state:
    st.session_state.mdf = pd.DataFrame(
        columns=["Label", "Latitude", "Longitude", "Quantity"])

if "lat" not in st.session_state:
    st.session_state.lat = 52.09

if "lng" not in st.session_state:
    st.session_state.lng = 19.59

with open(abs_path) as f:
    st.markdown("<style>{}</style>".format(f.read()),
                unsafe_allow_html=True)

# ------MAP
map = folium.Map(location=[52.05, 19.59], zoom_start=6)
my_marker = folium.LatLngPopup()
map.add_child(my_marker)


# ------USER INPUTS
col1, col2, col3 = st.columns([2, 0.6, 0.5])

label = col1.text_input(label="Description")
quantity = col2.number_input(label="Quantity", value=0, step=1)
with col3:
    run = st.button(label="Submit", key="Submit")
    clear = st.button(label="Clear", key="Clear")


# ------CREATING NEW DATA FRAME WITH USER PARAMETERS
df_new = pd.DataFrame({"Label": label,
                       "Latitude": st.session_state.lat,
                       "Longitude": st.session_state.lng,
                       "Quantity": quantity}, index=[label])

# ------CONCATENATE DATA FRAMES
if run:
    st.session_state.mdf = pd.concat([st.session_state.mdf, df_new], axis=0)
    st.session_state.mdf['marker_color'] = pd.cut(st.session_state.mdf['Quantity'], bins=4,
                                                  labels=['orange', 'lightred', 'red', 'darkred'])

# ------CLEARING DATA
if clear:
    st.session_state.mdf.drop(st.session_state.mdf.index, inplace=True)
    clear_cache()

#TODO: change displaying data
# ------DISPAYING USER DATA
col1, col2 = st.columns([1, 3])
with col1:
    hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """

    st.markdown(hide_table_row_index, unsafe_allow_html=True)
    st.table(
        st.session_state.mdf[["Label", "Latitude", "Longitude", "Quantity"]])
    
with col2:
    #TODO: improve displaying tooltip
    for i in range(0, len(st.session_state.mdf)):
        folium.Marker(location=[st.session_state.mdf.iloc[i]["Latitude"], st.session_state.mdf.iloc[i]
                                ["Longitude"]], popup=st.session_state.mdf.iloc[i]["Label"], tooltip=st.session_state.mdf.iloc[i]["Quantity"], icon=folium.Icon(color=st.session_state.mdf.iloc[i]['marker_color'])).add_to(map)

    output = st_folium(map, width=800, height=500)
    if (output["last_clicked"] != None):
        st.session_state.lat = output["last_clicked"]["lat"]
        st.session_state.lng = output["last_clicked"]["lng"]