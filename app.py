import streamlit as st
import requests
from PIL import Image
from io import BytesIO

st.title("🖼️ Text-to-Image (HF Inference API)")

prompt = st.text_input("Enter your prompt here:")

if st.button("Generate"):
    if prompt.strip() == "":
        st.error("Please type a prompt!")
    else:
        api_url = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
        headers = {"Authorization": f"Bearer {st.secrets['hf_token']}"}

        payload = {
            "inputs": prompt
        }

        with st.spinner("Generating image..."):
            response = requests.post(api_url, headers=headers, json=payload)

            if response.status_code == 200:
                image = Image.open(BytesIO(response.content))
                st.image(image, caption="Generated Image", use_column_width=True)
            else:
                st.error("Error generating image. Try again.")
                st.write(response.status_code, response.text)

