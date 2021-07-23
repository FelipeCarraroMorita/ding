import vlc
import time

def ding():
    p = vlc.MediaPlayer("http://tale3habet.eb2a.com/sounds/kitchen%20timer%20done.mp3")
    p.play()
    time.sleep(9)