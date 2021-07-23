import time
from playsound import playsound
import IPython

def ding(mute = False):
    playsound("http://tale3habet.eb2a.com/sounds/kitchen%20timer%20done.mp3")
    if mute == True:
        time.sleep(9)

# Para o Google Colab
def ding2():
    return IPython.display.Audio("http://tale3habet.eb2a.com/sounds/kitchen%20timer%20done.mp3", autoplay=True)
