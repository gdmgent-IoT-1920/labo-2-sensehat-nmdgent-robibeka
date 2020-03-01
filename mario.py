from sense_hat import SenseHat
from time import sleep
import sys

sense = SenseHat()

o = (0, 0, 0)
b = (0, 0, 255)
r = (255, 0, 0)
s = (236, 188, 180)

mario = [
    o, o, r, r, r, r, o, o,
    o, o, s, s, s, o, o, o,
    o, o, s, s, s, o, o, o,
    r, r, r, s, r, r, r, o,
    o, o, b, r, b, o, o, o,
    o, o, b, b, b, o, o, o,
    o, o, b, o, b, o, o, o,
    o, o, b, b, b, b, o, o
]

marioJump = [
    o, o, r, r, r, r, o, o,
    o, o, s, s, s, o, o, o,
    o, o, s, s, s, o, o, o,
    r, r, r, s, r, r, r, o,
    o, o, b, r, b, o, b, o,
    b, b, b, b, b, b, b, o,
    b, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o
]


def main():
    while True:
        sense.set_pixels(mario)
        event = sense.stick.wait_for_event()

        if event.direction == "up":
            sense.set_pixels(marioJump)
            sleep(.2)
            sense.set_pixels(mario)


try:
    main()
except (KeyboardInterrupt, SystemExit):
    print("Programma sluiten")
finally:
    print("Opkuisen van de matrix")
    sense.clear()
    sys.exit(0)
