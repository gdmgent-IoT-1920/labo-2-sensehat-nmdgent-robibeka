from sense_hat import SenseHat
from time import sleep
from random import randint
import sys

sense = SenseHat()

def main():
    avatars = ["./images/avatar1.png", "./images/avatar2.png", "./images/avatar3.png"]
    interval = float(input("How much time do you want between each avatar? "))

    while True:
        sense.load_image(avatars[randint(0,2)])
        sleep(interval)
        sense.clear()

try:
    main()
except (KeyboardInterrupt, SystemExit):
    print("Programma sluiten")
finally:
    print("Opkuisen van de matrix")
    sense.clear()
    sys.exit(0)