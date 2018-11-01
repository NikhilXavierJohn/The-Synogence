from pytube import YouTube
import os
def ytdownload(url):
	yt = YouTube(str(url))
	opt=input("Would you like to rename the file (Y/N)")
	if(opt=='Y'):
	    filename=input("Enter a filename :")
	    yt.streams.filter(subtype='mp4').first().download("./videos",filename=filename)
	else:
	    yt.streams.filter(subtype='mp4').first().download("./videos")
	print("file has been successfully downloaded")