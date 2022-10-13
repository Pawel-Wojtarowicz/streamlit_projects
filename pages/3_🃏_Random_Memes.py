import streamlit as st
import os
import requests
import json
from streamlit_autorefresh import st_autorefresh


def get_meme():
    url = 'https://meme-api.herokuapp.com/gimme'
    response = json.loads(requests.request("GET", url).text)
    subreddit = response["subreddit"]
    meme = response["preview"][-1]
    return subreddit, meme


def main():

    st.sidebar.success("Select project above.")
    css_path = "styles/main.css"
    abs_path = os.path.abspath(css_path)

    with open(abs_path) as f:
        st.markdown("<style>{}</style>".format(f.read()),
                    unsafe_allow_html=True)

    title = '<p style="color:White; font-size: 35px;">Random Memes every 20 seconds</p>'
    st.markdown(title, unsafe_allow_html=True)
    st.write("---")
    count = st_autorefresh(interval=20000)

    if count == 0 or count != 0:
        subreddit, meme = get_meme()

        title = f'<p style="font-family:Readex Pro; color:#d33682; font-size: 20px;">Subreddit: {subreddit}</p>'
        st.markdown(title, unsafe_allow_html=True)
        st.image(meme, width=700)


if __name__ == "__main__":
    main()
