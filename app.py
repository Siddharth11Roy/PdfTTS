# -*- coding: utf-8 -*-
"""pydf_tts.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lPVx9wSF3IkWOXgzhIb-DfbTOZBF14_6
"""

# !pip install streamlit

# !pip install pymupdf

# !pip install pyttsx3

# import streamlit as st
# import fitz
# import pyttsx3
# from gtts import gTTS
# import os

# def extract_text_from_pdf(pdf_file):
#     with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
#         text = "\n".join(page.get_text("text") for page in doc)
#     return text

# def text_to_speech(text):
#     tts = gTTS(text=text, lang="en")  # Convert text to speech
#     tts.save("output_audio.mp3")  # Save as MP3 file

# st.title("PDF to Speech Converter")

# uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

# # if uploaded_file is not None:
# #     text = extract_text_from_pdf(uploaded_file)
# #     st.text_area("Extracted Text", text, height=300)

# #     if st.button("Convert to Speech"):
# #         text_to_speech(text)
# #         st.audio("output_audio.mp3", format="audio/mp3", start_time=0)


# # Language Selection
# lang_map = {"English": "en", "Hindi": "hi", "French": "fr", "Spanish": "es"}
# lang_choice = st.selectbox("Select Language", list(lang_map.keys()))

# # Speech Speed Selection
# speed_choice = st.radio("Speech Speed", ["Normal", "Slow"])

# if uploaded_file is not None:
#     text = extract_text_from_pdf(uploaded_file)
#     st.text_area("Extracted Text", text, height=300)

#     if st.button("Convert to Speech"):
#         text_to_speech(text, lang_map[lang_choice], speed_choice)
#         st.audio("output_audio.mp3", format="audio/mp3", start_time=0)


# import streamlit as st
# import fitz  # PyMuPDF for extracting text from PDFs
# from gtts import gTTS
# import os

# # Function to extract text from PDF
# def extract_text_from_pdf(pdf_file):
#     try:
#         with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
#             text = "\n".join(page.get_text("text") for page in doc)
#         return text.strip()  # Remove leading/trailing whitespace
#     except Exception as e:
#         st.error(f"Error extracting text: {e}")
#         return ""

# # Function to convert text to speech using gTTS
# def text_to_speech(text, lang, speed):
#     if not text:
#         st.error("No text extracted from the PDF. Please upload a valid PDF with selectable text.")
#         return

#     try:
#         tts = gTTS(text=text, lang=lang, slow=(speed == "Slow"))
#         tts.save("output_audio.mp3")
#     except Exception as e:
#         st.error(f"Error in text-to-speech conversion: {e}")

# # Streamlit UI
# st.title("📄 PDF to Speech Converter 🔊")

# # File Upload
# uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

# # Language Selection
# lang_map = {"English": "en", "Hindi": "hi", "French": "fr", "Spanish": "es"}
# lang_choice = st.selectbox("Select Language", list(lang_map.keys()))

# # Speech Speed Selection
# speed_choice = st.radio("Speech Speed", ["Normal", "Slow"])

# if uploaded_file is not None:
#     text = extract_text_from_pdf(uploaded_file)
#     st.text_area("Extracted Text", text, height=300)

#     if st.button("Convert to Speech"):
#         text_to_speech(text, lang_map[lang_choice], speed_choice)

#         # Play audio if it was generated successfully
#         if os.path.exists("output_audio.mp3"):
#             st.audio("output_audio.mp3", format="audio/mp3", start_time=0)


import streamlit as st
import fitz  # PyMuPDF for extracting text from PDFs
from gtts import gTTS
from pydub import AudioSegment
import os

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    try:
        with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
            text = "\n".join(page.get_text("text") for page in doc)
        return text.strip()
    except Exception as e:
        st.error(f"Error extracting text: {e}")
        return ""

# Function to convert text to speech and adjust speed
def text_to_speech(text, lang, speed_multiplier):
    if not text:
        st.error("No text extracted from the PDF. Please upload a valid PDF with selectable text.")
        return

    try:
        # Generate speech at normal speed
        tts = gTTS(text=text, lang=lang)
        tts.save("temp_audio.mp3")

        # Load the generated audio and adjust speed
        audio = AudioSegment.from_file("temp_audio.mp3", format="mp3")
        new_audio = audio.speedup(playback_speed=speed_multiplier)
        new_audio.export("output_audio.mp3", format="mp3")

    except Exception as e:
        st.error(f"Error in text-to-speech conversion: {e}")

# Streamlit UI
st.title("📄 PDF to Speech Converter 🔊")

# File Upload
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

# Language Selection
lang_map = {"English": "en", "Hindi": "hi", "French": "fr", "Spanish": "es"}
lang_choice = st.selectbox("Select Language", list(lang_map.keys()))

# Speech Speed Selection (1.0x to 2.5x)
speed_choice = st.slider("Speech Speed", min_value=1.0, max_value=2.5, value=1.0, step=0.5)

if uploaded_file is not None:
    text = extract_text_from_pdf(uploaded_file)
    st.text_area("Extracted Text", text, height=300)

    if st.button("Convert to Speech"):
        text_to_speech(text, lang_map[lang_choice], speed_choice)

        # Play audio if it was generated successfully
        if os.path.exists("output_audio.mp3"):
            st.audio("output_audio.mp3", format="audio/mp3", start_time=0)

