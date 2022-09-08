import streamlit as st
import os
import rebrick
import json
from PIL import Image


def main():
    st.sidebar.success("Select project above.")
    css_path = "styles\main.css"
    abs_path = os.path.abspath(css_path)
    rebrick.init("8e81bf52ab2d71baadb63847e48d5035")

    with open(abs_path) as f:
        st.markdown("<style>{}</style>".format(f.read()),
                    unsafe_allow_html=True)

    title = '<p style="color:White; font-size: 35px;">Alternative LEGO sets</p>'
    st.markdown(title, unsafe_allow_html=True)

    st.write("🚧", "under construction")

    with st.form(key="myform"):
        provided_lego_set = st.number_input(
            label="Provide LEGO set", value=0, step=1)
        submitted = st.form_submit_button("Find alternatives LEGO sets")

    if submitted:
        try:
            response = rebrick.lego.get_set_alternates(provided_lego_set)
            results = json.loads(response.read())
            if results['count'] == 0:
                st.error("Nie ma takiego zestawu")
            else:
                mocs = results["results"]
                names = ([d["name"] for d in mocs])
                img_url = ([d["moc_img_url"] for d in mocs])
                moc_url = ([d["moc_url"] for d in mocs])
                mocs_dict = {key: value for key, *
                             value in zip(names, img_url, moc_url)}

                for key, value in mocs_dict.items():
                    st.write(key)
                    st.write(f"[![zdj]({value[0]})]({value[1]})")

        except:
            pass


if __name__ == "__main__":
    main()
