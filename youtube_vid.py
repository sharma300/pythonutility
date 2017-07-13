from __future__ import unicode_literals
import bs4, requests
import youtube_dl



home_url = "https://www.youtube.com"



search_item = raw_input("Enter the search item ")
url = "https://www.youtube.com/results?search_query=" + search_item

res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text)

search_results = soup.select("h3 a")
video_title = search_results[0].get("title")
video_url = home_url + search_results[0].get("href")

choice=raw_input("1. for video and else for audio")
if choice == '1':
    print("Downloading video from %s" % (video_url))
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
    print("Dowload Complete.")

else:
    print("Downloading audio from %s" % (video_url))


    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
    print("Dowload Complete.")







