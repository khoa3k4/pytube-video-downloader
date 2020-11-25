# pip install pytube

import pytube

url = input("Enter the url: ")

youtube = pytube.YouTube(url)
video = youtube.streams.get_highest_resolution()

video.download("./Videos")

print("Dowload completed!\nVideo path: ./Videos/" + video.title + ".mp4")