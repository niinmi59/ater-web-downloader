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
    layout="centered",
    initial_sidebar_state="expanded"
)

# --- 2. モダン・デザイン（CSS） ---
st.markdown("""
    <style>
    /* 全体の背景 */
    [data-testid="stAppViewContainer"] {
        background-color: #ffffff;
    }
    
    /* サイドバーの背景 */
    [data-testid="stSidebar"] {
        background-color: #fcfcfc !important;
    }

    /* 【修正】サイドバー内の要素の間隔をギリギリまで詰める */
    [data-testid="stSidebarContent"] div {
        gap: 0rem !important;
    }
    
    /* 【修正】ロゴ画像自体の上下余白を消す */
    [data-testid="stSidebar"] [data-testid="stImage"] {
        padding-bottom: 0px !important;
        margin-bottom: -20px !important; /* 上に詰め寄せる */
    }

    /* サイドバー内の文字色を黒に */
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] span, [data-testid="stSidebar"] h3 {
        color: #111111 !important;
        font-weight: 700 !important;
    }

    /* メインタイトル */
    .modern-logo {
        font-family: 'Helvetica Neue', Arial, sans-serif;
        font-size: 32px !important;
        font-weight: 800 !important;
        color: #1a1a1a;
        text-align: center;
        padding-top: 10px;
    }

    /* UNLOCKボタン：黒背景 ＋ 白文字 */
    div.stButton > button {
        width: 100%;
        height: 45px;
        border-radius: 10px;
        border: none;
        background: linear-gradient(135deg, #222 0%, #444 100%) !important;
        color: #ffffff !important;
        font-weight: 700 !important;
        transition: 0.2s;
    }
    
    div.stButton > button:hover {
        background: linear-gradient(135deg, #444 0%, #666 100%) !important;
        color: #ffffff !important;
    }
    </style>
    
    <div class="modern-logo">ATER YouTube Downloader</div>
    <div style="text-align: center; color: #888; font-size: 12px; margin-bottom: 30px;">Professional Media Tool</div>
    """, unsafe_allow_html=True)

# --- 3. サイドバーの構成 ---
with st.sidebar:
    # width=60 にしてロゴをさらに小さく設定
    try:
        st.image("logo.png", width=60) 
    except:
        pass
    
    # 🛡️ SECURITY との距離を詰めるため、線を消して直接配置
    st.markdown("### 🛡️ SECURITY")
    
    input_password = st.text_input("PASSWORD", type="password", placeholder="Key...")
    
    if st.button("UNLOCK"):
        if input_password == "ater777":
            st.session_state["authenticated"] = True
            st.success("GRANTED")
        else:
            st.error("DENIED")

# --- 4. メイン機能 ---
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if st.session_state["authenticated"]:
    url = st.text_input("", placeholder="URLをここに貼り付けてください")
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
    st.info("左側のサイドバーでロックを解除してください。")
