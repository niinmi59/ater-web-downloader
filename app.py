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

# --- 2. 徹底的に洗練されたモダン・デザイン（CSS） ---
st.markdown("""
    <style>
    /* 全体の背景 */
    [data-testid="stAppViewContainer"] {
        background-color: #ffffff;
    }
    
    /* サイドバーの調整 */
    [data-testid="stSidebar"] {
        background-color: #fcfcfc !important;
        border-right: 1px solid #f0f0f0;
    }
    
    /* サイドバーの文字（SECURITYなど）をくっきり黒に */
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] span, [data-testid="stSidebar"] h3 {
        color: #111111 !important;
        font-weight: 700 !important;
        font-family: 'Inter', sans-serif;
    }

    /* メインロゴ */
    .modern-logo {
        font-family: 'Helvetica Neue', Arial, sans-serif;
        font-size: 36px !important;
        font-weight: 800 !important;
        color: #1a1a1a;
        text-align: center;
        padding-top: 30px;
        letter-spacing: -1px;
    }

    /* 【修正】ボタンのデザイン：見やすさと高級感を両立 */
    div.stButton > button {
        width: 100%;
        height: 48px;
        border-radius: 12px;
        border: none;
        background-color: #007bff !important; /* 清潔感のあるブルー */
        color: #ffffff !important; /* 文字を真っ白に */
        font-weight: 700 !important;
        font-size: 16px !important;
        box-shadow: 0 4px 12px rgba(0,123,255,0.2);
        transition: all 0.2s ease;
    }
    
    div.stButton > button:hover {
        background-color: #0056b3 !important;
        box-shadow: 0 6px 18px rgba(0,123,255,0.3);
        transform: translateY(-1px);
    }

    /* 入力エリア */
    .stTextInput>div>div>input {
        border-radius: 10px !important;
        border: 1px solid #ddd !important;
    }
    </style>
    
    <div class="modern-logo">ATER YouTube Downloader</div>
    <div style="text-align: center; color: #888; font-size: 14px; margin-bottom: 40px;">Professional Media Tool</div>
    """, unsafe_allow_html=True)

# --- 3. 認証機能 ---
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

with st.sidebar:
    st.markdown("### 🛡️ SECURITY")
    input_password = st.text_input("PASSWORD", type="password", placeholder="Enter your key")
    if st.button("UNLOCK SYSTEM"):
        if input_password == "ater777":
            st.session_state["authenticated"] = True
            st.success("ACCESS GRANTED")
        else:
            st.error("ACCESS DENIED")

# --- 4. メイン機能 ---
if st.session_state["authenticated"]:
    url = st.text_input("", placeholder="ここにURLを貼り付けてください")
    
    if st.button("DOWNLOAD (MP4)"):
        if url:
            with st.spinner("Processing..."):
                try:
                    ydl_opts = {'format': 'best', 'outtmpl': 'video.mp4'}
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([url])
                    with open("video.mp4", "rb") as f:
                        st.download_button("📥 SAVE TO DEVICE", f, file_name="ater_video.mp4")
                    os.remove("video.mp4")
                except Exception as e:
                    st.error(f"Error: {e}")
else:
    st.info("Please enter password in the sidebar.")
