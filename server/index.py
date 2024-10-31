from pytubefix import YouTube
import os
import asyncio
try:
    yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo').streams
except URLError:
    print("connect to wifi")
# print(yt.filter(only_audio=True))
# song_name = yt.get_audio_only().title.replace(" ", "_")

song_path = yt.get_audio_only().download(mp3=True)

new_path = os.path.join("./", yt.get_audio_only().title.replace(" ", "_")[:11] + ".mp3")
os.rename(song_path, new_path)

# os.rename(song_path, song_name) 

# await asyncio.run(os.rename(f"{yt.get_audio_only().title}.mp3", song_name))
print("real done")



