from sense_hat import SenseHat
from random import randint
from time import sleep
import sys

sense = SenseHat()

def set_random_color():
    return [randint(0,255), randint(0,255), randint(0,255)]

def main():
    letters = input("Enter your text: ")
    intervalBetween = int(input("How long do you want each letter to show? "))
    intervalAfter = int(input("How long do you want to wait after the last letter? "))

    while True:
        for letter in letters:
            sense.show_letter(letter, set_random_color())
            sleep(intervalBetween)
        sense.clear()
        sleep(intervalAfter)
    
try:
    main()
except (KeyboardInterrupt, SystemExit):
    print("Programma sluiten")
finally:
    print("Opkuisen van de matrix")
    sense.clear()
    sys.exit(0)