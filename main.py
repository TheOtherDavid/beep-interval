import time
from playsound import playsound

interval = 30
repeat = 4

playsound("beep.mp3")

for x in range(repeat):
    time.sleep(interval)
    print("Playing beep")
    playsound("beep.mp3")

#Two rapid beeps at the end to let you know the program ended
time.sleep(.25)
playsound("beep.mp3")
time.sleep(.01)
playsound("beep.mp3")