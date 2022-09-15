import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium


st.title("Mushroom Map")
if "mdf" not in st.session_state:
    st.session_state.mdf = pd.DataFrame(
        columns=["Localization", "Latitude", "Longitude"])


# TODO: add possibility to load file with coordinates
# TODO: add possibility to clear map

map = folium.Map(location=[52.32, 19.42], zoom_start=6)
col1, col2, col3 = st.columns(3)

localization = col1.text_input("Localization")
latitude = col2.number_input("Latitude", step=1., format="%.2f")
longitude = col3.number_input("Longitude", step=1., format="%.2f")

col1, col2 = st.columns([1, 18])

with col1:
    run = st.button("Submit", key="Submit")
with col2:
    clear = st.button("Clear", key="Clear")

df_new = pd.DataFrame({"Localization": localization,
                       "Latitude": latitude,
                       "Longitude": longitude}, index=[localization])

if run:
    st.session_state.mdf = pd.concat([st.session_state.mdf, df_new], axis=0)

if clear:
    st.write("df cleared")

# st.dataframe(st.session_state.mdf)

for index, row in st.session_state.mdf.iterrows():
    folium.Marker(location=[row["Latitude"], row["Longitude"]], tooltip=[
                  "Szerokość", row["Latitude"], "Długość", row["Longitude"]], popup=row["Localization"]).add_to(map)

st.data = st_folium(map, width=800, height=500)
# st.write(f"Total Rows: {st.session_state.mdf.shape[0]}")
