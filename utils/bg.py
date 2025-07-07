import streamlit as st
import base64

def set_bg_from_local(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
        
    encoded = base64.b64encode(data).decode()
    css = f"""
   <style>
   .stApp {{
    background-image: url("data:image/jpeg;base64,{encoded}");
    background-size: contain;
    background-position: center;
    background-attachment: fixed;
    
    }}

    </style>

    """  
 
    st.markdown(css, unsafe_allow_html=True)



