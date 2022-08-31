from newspaper import Article
import nltk
from gtts import gTTS
import streamlit as st
import os
import time


@st.cache(suppress_st_warning=True)
def generate_mp3_file_from_link(data):
    article = Article(data)
    article.download()
    article.parse()
    nltk.download('punkt')
    article.nlp()

    mytext = article.text
    language = 'pl'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("article.mp3")


    #progress bar
    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.1)
        my_bar.progress(percent_complete + 1)
        
    #downloading
    with open('article.mp3', 'rb') as f:
        st.download_button('Download mp3 file', f, file_name='file.mp3')


@st.cache(suppress_st_warning=True)
def generate_mp3_file_from_input(data):
    mytext = data
    language = 'pl'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("article.mp3")

    #progress bar
    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.05)
        my_bar.progress(percent_complete + 1)
        
    #downloading
    with open('article.mp3', 'rb') as f:
        st.download_button('Download mp3 file', f, file_name='file.mp3')

#form logic
def check_form(user_article_link, user_article_input):
    if user_article_link != "" and user_article_input != "":
        st.error("Select only one form")
    elif user_article_link != "":
        generate_mp3_file_from_link(user_article_link)
    else:
        generate_mp3_file_from_input(user_article_input)


def main():
    css_path = "styles\main.css"
    abs_path = os.path.abspath(css_path)

    with open(abs_path) as f:
        st.markdown("<style>{}</style>".format(f.read()),
                    unsafe_allow_html=True)

    title = '<p style="color:White; font-size: 35px;">Convert text to speech</p>'
    st.markdown(title, unsafe_allow_html=True)

    with st.form(key="myform"):
        user_article_link = st.text_input("Enter your link")
        user_article_input = st.text_area('or paste text to convert')
        submitted = st.form_submit_button("Generate mp3 file")

    if submitted:
        check_form(user_article_link, user_article_input)


if __name__ == '__main__':
    main()


# TODO: add file uploader maybe
# TODO: radio choice/language selectbox
