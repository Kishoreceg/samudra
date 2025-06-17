import streamlit as st
from PIL import Image

# ---------- Page config ----------
st.set_page_config(
    page_title="NIOT • National Institute of Ocean Technology",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------- Inject shared CSS ----------
with open("custom_styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---------- Header ----------
col1, col2, col3 = st.columns([1, 2, 1], gap="medium")
with col1:
    st.write("")  # spacer
with col2:
    st.image("assets/niot_logo.png", width=180)
    st.markdown("<h1 class='app-title'>National Institute of Ocean Technology</h1>",
                unsafe_allow_html=True)
with col3:
    st.write("")

st.markdown("---")

# ---------- NIOT overview ----------
st.subheader("Overview")
st.write(
    "Established in **November 1993** as an autonomous society under the "
    "*Ministry of Earth Sciences (MoES), Government of India*, the National Institute of "
    "Ocean Technology (NIOT) develops indigenous ocean technologies to support India’s "
    "blue‑economy ambitions."
)

# ---------- Mission ----------
st.subheader("Mission")
st.write(
    "To create reliable, cost‑effective technologies for **ocean resource exploration, "
    "observation, renewable energy, coastal protection, and disaster mitigation**, thereby "
    "enhancing national self‑reliance."
)

# ---------- Core research areas ----------
st.subheader("Key Research Areas")
st.markdown(
"""
- **Deep‑Sea Technologies** — crewed & autonomous submersibles for seabed mining and research  
- **Ocean Observation Systems** — data buoys and bottom‑pressure recorders for tsunami early‑warning  
- **Coastal & Offshore Engineering** — moorings, pipelines, island shoreline protection  
- **Ocean Renewable Energy & Desalination** — low‑temperature thermal desalination (LTTD) and OTEC  
"""
)

# ---------- Flagship projects ----------
st.subheader("Flagship Projects")
st.table({
    "Project": [
        "Matsya 6000 crewed submersible",
        "Deep Ocean Mission",
        "100 k L/day LTTD plants"
    ],
    "Purpose": [
        "Carry 3 aquanauts to 6 km depth for *Samudrayaan* mission",
        "End‑to‑end tech for deep‑sea mining & blue‑economy R&D",
        "Provide potable water to Lakshadweep & remote islands"
    ]
})

# ---------- Headquarters ----------
st.subheader("Headquarters")
st.write(
    "📍 Velachery‑Tambaram Main Road, Pallikaranai, Chennai 600 100, Tamil Nadu, India"
)

# ---------- Call‑to‑action ----------
st.success(
    "Use the sidebar to navigate to **SAMUDRA Enhancer** and try NIOT‑style "
    "underwater image processing on your own photos."
)

# ---------- Footer note ----------
st.caption("© 2025 National Institute of Ocean Technology • Ministry of Earth Sciences, India")
