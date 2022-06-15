#! /usr/bin/python3

from . import LED
import sys

args = sys.argv

def main():
    print("\nStarted!\nPress \"Ctrl + C\" to stop.")
    arg = int(args[1]) + 0
    print("\nThe number is: " + str(arg) + "\n")
    
    while 0 <= arg:
        if arg & 4 == 1:
            LED.startBlinking(LED.LEDPorts.GRN)
        if arg & 2 == 1:
            LED.startBlinking(LED.LEDPorts.YLW)
        if arg & 1 == 1:
            LED.startBlinking(LED.LEDPorts.RED)

LED.stopBlinking()

if __name__ == "__main__":
    LED.__init__()
    main()
