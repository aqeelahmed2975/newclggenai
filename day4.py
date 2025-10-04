import streamlit as st
from PIL import Image
from google import genai
Robo = genai.Client(api_key="AIzaSyDUzxme5hzw082d1PcIfjoe3IMoIpQCLYo")
st.title("AI Bot: Image Insight")
myfile = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
if myfile:
    image = Image.open(myfile)
    st.image(image, caption="Uploaded Image", use_column_width=True)
question = st.text_input("Ask something about the image")
if st.button("Send") and myfile and question:
    response = Robo.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            {"role": "user", "parts": [
                {"text": question},
                {"inline_data": {
                    "mime_type": myfile.type,
                    "data": myfile.getvalue()
                }}
            ]}
        ]
    )
    st.write("Response:", response.text)


