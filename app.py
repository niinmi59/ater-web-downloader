import streamlit as st
import yt_dlp
import os

# --- 1. ページ全体の基本設定 ---
st.set_page_config(page_title="ATER Youtube download", page_icon="⚡", layout="centered")

# --- 2. デザイン（CSS）背景を白に、ロゴを際立たせる ---
st.markdown("""
    <style>
    /* 背景を白に設定 */
    [data-testid="stAppViewContainer"] {
        background-color: #ffffff;
        background-image: none;
    }

    /* 強そうなネオンロゴのデザイン（白背景でも映えるように調整） */
    .strong-logo {
        font-size: 50px !important;
        font-weight: 900 !important;
        color: #1a1a1a !important; /* 文字を黒系に */
        text-transform: uppercase;
        text-align: center;
        text-shadow: 2px 2px 10px rgba(255, 0, 85, 0.5); /* ほのかな光 */
        letter-spacing: 8px;
        padding: 20px;
        margin-bottom: 30px;
        font-family: 'Arial Black', sans-serif;
        border-bottom: 5px solid #ff0055; /* 下線で強調 */
    }

    /* 入力欄とボタンの調整 */
    .stTextInput>div>div>input {
        border: 2px solid #ff0055 !important;
    }
    
    .stButton>button {
        width: 100%;
        background-color: #ff0055 !important;
        color: white !important;
        font-weight: bold;
        border-radius: 5px;
    }
    </style>
    
    <div class="strong-logo">ATER SYSTEM</div>
    """, unsafe_allow_html=True)

# --- 3. 認証機能 ---
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

with st.sidebar:
    st.title("🛡️ SECURITY")
    input_password = st.text_input("ENTER PASSWORD", type="password")
    if st.button("UNLOCK"):
        if input_password == "ater777":
            st.session_state["authenticated"] = True
            st.success("ACCESS GRANTED")
        else:
            st.error("ACCESS DENIED")

# --- 4. メイン機能 ---
if st.session_state["authenticated"]:
    url = st.text_input("YouTube URLを入力してください")
    
    if st.button("Video (MP4) を準備"):
        if url:
            with st.spinner("解析中..."):
                try:
                    ydl_opts = {'format': 'best', 'outtmpl': 'video.mp4'}
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([url])
                    with open("video.mp4", "rb") as f:
                        st.download_button("MP4を保存", f, file_name="ater_video.mp4")
                    os.remove("video.mp4")
                except Exception as e:
                    st.error(f"エラー: {e}")
else:
    st.info("パスワードを入力してください。")
