from sense_hat import SenseHat
from random import randint
from time import sleep
import sys

sense = SenseHat()

letters = ["N", "M", "D"]

def set_random_color():
    randomRed = randint(0,256)
    randomGreen = randint(0,256)
    randomBlue = randint(0,256)
    return [randomRed, randomGreen, randomBlue]

def main():
    while True:
        for letter in letters:
            sense.show_letter(letter, set_random_color())
            sleep(1)
        sense.clear()
        sleep(3)
    
try:
    main()
except (KeyboardInterrupt, SystemExit):
    print("Programma sluiten")
finally:
    print("Opkuisen van de matrix")
    sense.clear()
    sys.exit(0)
