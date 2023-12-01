import requests
import streamlit as st

url = 'https://api.giphy.com/v1/gifs/random'
api_key = st.secrets.GIPHY.key

gif = st.text_input('Choose your giphy...', 'cat')

params = {
    'api_key':api_key,
    'tag':gif
}
response = requests.get(url, params=params).json()

st.write(f"<iframe src={response['data']['embed_url']}>", unsafe_allow_html=True)
