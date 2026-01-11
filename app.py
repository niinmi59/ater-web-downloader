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
    
    /* サイドバーの背景を白っぽく */
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

    /* 【修正】ボタンのデザイン：黒背景に白文字で高級感を出す */
    div.stButton > button {
        width: 100%;
        height: 48px;
        border-radius: 12px;
        border: none;
        background: linear-gradient(135deg, #222 0%, #444 100%) !important; /* さっきの黒グラデ */
        color: #ffffff !important; /* 文字を真っ白に固定 */
        font-weight: 700 !important;
        font-size: 16px !important;
        letter-spacing: 1px;
        box-shadow: 0 4px
