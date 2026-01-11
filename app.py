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

    /* 【修正】ロゴを左端に寄せ、余白を調整 */
    [data-testid="stSidebar"] [data-testid="stImage"] {
        text-align: left !important;
        padding-top: 10px !important;
        margin-left: -15px !important; /* 左端に寄せる */
        margin-bottom: 5px !important;
    }

    /* 【修正】SECURITYの文字位置を微調整 */
    [data-testid="stSidebar"] h3 {
        color: #111111 !important;
        font-weight: 700 !important;
        margin-top: 5px !important; /* ロゴとの絶妙な距離 */
        padding-left: 2px !important;
    }

    /* タイトルデザイン */
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
    }
    
    div.stButton > button:hover {
        background: linear-gradient(135deg, #444 0%, #666 100%) !important;
        color: #ffffff !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 中央のタイトル表示
st.markdown('<div class="modern-logo">ATER YouTube Downloader</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: center; color: #888; font-size: 12px; margin-bottom: 30px;">Professional Media Tool</div>', unsafe_allow_html=True)

# --- 3. サイドバーの構成 ---
with st.sidebar:
    # ロゴサイズ 45px で左端に配置
    try:
        st.image("logo.png", width=45) 
    except:
        pass
    
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
    url = st.text_input("", placeholder="URLを入力してください")
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
