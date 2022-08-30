from newspaper import Article
import nltk
from gtts import gTTS
import streamlit as st
import os


def generate_mp3_file_from_link(data):
    article = Article(data)
    article.download()
    article.parse()
    nltk.download('punkt')
    article.nlp()

    mytext = article.text
    language = 'pl'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("read_article.mp3")

    with open('read_article.mp3', 'rb') as f:
        st.download_button('Download mp3 file', f, file_name='file.mp3')


def generate_mp3_file_from_input(data):
    mytext = data
    language = 'pl'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("read_article.mp3")
    with open('read_article.mp3', 'rb') as f:
        st.download_button('Download mp3 file', f, file_name='file.mp3')


def main():
    css_path = "styles\main.css"
    abs_path = os.path.abspath(css_path)

    with open(abs_path) as f:
        st.markdown("<style>{}</style>".format(f.read()),
                    unsafe_allow_html=True)

    title = '<p style="color:White; font-size: 35px;">Convert text to speech</p>'
    st.markdown(title, unsafe_allow_html=True)

    with st.form(key="myform", clear_on_submit=True):
        user_article = st.text_input("Enter your link")
        user_article_text = st.text_area('or paste text to convert')
        submit_button = st.form_submit_button("Generate mp3 file")

        # TODO: add progress bar/status
        # TODO: add file uploader maybe
        # TODO: radio choice/language selectbox
        # TODO: session state

    if submit_button:
        if user_article:
            generate_mp3_file_from_link(user_article)
        elif user_article_text:
            generate_mp3_file_from_input(user_article_text)
        else:
            st.write("Error")


if __name__ == '__main__':
    main()
