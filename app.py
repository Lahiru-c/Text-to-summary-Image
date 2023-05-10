import streamlit as st
from utils import summarize,generate_image

st.title("Text to Summery to Image")
st.header("Webapp that summarize text and generate image for that summary")

text=st.text_area("Enter your text","sample text")

if st.button("Summarize and Genarate"):
    if not text:
        st.error("Please input a text")
    else:
        with st.spinner("Summerizing..."):
            summary = summarize(text)
        with st.spinner("Generate image..."):
            image = generate_image(summary)
        st.info(f"Summary: {summary}")
        st.image(image)