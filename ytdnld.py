from pytube import YouTube

yt = YouTube(str(input("Enter link of video\n")))
videos = yt.streams.all()
for x in videos:
    print(str(x))
n = int(input("enter your choice\n"))
vid = videos[n-1]
vid.download(input("enter destination folder path"))
