import streamlit as st
import os
from PIL import Image

# https://www.webfx.com/tools/emoji-cheat-sheet/


def main():
    st.set_page_config(page_title="My projects",
                       page_icon=":desktop_computer:")

    # files
    css_file = "styles\main.css"
    css_path = os.path.abspath(css_file)
    resume_file = "assets/resume.pdf"
    resume_path = os.path.abspath(resume_file)
    profile_picture = "assets/profile-pic.png"
    picture_path = os.path.abspath(profile_picture)

    with open(css_path) as f:
        st.markdown("<style>{}</style>".format(f.read()),
                    unsafe_allow_html=True)
    with open(resume_path, "rb") as f:
        pdf_file = f.read()

    profile_pic = Image.open(picture_path)

    # main site
    st.sidebar.success("Select project above.")

    BIO = "My name is **Paweł Wojtarowicz**, and I am currently working as a System \
    Administrator in a reputable company for over seven years.\
    In 2021, I decided to change my career path to a Python developer. \
    Since then, I have systematically learned and expanded my knowledge by \
    coding various applications."

    EMAIL = "wojtarowicz.pawel@gmail.com"
    GITHUB = "www.github.com/Pawel-Wojtarowicz"
    LINKEDIN = "www.linkedin.com/in/pawelwojtarowicz"

    PROJECTS = {"📌 Streamlit Twitter - The app allows you to retrieve Tweets from selected users on \
                given dates; Users can export them to CSV files and plot a simple chart. In the application, I used Twitter API,\
                Twitter Scraper, Streamlit, Plotly, and deployed it on Heroku": "https://twitter--streamlit.herokuapp.com",

                "Twitter movie notification - The app sends one tweet daily informing whether the movie \
                'Kiler' will air. The app connects to Twitter via an API and uses web scraping.": "https://twitter.com/czy_kiler",

                "Bricks - I've aimed to build a Flask app that allows users to choose an official lego set, retrieve its components and find \
                alternative MOCs to make. The app connects to the Rebrickable API. I used HTML, CSS and Flask to write the app and deployed it on Heroku.":
                "https://legoflask.herokuapp.com",

                "GUS Dashboard - The app gathers GUS data and plots a chart allowing users to view how the population has changed and will change over the \
                years. App filters data by gender and age groups. I used Streamlit, Pandas and Plotly and deployed it on Heroku": "https://pandas-streamlit.herokuapp.com"
                }

    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image(profile_pic, width=330)

    with col2:
        st.title("Hi All 🙋")
        st.write(BIO)
        st.download_button(label="📄 Download Resume", data=pdf_file,
                           file_name="resume.pdf", mime="application/octet-stream")
        st.write("📬", EMAIL)
        st.write("🗃️", GITHUB)
        st.write("📇", LINKEDIN)


if __name__ == "__main__":
    main()
