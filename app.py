import streamlit as st
from PIL import Image, ImageFilter
import io

# Custom CSS for styling
st.markdown("""
<style>
    .stApp {
        background-color: #f5f5f5;
    }
    .css-1d391kg {  /* Sidebar */
        background-color: #ffffff;
        border-right: 2px solid #e0e0e0;
    }
    .stTitle {
        color: #2e86c1;
        font-family: 'Arial', sans-serif;
        text-align: center;
    }
    .stSubheader {
        color: #34495e;
        font-weight: bold;
    }
    .stButton>button {
        background-color: #3498db;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #2980b9;
    }
    .stImage {
        border: 2px solid #bdc3c7;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .stInfo {
        background-color: #d4edda;
        color: #155724;
        border: 1px solid #c3e6cb;
        border-radius: 5px;
        padding: 10px;
    }
</style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="Image Smoothing", layout="wide")
st.title("Image Smoothing Application")
st.write("Upload an image and apply smoothing filters to blur it")

# Sidebar for filter selection
st.sidebar.header("Filter Settings")
filter_type = st.sidebar.selectbox(
    "Select smoothing filter:",
    ["Blur", "Smooth", "Gaussian Blur"]
)

radius = st.sidebar.slider(
    "Blur radius:",
    min_value=1,
    max_value=20,
    value=5,
    step=1
)

# File uploader
uploaded_file = st.file_uploader(
    "Choose an image file",
    type=["jpg", "jpeg", "png", "bmp", "gif"]
)

if uploaded_file is not None:
    # Load the image
    image = Image.open(uploaded_file)
    
    # Apply smoothing filter
    if filter_type == "Blur":
        smoothed_image = image.filter(ImageFilter.BLUR)
    elif filter_type == "Smooth":
        smoothed_image = image.filter(ImageFilter.SMOOTH_MORE)
    else:  # Gaussian Blur
        smoothed_image = image.filter(ImageFilter.GaussianBlur(radius=radius))
    
    # Display results
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Original Image")
        st.image(image, use_column_width=True)
    
    with col2:
        st.subheader("Smoothed Image")
        st.image(smoothed_image, use_column_width=True)
    
    # Download button
    buf = io.BytesIO()
    smoothed_image.save(buf, format="PNG")
    buf.seek(0)
    
    st.download_button(
        label="Download Smoothed Image",
        data=buf,
        file_name="smoothed_image.png",
        mime="image/png"
    )
else:
    st.info("Please upload an image to get started")