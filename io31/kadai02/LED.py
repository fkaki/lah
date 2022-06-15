#! usr/bin

from   enum import IntEnum
import RPi.GPIO as GPIO
import time

### define port numbers
def __init__():
    GPIO.setmode(GPIO.BCM) # set GPIO mode

    for pin in LEDPorts: # setup ports
        GPIO.setup(pin, GPIO.OUT)

class LEDPorts(IntEnum):
    GRN = 16
    YLW = 20
    RED = 21    
    
def startBlinking(portNum):
    GPIO.output(portNum, GPIO.HIGH)
    
def stopBlinking():
    for portNum in LEDPorts:
        GPIO.output(portNum, GPIO.LOW)
    
    GPIO.cleanup()
    print("\nStopped!")
