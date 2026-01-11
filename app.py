import streamlit as st
import yt_dlp
import os
from PIL import Image

# --- 1. ページ全体の基本設定 ---
try:
    # GitHubにアップロードしたロゴ画像を読み込む
    icon_image = Image.open("logo.png")
except:
    icon_image = "📥"

st.set_page_config(
    page_title="ATER YouTube Downloader", 
    page_icon=icon_image, 
    layout="centered"
)

# --- 2. モダン・デザイン（CSS） ---
st.markdown("""
    <style>
    /* 全体の背景を白に */
    [data-testid="stAppViewContainer"] {
        background-color: #ffffff;
    }
    
    /* サイドバーの調整 */
    [data-testid="stSidebar"] {
        background-color: #fcfcfc !important;
        border-right: 1px solid #f0f0f0;
    }
    
    /* サイドバー内の文字（SECURITYなど）をくっきり黒に */
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] span, [data-testid="stSidebar"] h3 {
        color: #111111 !important;
        font-weight: 700 !important;
    }

    /* メインタイトルロゴ */
    .modern-logo {
        font-family: 'Helvetica Neue', Arial, sans-serif;
        font-size: 34px !important;
        font-weight: 800 !important;
        color: #1a1a1a;
        text-align: center;
        padding-top: 10px;
        letter-spacing: -1px;
    }

    /* UNLOCKボタンのデザイン（黒背景 ＋ 白文字） */
    div.stButton > button {
        width: 100%;
        height: 48px;
        border-radius: 12px;
        border: none;
        background: linear-gradient(135deg, #222 0%, #444 100%) !important;
        color: #ffffff !important;
        font-weight: 700 !important;
        font-size: 16px !important;
        letter-spacing: 1px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        transition: all 0.2s ease;
    }
    
    div.stButton > button:hover {
        background: linear-gradient(135deg, #444 0%, #666 100%) !important;
        box-shadow: 0 6px 18px rgba(0,0,0,0.25);
        transform: translateY(-1px);
    }
    </style>
    
    <div class="modern-logo">ATER YouTube Downloader</div>
    <div style="text-align: center; color: #888; font-size: 13px; margin-bottom: 30px;">Professional High-Speed Tool</div>
    """, unsafe_allow_html=True)

# --- 3. サイドバーの構成（左上にロゴを配置） ---
with st.sidebar:
    # 画像を一番上に表示することで、画面の「左上」にロゴが来ます
    try:
        st.image("logo.png", use_container_width=True)
    except:
        st.write("Logo image not found")
    
    st.markdown("---") # 区切り線
    st.markdown("### 🛡️ SECURITY")
    input_password = st.text_input("PASSWORD", type="password", placeholder="Enter key")
    
    if st.button("UNLOCK"):
        if input_password == "ater777":
            st.session_state["authenticated"] = True
            st.success("ACCESS GRANTED")
        else:
            st.error("ACCESS DENIED")

# --- 4. メイン機能（認証後） ---
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if st.session_state["authenticated"]:
    url = st.text_input("", placeholder="URLをここに貼り付けてください...")
    
    if st.button("DOWNLOAD START"):
        if url:
            with st.spinner("Processing..."):
                try:
                    ydl_opts = {'format': 'best', 'outtmpl': 'video.mp4'}
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([url])
                    
                    with open("video.mp4", "rb") as f:
                        st.download_button("📥 SAVE FILE", f, file_name="ater_video.mp4")
                    
                    os.remove("video.mp4")
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("URLを入力してください")
else:
    st.info("左側のサイドバーでロックを解除してください。")
