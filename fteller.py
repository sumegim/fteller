import streamlit as st
import requests
from datetime import datetime
import logging

default_max_tokens=100
default_temperature=0.9
default_top_p=1.0
default_presence_penalty=0.0
default_frequency_penalty=0.0

def f(prompt, 
        name, 
        max_tokens=default_max_tokens, 
        temperature=default_temperature, 
        top_p=default_top_p, 
        presence_penalty=default_presence_penalty, 
        frequency_penalty=default_frequency_penalty):
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + st.secrets["API_KEY"],
    }
    data = '{\n  "prompt": "' + prompt + '",\n  "max_tokens": 100\n}'
    data = '{\n' + \
            f'"prompt": "{prompt}",\n' + \
            f'"max_tokens": {max_tokens},\n' + \
            f'"temperature": {temperature},\n' + \
            f'"top_p": {top_p},\n' + \
            f'"presence_penalty": {presence_penalty},\n' + \
            f'"frequency_penalty": {frequency_penalty},\n' + \
            f'"echo": true\n' + \
            '}' 
    response = requests.post('https://api.openai.com/v1/engines/davinci/completions', headers=headers, data=data)
    if name != "":
        st.header(name + "!")
    else:
        name = 'guest'
    response_text = response.json()['choices'][0]['text'].replace("\n", " ")
    st.subheader(response_text)
    logging.error(f"{name},{response_text}")


advanced = st.sidebar.checkbox("Advanced settings", False)

st.write("# I will tell your fortune")

name = st.text_input("How do they call you?")

if advanced:
    prompt = st.text_input("Write anything here, I will continue", "Once upon a time, ")
    temprerature = st.slider("temperature (higher the temperature = crazyer fortune)", 0.0, 1.0, default_temperature, 0.01)
    max_tokens = st.slider("max_tokens", 1, 100, default_max_tokens, 1)
    top_p=st.slider("top_p", 0.0, 1.0, default_top_p, 0.01)
    presence_penalty=st.slider("presence_penalty", -2.0, 2.0, default_presence_penalty, 0.01)
    frequency_penalty=st.slider("frequency_penalty", -2.0, 2.0, default_frequency_penalty, 0.01)
    st.button("Tell fortune", on_click=f, args=(prompt, name, max_tokens, temprerature, top_p, presence_penalty, frequency_penalty))
else:
    prompt = st.selectbox(
        'What do you seek?',
        ('When I look into your palm, the future reveals itself to me. Next week you will', 
        'The tarot cards never lie... I can cleary see that next year you will'))
    st.button("Tell fortune", on_click=f, args=(prompt, name))



st.image("https://s3-eu-west-1.amazonaws.com/dailyartartwork/img-2017031258c5aa9390ee2_ipad")
