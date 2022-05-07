import time
from playsound import playsound

interval = 30
repeat = 0

playsound("beep.mp3")

for x in range(repeat):
    time.sleep(interval)
    playsound("beep.mp3")

#Two rapid beeps at the end to let you know the program ended
playsound("beep.mp3")
time.sleep(.01)
playsound("beep.mp3")