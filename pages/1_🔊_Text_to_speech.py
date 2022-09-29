from newspaper import Article
import nltk
from gtts import gTTS
import streamlit as st
import os
import time
from gtts.lang import tts_langs


def languages():
    langs = tts_langs()
    return langs


@st.cache(suppress_st_warning=True)
def generate_mp3_file_from_link(data, lng):
    article = Article(data)
    article.download()
    article.parse()
    nltk.download('punkt')
    article.nlp()

    mytext = article.text
    language = lng
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("article.mp3")

    # progress bar
    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.1)
        my_bar.progress(percent_complete + 1)

    # downloading
    with open('audio.mp3', 'rb') as f:
        st.download_button('Download mp3 file', f, file_name='file.mp3')


@st.cache(suppress_st_warning=True)
def generate_mp3_file_from_text(data, lng):
    mytext = data
    language = lng
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("audio.mp3")

    # progress bar
    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.05)
        my_bar.progress(percent_complete + 1)

    # downloading
    with open('audio.mp3', 'rb') as f:
        st.download_button('Download mp3 file', f, file_name='file.mp3')


def main():
    st.sidebar.success("Select project above.")
    css_path = "styles\main.css"
    abs_path = os.path.abspath(css_path)

    with open(abs_path) as f:
        st.markdown("<style>{}</style>".format(f.read()),
                    unsafe_allow_html=True)

    title = '<p style="color:White; font-size: 35px;">Convert text to speech</p>'
    st.markdown(title, unsafe_allow_html=True)

    with st.form(key="myform", clear_on_submit=True):
        set_lng = languages()
        user_article_link = st.text_input(label="Enter your link")
        user_article_text = st.text_area(label="or paste text to convert")
        language = st.selectbox(
            label="and choose your language", options=set_lng.values(), index=11)
        choosen_language = (list(set_lng.keys())[
                            list(set_lng.values()).index(language)])
        submitted = st.form_submit_button(label="Generate mp3 file")

    if submitted:
        if user_article_link and not user_article_text:
            generate_mp3_file_from_link(user_article_link, choosen_language)
        if user_article_text and not user_article_link:
            generate_mp3_file_from_text(user_article_text, choosen_language)
        if user_article_link and user_article_text:
            st.error("Select one option")
        if not user_article_link and not user_article_text:
            st.error("Nothing has been selected")


if __name__ == '__main__':
    main()
