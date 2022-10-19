import streamlit as st
import os


def main():
    title = '<p style="color:White; font-size: 35px;">My other projects.</p>'
    st.markdown(title, unsafe_allow_html=True)
    st.sidebar.success("Select project above.")
    css_path = "styles/main.css"
    abs_path = os.path.abspath(css_path)

    with open(abs_path) as f:
        st.markdown("<style>{}</style>".format(f.read()),
                    unsafe_allow_html=True)

    PROJECTS = {"🔗 Streamlit Twitter - download the user's tweets and plot bar chart": ["https://streamlit-twitter.onrender.com",
                """- In this project, I learned how to work with the Twitter API and the Twitter Scrapper, as well
                     as how to save and load data to/from files such as CSV and how to plot simple charts."""],
                "🔗 CLI NBP Currency exchanger with API": ["https://github.com/Pawel-Wojtarowicz/nbp-api", """- During the writing of this application, 
                                                       I learned how to create local databases based on previously downloaded information. 
                                                       How to process them into **.json** format and finally upload them to the S3 platform on AWS. 
                                                       With this project, I also learned about Docker and created a DockerFile for future containerization. """],
                "🔗 LEGO FLask version": ["https://lego-flask.onrender.com", "- The goal of this project was to build a simple app using framework Flask. With this app you can past every official Lego set and if alternative set exist you will recive a picture with link to him."],
                "🔗 CLI Twitter movie notification - tells you if a movie is on TV and sends a tweet": ["https://github.com/Pawel-Wojtarowicz/Python/tree/master/twitter",
                                                                                                       "- I have learned how to scrapp data from web page without API"],
                "🔗 Password manager - GUI password manager": ["https://github.com/Pawel-Wojtarowicz/password_manager",
                                                              """- In this project, I learned about the tkinter library and learned how to build a GUI application. 
                I learned the basics of cryptography to create the secret key needed to encrypt provided user passwords."""],
                "🔗 GUS Dashboard app - historical and forecast yearbook data from the Central Statistical Office": ["https://gus-dashboard.onrender.com",
                                                                                                                    "- I learned about the Pandas library and how to create simple dataframes and operate on them."],
                "🔗 CLI McDonald's - calorie counter of ordered dishes": ["https://github.com/Pawel-Wojtarowicz/Python/tree/master/McDonald's", "- I learned the basics of OOP "],
                "🔗 CLI Lotto - is it worth playing or not": ["https://github.com/Pawel-Wojtarowicz/Python/tree/master/Lotto", ""],
                }

    st.write("---")
    for project, data in PROJECTS.items():
        st.subheader(f"[{project}]({data[0]})")
        st.write(f"{data[1]}")
        st.write("---")


if __name__ == "__main__":
    main()
