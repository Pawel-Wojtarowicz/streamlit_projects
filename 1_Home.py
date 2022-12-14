import streamlit as st
import os
from PIL import Image

# https://www.webfx.com/tools/emoji-cheat-sheet/


def main():
    st.set_page_config(page_title="My projects",
                       page_icon=":desktop_computer:", layout="wide")

    # files
    css_file = "styles/main.css"
    css_path = os.path.abspath(css_file)
    resume_file = "assets/PWojtarowicz_CV.pdf"
    resume_path = os.path.abspath(resume_file)
    profile_picture = "assets/profile-pic.png"
    picture_path = os.path.abspath(profile_picture)

    with open(css_path) as f:
        st.markdown("<style>{}</style>".format(f.read()),
                    unsafe_allow_html=True)

    with open(resume_path, "rb") as f:
        pdf_file = f.read()

    profile_pic = Image.open(picture_path)

    st.sidebar.success("Select project above.")

    BIO = "My name is **PaweÅ**, and I am currently working as a *SYSADMIN* in a reputable company for over 7 years.\
    In 2021, I decided to change my career path to a Python developer. Since then, I have systematically learned and expanded my knowledge by \
    coding various applications."

    EMAIL = "wojtarowicz.pawel@gmail.com"
    SOCIAL_MEDIA = {"GITHUB": "http://www.github.com/Pawel-Wojtarowicz",
                    "LINKEDIN": "http://www.linkedin.com/in/pawelwojtarowicz"}

    col1, col2, col3 = st.columns(3, gap="small")
    with col2:
        st.write("#")
        st.image(profile_pic, width=330)

    with col3:
        st.title("Hi All ð")
        st.write(BIO)
        st.download_button(label="ð Download CV", data=pdf_file,
                           file_name="PWojtarowicz_CV.pdf", mime="application/octet-stream")
        st.write("ð¬", EMAIL)

    st.write("#")
    cols = st.columns(len(SOCIAL_MEDIA) + 10)
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"- [{platform}]({link})")

    st.write("---")
    st.subheader("TECHNOLOGY STACK")
    st.write(
        "- Python, Java, SQL, SQLite, Pandas, NumPy, Plotly, Flask, Streamlit, GIT, HTML, CSS, Bash, UNIX, Docker, AWS-S3, Heroku, Railway, Render")

    st.write("#")
    st.subheader("WORK HISTORY")
    st.write("---")

    title = '<p style="color:#d33682; font-size: 20px;">ð§ IT Specialist (iSeries 2nd level support)</p>'
    st.markdown(title, unsafe_allow_html=True)
    st.write("*Kyndryl Global Service Delivery Center, WrocÅaw*")
    st.write("2021/08 - Present")
    st.write("""
            - Support for the server operating system, system management software, and operating system utilities, including upgrades.
            - Analyze and diagnose bugs, performance issues, and troubleshoot problems.
            - Recommend operating system updates and configuration modifications.
            - Applying patches to the operating system.
            - Assessment of planned changes in the server environment and informing about any requirements supporting such changes.
            - Incident resolution and on-demand data recovery""")

    title = '<p style="color:#d33682; font-size: 20px;">ð§ IT Specialist (iSeries 2nd level support)</p>'
    st.markdown(title, unsafe_allow_html=True)
    st.write("*IBM Global Delivery Center, WrocÅaw*")
    st.write("2017/08 - 2021/08")
    st.write("""
            - Planning and monitoring of application deployment to update customer platforms.
            - Ensuring user satisfaction by installing enhancements, configuration, preventive maintenance, troubleshooting, and solving complex problems.
            - Monitoring and scheduling of tasks. Scheduling and backup via BRMS.
            - Examination of failed backups.
            - High quality assurance, safety compliance plan, operational procedures to maintain stability and resilience. (Keep the operating system secure)
             """)

    title = '<p style="color:#d33682; font-size: 20px;">ð§ IT Specialist (iSeries 1st level support)</p>'
    st.markdown(title, unsafe_allow_html=True)
    st.write("*IBM Global Delivery Center, WrocÅaw*")
    st.write("2015/04 - 2017/08")
    st.write("""
            - Performing daily system monitoring, verifying the integrity and availability of all hardware, server resource systems and key processes.
            - Monitor customer changes, service requests, tasks with standard incidents and tool changes to agreed deadlines and processes to maintain stability.
            - Skills required to operate the application and ensure the employee's current knowledge.
            - Responsible for sharing, advising and educating others.
            - Understand and follow the compliance requirements set out in the company's policy
             """)


if __name__ == "__main__":
    main()
