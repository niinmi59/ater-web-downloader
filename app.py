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

    /* ロゴ画像の上下余白を最小化（重ならない程度に） */
    [data-testid="stSidebar"] [data-testid="stImage"] {
        padding-top: 10px !important;
        padding-bottom: 0px !important;
        margin-bottom: 5px !important; /* マイナスをやめて少しだけ隙間を空ける */
    }

    /* サイドバー内の文字色を黒に */
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] span, [data-testid="stSidebar"] h3 {
        color: #111111 !important;
        font-weight: 700 !important;
        margin-top: 0px !important;
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
        color: #ffffff !
