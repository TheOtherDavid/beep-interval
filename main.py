import time
from playsound import playsound

interval = 30
quantity = 4

for x in range(quantity):
    playsound("beep.mp3")
    time.sleep(interval)