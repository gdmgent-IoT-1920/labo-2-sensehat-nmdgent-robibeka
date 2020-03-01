from sense_hat import SenseHat
from random import randint
from time import sleep
import sys

sense = SenseHat()

rows = 8
cols = 8

def set_random_color():
    return [randint(0,255), randint(0,255), randint(0,255)]

def main():
    while True:
        for row in range(rows):
            for col in range(cols):
                sense.set_pixel(col, row, set_random_color())
                sleep(.25)

        sense.clear()

try:
    main()
except (KeyboardInterrupt, SystemExit):
    print("Programma sluiten")
finally:
    print("Opkuisen van de matrix")
    sense.clear()
    sys.exit(0)