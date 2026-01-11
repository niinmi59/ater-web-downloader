import streamlit as st
import yt_dlp
import os

# ページの設定
st.set_page_config(page_title="ATER YouTube Downloader", page_icon="📺")

# タイトルとロゴ
st.title("📺 ATER YouTube Downloader")
st.markdown("---")

# 簡易パスワード機能（プライベート化）
PASSWORD = "ater777" # 好きなパスワードに変えてください
user_pass = st.sidebar.text_input("Password", type="password")

if user_pass != PASSWORD:
    st.warning("パスワードを入力してください（左側のメニュー）")
else:
    # URL入力欄
    url = st.text_input("YouTubeのURLを入力してください", placeholder="https://www.youtube.com/watch?v=...")

    col1, col2 = st.columns(2)
    with col1:
        v_btn = st.button("Video (MP4) を準備")
    with col2:
        a_btn = st.button("Audio (MP3) を準備")

    if v_btn or a_btn:
        if not url:
            st.error("URLを入力してください")
        else:
            try:
                st.info("サーバーで動画を処理中... 1分ほどかかる場合があります。")
                
                # yt-dlpの設定
                format_opt = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]' if v_btn else 'bestaudio/best'
                ext = 'mp4' if v_btn else 'mp3'
                
                ydl_opts = {
                    'format': format_opt,
                    'outtmpl': 'downloaded_file.%(ext)s',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }] if a_btn else [],
                }

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=True)
                    filename = ydl.prepare_filename(info)
                    if a_btn: filename = filename.rsplit('.', 1)[0] + ".mp3"

                # ダウンロードボタンの表示
                with open(filename, "rb") as f:
                    st.success("準備完了！下のボタンを押して保存してください。")
                    st.download_button(
                        label="スマホに保存する",
                        data=f,
                        file_name=f"{info['title']}.{ext}",
                        mime=f"video/{ext}" if v_btn else f"audio/{ext}"
                    )
                
                # サーバー内のファイルを削除（掃除）
                os.remove(filename)

            except Exception as e:
                st.error(f"エラーが発生しました: {e}")