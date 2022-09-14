import streamlit as st
import pandas as pd

st.title("Mushroom Map")
if "mdf" not in st.session_state:
    st.session_state.mdf = pd.DataFrame(
        columns=["Localization", "Latitude", "Longitude"])

col1, col2, col3 = st.columns(3)

localization = col1.text_input("Localization")
latitude = col2.text_input("Latitude")
longitude = col3.text_input("Longitude")

run = st.button('Submit')

df_new = pd.DataFrame({"Localization": localization,
                       "Latitude": latitude,
                       "Longitude": longitude}, index=[0])

if run:
    st.session_state.mdf = pd.concat([st.session_state.mdf, df_new], axis=0)
    st.dataframe(st.session_state.mdf)

st.write(f"Total Rows: {st.session_state.mdf.shape[0]}")
