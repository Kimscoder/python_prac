from yt_dlp import YoutubeDL

url = 'https://www.youtube.com/watch?v=u_Q7Dkl7AIk'

ydl_opts={}

download = YoutubeDL(ydl_opts).download([url])