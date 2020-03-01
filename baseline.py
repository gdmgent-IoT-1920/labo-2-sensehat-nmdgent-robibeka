from sense_hat import SenseHat
from random import randint
import time
import sys

sense = SenseHat()

def set_random_color():
    return [randint(0, 255), randint(0, 255), randint(0, 255)]

def set_back_color():
    color = set_random_color()
    sense.low_light = True
    return color

def main():
    while True:
        sense.show_message("Hello! We are New Media Development :)", text_colour=set_random_color(), back_colour=set_back_color())

try:
    main()
except (KeyboardInterrupt, SystemExit):
    print("Programma sluiten")
finally:
    print("Opkuisen van de matrix")
    sense.clear()
    sys.exit(0)