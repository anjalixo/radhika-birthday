import streamlit as st
from pathlib import Path
import base64

st.set_page_config(
    page_title="Happy Birthday Radhika!",
    page_icon="🎂",
    layout="wide",
    initial_sidebar_state="collapsed",
)

BASE_DIR = Path(__file__).parent
PHOTO_DIR = BASE_DIR 

def image_to_base64(path):
    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

photos = sorted(PHOTO_DIR.glob("*.jpg"))

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Poppins:wght@400;500;600;700;800&display=swap');

html, body, [data-testid="stAppViewContainer"] {
    background: linear-gradient(145deg, #fff0f6 0%, #ffe1ed 48%, #fff7fb 100%);
}
[data-testid="stHeader"] { background: transparent; }
[data-testid="stSidebar"] { display: none; }
.block-container {
    max-width: 1120px;
    padding: 2.5rem 1.2rem 3rem;
}
.hero {
    text-align: center;
    padding: 2.2rem 1rem 1.4rem;
}
.kicker {
    color: #c64c83;
    font: 600 0.9rem 'Poppins', sans-serif;
    letter-spacing: 0.28em;
    text-transform: uppercase;
    margin-bottom: 1rem;
}
.hero h1 {
    font-family: 'DM Serif Display', Georgia, serif;
    color: #c52f75;
    font-size: clamp(3.2rem, 9vw, 7.2rem);
    line-height: 0.98;
    margin: 0;
    text-shadow: 0 5px 0 rgba(255,255,255,.8), 0 12px 28px rgba(190,55,115,.15);
}
.hero h2 {
    color: #e15b96;
    font: 700 clamp(1.6rem, 4vw, 3rem) 'Poppins', sans-serif;
    margin: 0.4rem 0 0;
}
.sparkles {
    font-size: 1.6rem;
    letter-spacing: 0.55rem;
    margin-top: 1.2rem;
}
.subtitle {
    color: #9d5274;
    font: 500 1rem 'Poppins', sans-serif;
    margin-top: 0.9rem;
}
.gallery-title {
    text-align: center;
    color: #bd477e;
    font: 600 1rem 'Poppins', sans-serif;
    letter-spacing: .12em;
    margin: 1.6rem 0 1.1rem;
}
.photo-card {
    background: white;
    padding: 9px 9px 13px;
    border-radius: 18px;
    box-shadow: 0 9px 25px rgba(167, 69, 112, .14);
    margin: 0 0 1.2rem;
    transform: rotate(var(--tilt, 0deg));
    transition: transform .25s ease, box-shadow .25s ease;
}
.photo-card:hover {
    transform: translateY(-5px) rotate(0deg);
    box-shadow: 0 14px 30px rgba(167, 69, 112, .22);
}
.photo-card img {
    display: block;
    width: 100%;
    height: 320px;
    object-fit: cover;
    border-radius: 12px;
}
.footer {
    text-align: center;
    color: #c34b81;
    font: 600 1.05rem 'Poppins', sans-serif;
    padding: 1.2rem 0 .5rem;
}
div[data-testid="stImage"] img { border-radius: 16px; }
@media (max-width: 700px) {
    .block-container { padding-top: 1rem; }
    .hero { padding-top: 1.2rem; }
    .photo-card img { height: 250px; }
}
</style>

<div class="hero">
    <div class="kicker">A little celebration for someone special</div>
    <h1>HAPPY BIRTHDAY</h1>
    <h2>RADHIKA! 🎂</h2>
    <div class="sparkles">♡ ✨ ♡ ✨ ♡</div>
    <div class="subtitle">So many memories, so much laughter, and more moments to come 💗</div>
</div>
<div class="gallery-title">OUR LITTLE MEMORY WALL ♡</div>
""", unsafe_allow_html=True)

if photos:
    # Three columns on desktop; Streamlit automatically stacks responsively on smaller screens.
    cols = st.columns(3, gap="medium")
    tilts = ["-1.4deg", "1.2deg", "-0.8deg", "1.5deg", "-1deg", "0.8deg"]
    for idx, photo in enumerate(photos):
        with cols[idx % 3]:
            encoded = image_to_base64(photo)
            st.markdown(
                f'<div class="photo-card" style="--tilt:{tilts[idx % len(tilts)]}">'
                f'<img src="data:image/jpeg;base64,{encoded}" alt="Birthday memory {idx+1}">'
                f'</div>',
                unsafe_allow_html=True,
            )

st.markdown("""
<div class="footer">
    Made with lots of love ♡ &nbsp; Happy Birthday, Radhika! 💕
</div>
""", unsafe_allow_html=True)
