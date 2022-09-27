import streamlit as st
import os


def main():
    title = '<p style="color:White; font-size: 35px;">My other projects.</p>'
    st.markdown(title, unsafe_allow_html=True)
    st.sidebar.success("Select project above.")
    css_path = "styles\main.css"
    abs_path = os.path.abspath(css_path)

    with open(abs_path) as f:
        st.markdown("<style>{}</style>".format(f.read()),
                    unsafe_allow_html=True)

    PROJECTS = {"🔗 Streamlit Twitter - download the user's tweets and ploting a chart": "https://twitter--streamlit.herokuapp.com",
                "🔗 Twitter movie notification - tells you if a movie is on TV and sends a tweet": "https://twitter.com/czy_kiler",
                "🔗 GUS Dashboard app - historical and forecast yearbook data from the Central Statistical Office": "https://pandas-streamlit.herokuapp.com",
                "🔗 Lotto - is it worth playing or not": "https://github.com/Pawel-Wojtarowicz/Python/tree/master/Lotto",
                "🔗 Password manager - GUI password manager written with tkinter": "https://github.com/Pawel-Wojtarowicz/password_manager",
                }

    st.write("---")
    for project, link in PROJECTS.items():
        st.write(f"[{project}]({link})")


if __name__ == "__main__":
    main()
