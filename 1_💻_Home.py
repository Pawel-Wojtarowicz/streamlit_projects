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

    PROJECTS = {"🔗 Streamlit Twitter - download user tweets ": "https://twitter--streamlit.herokuapp.com",
                "🔗 Twitter movie notification - informaing about the movie": "https://twitter.com/czy_kiler",
                "🔗 Bricks - find alternative sets": "https://legoflask.herokuapp.com",
                "🔗 GUS Dashboard app - review GUS data": "https://pandas-streamlit.herokuapp.com"
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

    st.write("#")
    st.subheader("Technological stack")
    st.write(
        "Python, Java, SQL, Pandas, Flask, Streamlit, Heroku, GIT, HTML, CSS, Bash, UNIX,")

    st.write("#")
    st.subheader("Work history")
    st.write("---")

    st.write("🚧", "**IT Specialist (iSeries 2nd level support)**")
    st.write("*Kyndryl Global Service Delivery Center, Wrocław*")
    st.write("2021/08 - Present")
    st.write("""
            - 📌Support for the server operating system, system management software, and operating system utilities, including upgrades.
            - 📌Analyze and diagnose bugs, performance issues, and troubleshoot problems.
            - 📌Recommend operating system updates and configuration modifications.
            - 📌Applying patches to the operating system.
            - 📌Assessment of planned changes in the server environment and informing about any requirements supporting such changes.
            - 📌Incident resolution and on-demand data recovery""")

    st.write("🚧", "**IT Specialist (iSeries 2nd level support)**")
    st.write("*IBM Global Delivery Center, Wrocław*")
    st.write("2017/08 - 2021/08")
    st.write("""
            - 📌 Planning and monitoring of application deployment to update customer platforms.
            - 📌 Ensuring user satisfaction by installing enhancements, configuration, preventive maintenance, troubleshooting, and solving complex problems.
            - 📌 Monitoring and scheduling of tasks. Scheduling and backup via BRMS.
            - 📌 Examination of failed backups.
            - 📌 High quality assurance, safety compliance plan, operational procedures to maintain stability and resilience. (Keep the operating system secure)
             """)

    st.write("🚧", "**IT Specialist (iSeries 1st level support)**")
    st.write("*IBM Global Delivery Center, Wrocław*")
    st.write("2015/04 - 2017/08")
    st.write("""
            - 📌 Performing daily system monitoring, verifying the integrity and availability of all hardware, server resource systems and key processes.
            - 📌 Monitor customer changes, service requests, tasks with standard incidents and tool changes to agreed deadlines and processes to maintain stability. 
            - 📌 Skills required to operate the application and ensure the employee's current knowledge.
            - 📌 Responsible for sharing, advising and educating others. 
            - 📌 Understand and follow the compliance requirements set out in the company's policy
             """)

    st.write("#")
    st.subheader("My projects")
    st.write("---")
    for project, link in PROJECTS.items():
        st.write(f"[{project}]({link})")


if __name__ == "__main__":
    main()
