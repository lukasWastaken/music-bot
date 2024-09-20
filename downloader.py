import os
import yt_dlp

def DownloadMp3FromUrl(Url):
    
    DL_path = f"C:\\Users\\{os.getlogin()}\\Music\Discord\\"

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': DL_path + '%(title)s.%(ext)s',
        'quiet': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(Url, download=True)
            audio_file = DL_path + f"{info['title']}.mp3"
            return audio_file
    except Exception as e:
            print(f"Error while handling download: {str(e)}")