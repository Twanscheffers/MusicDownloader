import os
from pytube import YouTube
from tkinter import *

root = Tk()

e = Entry(root, width=50, borderwidth=2)
e.pack()

def myClick():
    
    #maak een functie die de download start en de link pakt uit de entry e
    yt = YouTube(e.get())
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path='[OUTPUT_PATH]')
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

myCanvas = Canvas(root, height=100, width=400, bg="#263D42")
myCanvas.pack()

myButton = Button(root, text = "Download", command=myClick)
myButton.pack()

root.mainloop()
