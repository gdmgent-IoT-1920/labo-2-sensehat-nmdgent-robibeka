from sense_hat import SenseHat
from time import sleep
from random import randint
import sys

sense = SenseHat()

def set_random_color():
    return [randint(0,255), randint(0,255), randint(0,255)]

o = (0, 0, 0)
x = (set_random_color())

rect1 = [
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,x,x,o,o,o,
o,o,o,x,x,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o
]

rect2 = [
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,x,x,x,x,o,o,
o,o,x,o,o,x,o,o,
o,o,x,o,o,x,o,o,
o,o,x,x,x,x,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o
]

rect3 = [
o,o,o,o,o,o,o,o,
o,x,x,x,x,x,x,o,
o,x,o,o,o,o,x,o,
o,x,o,o,o,o,x,o,
o,x,o,o,o,o,x,o,
o,x,o,o,o,o,x,o,
o,x,x,x,x,x,x,o,
o,o,o,o,o,o,o,o
]

rect4 = [
x,x,x,x,x,x,x,x,
x,o,o,o,o,o,o,x,
x,o,o,o,o,o,o,x,
x,o,o,o,o,o,o,x,
x,o,o,o,o,o,o,x,
x,o,o,o,o,o,o,x,
x,o,o,o,o,o,o,x,
x,x,x,x,x,x,x,x
]

rectangles = [rect1, rect2, rect3, rect4]

def main():
    while True:
        for rect in rectangles:
            sense.set_pixels(rect)
            sleep(1)

        for rect in reversed(rectangles):
            sense.set_pixels(rect)
            sleep(1)

try:
    main()
except (KeyboardInterrupt, SystemExit):
    print("Programma sluiten")
finally:
    print("Opkuisen van de matrix")
    sense.clear()
    sys.exit(0)