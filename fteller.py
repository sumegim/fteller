import streamlit as st
import requests

def f(prompt, name):
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + st.secrets["API_KEY"],
    }
    data = '{\n  "prompt": "' + prompt + '",\n  "max_tokens": 100\n}'
    response = requests.post('https://api.openai.com/v1/engines/davinci/completions', headers=headers, data=data)
    if name != "":
        st.header(name + "!")
    st.subheader(str(prompt + " " + response.json()['choices'][0]['text']))

st.write("# I will tell your fortune")

name = st.text_input("How do they call you?")

prompt = st.selectbox(
    'What do you seek?',
    ('When I look into your palm, the future reveals itself to me. Next week you will', 
    'The tarot cards never lie... I can cleary see that next year you will'))

st.button("Tell fortune", on_click=f, args=(prompt, name))

st.image("https://s3-eu-west-1.amazonaws.com/dailyartartwork/img-2017031258c5aa9390ee2_ipad")
