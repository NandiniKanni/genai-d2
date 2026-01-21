import openai
import streamlit as st

openai.api_key = st.secrets["OPENAI_API_KEY"]

prompt = st.text_input("Enter prompt")

if st.button("Generate"):
    response = openai.images.generate(
        model="gpt-image-1",
        prompt=prompt,
        size="1024x1024"
    )

    image_url = response.data[0].url
    st.image(image_url)
