import streamlit as st

#https://www.webfx.com/tools/emoji-cheat-sheet/

st.set_page_config(page_title="My projects", page_icon=":desktop_computer:")

title = '<p style="color:White; font-size: 35px;">About me</p>'
st.markdown(title, unsafe_allow_html=True)


st.sidebar.success("Select project above.")


st.markdown("Hi🙋, my name is **Paweł Wojtarowicz**, and I am currently working as a System \
Administrator in a reputable company for over seven years.\
In 2021, I decided to change my career path to a Python developer. \
Since then, I have systematically learned and expanded my knowledge by \
coding various applications.")


st.write("e-mail: wojtarowicz.pawel@gmail.com  \n Github: https://github.com/Pawel-Wojtarowicz  \n LinkedIn: https://www.linkedin.com/in/pawelwojtarowicz/")


