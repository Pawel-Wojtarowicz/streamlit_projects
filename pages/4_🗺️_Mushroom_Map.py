import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import os
from streamlit.runtime.legacy_caching import clear_cache as clear_cache
from folium.plugins import Draw


# TODO: add possibility to load file with coordinates
# TODO: add possiblity to add markers without coordinates, just enter street name

st.title("Mushroom Map")
st.sidebar.success("Select project above.")
css_path = "styles\main.css"
abs_path = os.path.abspath(css_path)


with open(abs_path) as f:
    st.markdown("<style>{}</style>".format(f.read()),
                unsafe_allow_html=True)

if "mdf" not in st.session_state:
    st.session_state.mdf = pd.DataFrame(
        columns=["Label", "Latitude", "Longitude", "Quantity"])

map = folium.Map(location=[52.32, 19.42], zoom_start=6)

my_marker = folium.LatLngPopup()
map.add_child(my_marker)  

#TODO: check another version of the map 
# Draw(export=False).add_to(map)
# output = st_folium(map, width=500, height=500)
# st.write(output)
  
col1, col2, col3, col4 = st.columns(4)
label = col1.text_input("Label")
latitude = col2.number_input("Latitude", step=1., format="%.7f")
longitude = col3.number_input("Longitude", step=1., format="%.7f")
quantity = col4.number_input("Quantinty per hour", step=1)

col1, col2 = st.columns([1, 16])
with col1:
    run = st.button("Submit", key="Submit")
with col2:
    clear = st.button("Clear", key="Clear")
    clear_cache()

df_new = pd.DataFrame({"Label": label,
                       "Latitude": latitude,
                       "Longitude": longitude,
                       "Quantity": quantity}, index=[label])

if run:
    st.session_state.mdf = pd.concat([st.session_state.mdf, df_new], axis=0)
    st.session_state.mdf['marker_color'] = pd.cut(st.session_state.mdf['Quantity'], bins=4,
                                                  labels=['orange', 'lightred', 'red', 'darkred'])

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
    st.write("My data")
    st.table(st.session_state.mdf)

for i in range(0, len(st.session_state.mdf)):
    folium.Marker(location=[st.session_state.mdf.iloc[i]["Latitude"], st.session_state.mdf.iloc[i]
                            ["Longitude"]], popup=st.session_state.mdf.iloc[i]["Label"], tooltip=st.session_state.mdf.iloc[i]["Quantity"], icon=folium.Icon(color=st.session_state.mdf.iloc[i]['marker_color'])).add_to(map)

with col3:
    st.data = st_folium(map, width=1000, height=500)
   



