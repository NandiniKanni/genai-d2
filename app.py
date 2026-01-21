import streamlit as st
from PIL import Image
from io import BytesIO
import openai

st.title("🖼️ Text to Image using OpenAI DALL·E")

prompt = st.text_input("Enter prompt:")

openai.api_key = st.secrets["OPENAI_API_KEY"]

if st.button("Generate"):
    if prompt.strip() == "":
        st.error("Please enter a prompt!")
    else:
        with st.spinner("Generating..."):
            response = openai.images.generate(
    model="gpt-image-1",
    prompt=prompt,
    size="1024x1024"
    )

            image_url = response['data'][0]['url']
            st.image(image_url, caption="Generated Image", use_column_width=True)



