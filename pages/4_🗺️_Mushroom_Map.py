from streamlit.runtime.legacy_caching import clear_cache as clear_cache
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import os


title = '<p style="color:White; font-size: 35px;">Mushroom Map</p>'
st.markdown(title, unsafe_allow_html=True)
st.sidebar.success("Select project above.")
css_path = "styles/main.css"
abs_path = os.path.abspath(css_path)

# ------SESSION STATE
if "mdf" not in st.session_state:
    st.session_state.mdf = pd.DataFrame(
        columns=["Description", "Latitude", "Longitude", "Quantity"])

if "lat" not in st.session_state:
    st.session_state.lat = 52.09

if "lng" not in st.session_state:
    st.session_state.lng = 19.59

with open(abs_path) as f:
    st.markdown("<style>{}</style>".format(f.read()),
                unsafe_allow_html=True)

def convert_df(df):
   return df.to_csv().encode('utf-8')

def addplace():
    df_new = pd.DataFrame({"Description": description,
                        "Latitude": st.session_state.lat,
                        "Longitude": st.session_state.lng,
                        "Quantity": quantity}, index=[description])

    
    st.session_state.mdf = pd.concat([st.session_state.mdf, df_new], axis=0)
    st.session_state.mdf['marker_color'] = pd.cut(st.session_state.mdf['Quantity'], bins=4,
                                                labels=['orange', 'lightred', 'red', 'darkred'])
    
def cleardf():
    st.session_state.mdf.drop(st.session_state.mdf.index, inplace=True)
    clear_cache()

# ------MAP
map = folium.Map(location=[st.session_state.lat,
                 st.session_state.lng], zoom_start=6)
my_marker = folium.ClickForMarker()
map.add_child(my_marker)


# ------USER INPUTS
col1, col2, col3 = st.columns([1.5, 0.67, 1.2])
description = col1.text_input(label="Enter description")
quantity = col2.number_input(
    label="Quantity per Hour", value=0, min_value=0, step=1)

for i in range(0, len(st.session_state.mdf)):
    folium.Marker(location=[st.session_state.mdf.iloc[i]["Latitude"], st.session_state.mdf.iloc[i]
                            ["Longitude"]], popup=st.session_state.mdf.iloc[i]["Description"], tooltip=st.session_state.mdf.iloc[i]["Quantity"], icon=folium.Icon(color=st.session_state.mdf.iloc[i]['marker_color'])).add_to(map)

st.write("Please pick a point on the map")
output = st_folium(map, width=880, height=500)
if (output["last_clicked"] != None):
    st.session_state.lat = output["last_clicked"]["lat"]
    st.session_state.lng = output["last_clicked"]["lng"]

col1, col2, col3 = st.columns([1, 5, 10])
submit = col1.button("Submit", on_click = addplace, key="Submit")
clear = col2.button("Clear", on_click = cleardf, key="Clear")

# ------DISPAYING USER DATA
col1, col2 = st.columns([3, 1.5])
with col1:
    st.write("Added places")
    st.table(
        st.session_state.mdf[["Description", "Latitude", "Longitude", "Quantity"]])


st.download_button(
    "Press to Download",
    convert_df(st.session_state.mdf),
    "file.csv",
    "text/csv",
    key='download-csv'
)
