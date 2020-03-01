from sense_hat import SenseHat
from time import sleep
from random import randint
import sys

sense = SenseHat()

def set_random_color():
    return [randint(0,255), randint(0,255), randint(0,255)]

o = (0, 0, 0)
x = set_random_color()

avatar1 = [
    o,x,o,x,o,x,o,o,
    o,x,o,x,o,x,o,o,
    o,x,o,x,o,x,o,o,
    o,x,x,x,x,x,o,o,
    o,x,o,x,o,x,o,o,
    o,x,x,x,x,x,o,o,
    o,x,x,o,x,x,o,o,
    o,x,x,x,x,x,o,o
]

avatars = [avatar1]

def main():
    while True:
        for avatar in avatars:
            sense.set_pixels(avatar)
            sleep(1)
        sense.clear()

try:
    main()
except (KeyboardInterrupt, SystemExit):
    print("Programma sluiten")
finally:
    print("Opkuisen van de matrix")
    sense.clear()
    sys.exit(0)