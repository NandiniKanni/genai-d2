import streamlit as st
from diffusers import StableDiffusionPipeline
import torch

st.set_page_config(page_title="Text to Image Generator")

st.title("🖼️ Text-to-Image Generator")

prompt = st.text_input("Enter your prompt here:", "")

if st.button("Generate Image"):
    if prompt.strip() == "":
        st.error("Please enter a prompt!")
    else:
        with st.spinner("Generating..."):
            pipe = StableDiffusionPipeline.from_pretrained(
                "runwayml/stable-diffusion-v1-5",
                torch_dtype=torch.float16,
                use_auth_token=st.secrets["hf_token"]
            )
            pipe = pipe.to("cuda")

            image = pipe(prompt).images[0]
            st.image(image, caption="Generated Image", use_column_width=True)
