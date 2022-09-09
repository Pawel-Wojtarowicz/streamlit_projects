import streamlit as st
import os


def main():
    st.sidebar.success("Select project above.")
    css_path = "styles\main.css"
    abs_path = os.path.abspath(css_path)

    with open(abs_path) as f:
        st.markdown("<style>{}</style>".format(f.read()),
                    unsafe_allow_html=True)

    title = '<p style="color:White; font-size: 35px;">Send an E-Mail</p>'
    st.markdown(title, unsafe_allow_html=True)
    st.write("🚧", "under construction")


if __name__ == "__main__":
    main()
