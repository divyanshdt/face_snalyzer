import streamlit as st
from google import genai
from PIL import Image
from dotenv import load_dotenv
import os


load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
if api_key:
    client = genai.Client(api_key=api_key)
    st.title("Face Analyzer")
    photo = st.camera_input('take a real time photo.Dont worry you are not ugly.')
    if photo:
        image = Image.open(photo)
        st.image(image,caption='image uploaded' ,use_column_width=True)
        st.write('analyzing photo.....')
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=[
                "Analyze this face and provide a detailed description of eyes, nose, mouth, "
                "face shape, and any unique features. Then give a rating from 1 to 10 based on overall facial features.",
                image])
        st.subheader("📝 My analysis and rating")
        st.write(response.text)







