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

    PROJECTS = {"🔗 Streamlit Twitter - download the user's tweets and plot a chart": ["https://twitter--streamlit.herokuapp.com",
                """- In this project, I learned how to work with the Twitter API and the Twitter Scrapper, as well
                     as how to save and load data to/from files such as CSV and how to plot simple charts."""],
                "🔗 Twitter movie notification - tells you if a movie is on TV and sends a tweet": ["https://github.com/Pawel-Wojtarowicz/Python/tree/master/twitter", 
                "- I have learned how to scrapp data from web page without API"],
                "🔗 GUS Dashboard app - historical and forecast yearbook data from the Central Statistical Office": ["https://pandas-streamlit.herokuapp.com", 
                "- I learned about the Pandas library and how to create simple dataframes and operate on the data."],
                "🔗 Password manager - GUI password manager written with tkinter": ["https://github.com/Pawel-Wojtarowicz/password_manager",
                """- In this project, I learned about the tkinter library and learned how to build a GUI application. 
                I learned the basics of cryptography to create the secret key needed to encrypt provided user passwords."""],
                "🔗 Lotto - is it worth playing or not": ["https://github.com/Pawel-Wojtarowicz/Python/tree/master/Lotto", ""],
                }

    st.write("---")
    for project, data in PROJECTS.items():
        st.subheader(f"[{project}]({data[0]})")
        st.write(f"{data[1]}")
        st.write("---")


if __name__ == "__main__":
    main()
