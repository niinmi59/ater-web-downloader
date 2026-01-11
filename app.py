import streamlit as st
import yt_dlp
import os
from PIL import Image

# --- 1. ページ全体の基本設定（タブのアイコン設定） ---
# 事前にGitHubに「logo.png」という名前で画像をアップロードしておいてください
try:
    icon_image = Image.open("logo.png")
except:
    # 画像がない、または読み込めない場合の予備
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
        color: #333333;
    }
    
    /* モダンなタイトルロゴ（黒ベースで力強く） */
    .modern-logo {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-size: 42px !important;
        font-weight: 800 !important;
        color: #1a1a1a;
        text-align: center;
        padding: 40px 0 5px 0;
        letter-spacing: -1px;
    }
    
    .subtitle {
        text-align: center;
        color: #666;
        font-size: 14px;
        margin-bottom: 40px;
    }

    /* 入力エリア（角を少し丸く） */
    .stTextInput>div>div>input {
        border-radius: 10px !important;
        border: 1px solid #ddd !important;
        padding: 12px !important;
    }

    /* モダンなブルーボタン */
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        background-color: #007bff !important;
        color: white !important;
        font-weight: 600;
        border: none;
        padding: 10px 0;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background-color: #0056b3 !important;
        box-shadow: 0 4px 12px rgba(0,123,255,0.3);
    }

    /* サイドバーの調整 */
    section[data-testid="stSidebar"] {
        background-color: #f1f3f5;
    }
    </style>
    
    <div class="modern-logo">ATER YouTube Downloader</div>
    <div class="subtitle">High-speed media extraction system</div>
    """, unsafe_allow_html=True)

# --- 3. 認証機能 ---
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

with st.sidebar:
    st.markdown("### 🛡️ SECURITY")
    input_password = st.text_input("PASSWORD", type="password")
    if st.button("UNLOCK"):
        if input_password == "ater777":
            st.session_state["authenticated"] = True
            st.success("ACCESS GRANTED")
        else:
            st.error("ACCESS DENIED")

# --- 4. メイン機能（認証後） ---
if st.session_state["authenticated"]:
    url = st.text_input("", placeholder="YouTubeのURLをここに貼り付けてください...")
    
    st.write("") # スペース用
    
    if st.button("動画 (MP4) をダウンロード準備"):
        if url:
            with st.spinner("解析・ダウンロード中..."):
                try:
                    # yt-dlpの設定
                    ydl_opts = {'format': 'best', 'outtmpl': 'video.mp4'}
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([url])
                    
                    # ダウンロードボタンを表示
                    with open("video.mp4", "rb") as f:
                        st.download_button("📥 ファイルを保存する", f, file_name="ater_video.mp4")
                    
                    # 使い終わったらサーバーから消す
                    os.remove("video.mp4")
                except Exception as e:
                    st.error(f"エラーが発生しました: {e}")
        else:
            st.warning("URLが入力されていません")
else:
    st.info("利用を開始するにはサイドバーにパスワードを入力してください。")
