# pages/SAMUDRA_Enhancer.py
import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Configure page settings
st.set_page_config(
    page_title="SAMUDRA Enhancer",
    page_icon="🖼️",
    layout="wide",
)

# Inject shared CSS
with open("custom_styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Header with IIT & NIOT logos
c1, c2, c3 = st.columns([1,2,1], gap="medium")
with c1:
    st.image("assets/iit_logo.png", width=90)
with c2:
    st.markdown(
        "<h1 class='app-title'>SAMUDRA</h1><p>Dive Deeper, See Clearer</p>",
        unsafe_allow_html=True
    )
with c3:
    st.image("assets/niot_logo.png", width=90)

st.markdown("---")

# Sidebar: image uploader
uploaded = st.sidebar.file_uploader(
    "Upload underwater image (JPG/PNG)",
    type=["jpg", "jpeg", "png"]
)

# Image enhancement logic
def enhance_image(bgr):
    lab = cv2.cvtColor(bgr, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    l_eq = clahe.apply(l)
    merged = cv2.merge((l_eq, a, b))
    bgr_eq = cv2.cvtColor(merged, cv2.COLOR_LAB2BGR)

    wb = cv2.xphoto.createSimpleWB()
    bgr_wb = wb.balanceWhite(bgr_eq)

    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], dtype=np.float32)
    return cv2.filter2D(bgr_wb, -1, kernel)

if uploaded:
    img_pil = Image.open(uploaded).convert("RGB")
    rgb = np.array(img_pil)
    bgr = cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)

    enhanced_bgr = enhance_image(bgr)
    enhanced = cv2.cvtColor(enhanced_bgr, cv2.COLOR_BGR2RGB)

    cols = st.columns(3, gap="medium")
    for col, title, img in zip(cols, ["Original","Enhanced","Detected"], [rgb, enhanced, enhanced]):
        col.subheader(title)
        col.image(img, use_column_width=True)

    st.success(f"Image processed successfully!")
else:
    st.sidebar.info("⬅️ Upload an underwater image to begin")
    st.write("Awaiting your image...")