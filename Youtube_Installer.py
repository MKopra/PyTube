from pytube import YouTube 
import os

link = input("Enter video link here:  ")
yt = YouTube(link)
Title = yt.title
print("title:  ", Title)
print("views:  ", yt.views)

yd = yt.streams.get_highest_resolution()
filename = f"{Title}.mp4"
yd.download('/Users/mattkopra/Desktop/Movies/Youtube', filename=filename)
