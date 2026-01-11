import streamlit as st
import yt_dlp
import os

# --- 1. ページ全体の基本設定 ---
st.set_page_config(page_title="ATER YouTube Downloader", page_icon="📥", layout="centered")

# --- 2. モダン・デザイン（CSS） ---
st.markdown("""
    <style>
    /* 全体の背景を清潔感のある白に */
    [data-testid="stAppViewContainer"] {
        background-color: #f8f9fa;
        color: #333333;
    }
    
    /* モダンなタイトルロゴ */
    .modern-logo {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-size: 42px !important;
        font-weight: 800 !important;
        color: #1a1a1a;
        text-align: center;
        padding: 40px 0 10px 0;
        letter-spacing: -1px;
    }
    
    .subtitle {
        text-align: center;
        color: #666;
        font-size: 14px;
        margin-bottom: 40px;
    }

    /* 入力エリアのカスタマイズ */
    .stTextInput>div>div>input {
        border-radius: 10px !important;
        border: 1px solid #ddd !important;
        padding: 15px !important;
    }

    /* モダンな青いボタン */
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        background-color: #007bff !important;
        color: white !important;
        font-weight: 600;
        border: none;
        padding: 12px 0;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background-color: #0056b3 !important;
        box-shadow: 0 4px 12px rgba(0,123,255,0.3);
    }
    </style>
    
    <div class="modern-logo">ATER YouTube Downloader</div>
    <div class="subtitle">High-speed media extraction system</div>
    """, unsafe_allow_html=True)

# --- 3. 認証機能 ---
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

# サイドバーのデザイン
with st.sidebar:
    st.markdown("### 🛡️ Auth")
    input_password = st.text_input("PASSWORD", type="password")
    if st.button("UNLOCK"):
        if input_password == "ater777":
            st.session_state["authenticated"] = True
            st.success("認証成功")
        else:
            st.error("パスワードが違います")

# --- 4. メイン機能 ---
if st.session_state["authenticated"]:
    url = st.text_input("", placeholder="ここにYouTubeのURLを貼り付けてください...")
    
    st.write("") # スペース
    
    if st.button("動画を準備する (MP4)"):
        if url:
            with st.spinner("解析中..."):
                try:
                    ydl_opts = {'format': 'best', 'outtmpl': 'video.mp4'}
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([url])
                    with open("video.mp4", "rb") as f:
                        st.download_button("📥 ダウンロードを開始", f, file_name="ater_video.mp4")
                    os.remove("video.mp4")
                except Exception as e:
                    st.error(f"エラーが発生しました: {e}")
        else:
            st.warning("URLを入力してください")
else:
    st.info("利用するにはサイドバーからパスワードを入力してください。")
