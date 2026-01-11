import streamlit as st
import yt_dlp
import os

# --- 1. ページ全体の基本設定 ---
st.set_page_config(page_title="ATER YouTube Downloader", page_icon="⚡", layout="centered")

# --- 2. 強そうなデザイン（CSS） ---
st.markdown("""
    <style>
    /* 背景画像の設定 */
    [data-testid="stAppViewContainer"] {
        background-image: url("https://images.unsplash.com/photo-1614850523296-d8c1af93d400?q=80&w=2070&auto=format&fit=crop"); /* 仮のカッコいい背景 */
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    /* 全体にかける暗めのフィルター */
    [data-testid="stAppViewContainer"]::before {
        content: "";
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background-color: rgba(0, 0, 0, 0.6);
        z-index: -1;
    }

    /* 強そうなネオンロゴのデザイン */
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
        font-family: 'Arial Black', sans-serif;
    }

    /* 入力欄やボタンの見た目調整 */
    .stTextInput>div>div>input {
        background-color: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        border: 1px solid #ff0055 !important;
    }
