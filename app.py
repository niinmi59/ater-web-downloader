import streamlit as st
import yt_dlp
import os
from PIL import Image

# --- 1. ページ全体の基本設定 ---
try:
    icon_image = Image.open("logo.png")
except:
    icon_image = "📥"

st.set_page_config(
    page_title="ATER YouTube Downloader", 
    page_icon=icon_image, 
    layout="centered"
)

# --- 2. 徹底的にモダンなデザイン（CSS） ---
st.markdown("""
    <style>
    /* メイン背景 */
    [data-testid="stAppViewContainer"] {
        background-color: #ffffff;
    }
    
    /* サイドバーの高級化 */
    [data-testid="stSidebar"] {
        background-color: #fcfcfc !important;
        border-right: 1px solid #eee;
    }
    
    /* サイドバーの文字色（超重要：ここを黒く） */
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] span, [data-testid="stSidebar"] h3 {
        color: #222 !important;
        font-family: 'Inter', sans-serif;
        font-weight: 700 !important;
    }

    /* タイトルロゴ */
    .modern-logo {
        font-family: 'Avenir', 'Helvetica Neue', sans-serif;
        font-size: 36px !important;
        font-weight: 900 !important;
        color: #000;
        text-align: center;
        padding-top: 30px;
        letter-spacing: -1.5px;
    }

    /* 入力エリアのモダン化 */
    .stTextInput>div>div>input {
        border-radius: 8px !important;
        border: 1px solid #e0e0e0 !important;
        background-color: #fff !important;
        transition: 0.3s;
    }
    .stTextInput>div>div>input:focus {
        border-color: #007bff !important;
        box-shadow: 0 0 0 3px rgba(0,123,255,0.1) !important;
    }

    /* 【修正】UNLOCKボタンをカッコよく！ */
    div.stButton > button {
        width: 100%;
        height: 45px;
        border-radius: 10px;
        border: none;
        background: linear-gradient(135deg, #222 0%, #444 100%) !important;
        color: white !important;
        font-weight: 600 !important;
        font-size: 16px !important;
        letter-spacing: 1px;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    div.stButton > button:hover {
        background: linear-gradient(135deg, #444 0%, #666 100%) !important;
        box-shadow: 0 6px 15px rgba(0,0,0,0.2);
        transform: translateY(-2px);
    }
    
    div.stButton > button:active {
        transform: translateY(1px);
    }
    </style>
    
    <div class="modern-logo">ATER YouTube Downloader</div>
    <div style="text-align: center; color: #999; font-size: 12px; margin-bottom: 40px;">Ver 2.0 Premium Design</div>
    """, unsafe_allow_html=True)

# --- 3. 認証機能 ---
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

with st.sidebar:
    st.markdown("### 🛡️ SECURITY")
    input_password = st.text_input("PASSWORD", type="password", placeholder="••••••••")
    if st.button("UNLOCK"):
        if input_password == "ater777":
            st.session_state["authenticated"] = True
            st.success("ACCESS GRANTED")
        else:
            st.error("ACCESS DENIED")

# --- 4. メイン機能 ---
if st.session_state["authenticated"]:
    url = st.text_input("", placeholder="ここにURLをペースト...")
    
    if st.button("PREPARE DOWNLOAD"):
        if url:
            with st.spinner("Processing..."):
                try:
                    ydl_opts = {'format': 'best', 'outtmpl': 'video.mp4'}
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([url])
                    with open("video.mp4", "rb") as f:
                        st.download_button("📥 DOWNLOAD MP4", f, file_name="ater_video.mp4")
                    os.remove("video.mp4")
                except Exception as e:
                    st.error(f"Error: {e}")
else:
    st.info("Please unlock to use this system.")
