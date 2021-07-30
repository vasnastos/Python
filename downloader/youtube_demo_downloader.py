#pip install pytube3
import pytube as pyt
import sys
from tkinter import messagebox as tk

link="https://youtu.be/YoXa2Pl7Hk0"
try:
 yt=pyt.YouTube(str(link))
except:
    tk.showerror("Connection Error")
msg=""
msg+='------------- Song Info ----------------------\n'
msg+="Song Title:"+str(yt.title)+"\n"
msg+="Song Views:"+str(yt.views)+"\n"
msg+="Song Length:"+str(yt.length)+"\n"
msg+="Description:"+str(yt.description)+"\n"
msg+="Rating:"+str(yt.rating)+"\n"
tk.showinfo(str(link)+" information",msg)
vids=yt.streams.filter(only_audio=True)
counter=1
for x in vids:
    print(str(counter)+"."+str(x)+"\n")
    counter+=1
selected=input("select a download format:")
if int(selected)<0 or int(selected)>len(vids):
    print("Error on selected format exiting app")
    sys.exit(-1)
vids[int(selected)-1].download()

#Play The songPart
