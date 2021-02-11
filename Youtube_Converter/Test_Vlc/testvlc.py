import vlc
 
# creating vlc media player object
media = vlc.MediaPlayer("test.mp4")
 
# start playing video
media.play()

while True:
     pass