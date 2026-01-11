import streamlit as st
import yt_dlp
import os

# --- 1. ページ全体の基本設定 ---
st.set_page_config(page_title="ATER SYSTEM", page_icon="⚡", layout="centered")

# --- 2. デザイン（CSS） ---
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://images.unsplash.com/photo-1614850523296-d8c1af93d400?q=80&w=2070&auto=format&fit=crop");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    [data-testid="stAppViewContainer"]::before {
        content: "";
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background-color: rgba(0, 0, 0, 0.6);
        z-index: -1;
    }
    .strong-logo {
        font-size: 50px !important;
        font-weight: 900 !important;
        color: #fff !important;
        text-transform: uppercase;
        text-align: center;
        text-shadow: 0 0 10px #ff0055, 0 0 20px #ff0055, 0 0 40px #ff0055;
        letter-spacing: 8px;
        padding: 20px;
        margin-bottom: 30px;
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
    url = st.text_input("YouTube URLを入力")
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
    st.info("パスワードを入力してください")
