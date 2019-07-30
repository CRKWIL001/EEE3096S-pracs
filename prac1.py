#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: William Crake
Student Number: CRKWIL001
Prac: 1
Date: 29/07/2019
"""

# import Relevant Librares
import RPi.GPIO as GPIO
import time
# Logic that you write

def main():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    output_channels = [11, 13, 15] #LEDS
    input_channels = [16, 18] #switches
    GPIO.setup(output_channels, GPIO.OUT, initial = GPIO.LOW)#setting up all output GPIOs
    GPIO.setup(input_channels, GPIO.IN, pull_up_down = GPIO.PUD_UP)#setting up all input GPIOs

    GPIO.add_event_detect(16, GPIO.FALLING, callback = increment, bouncetime = 200)
    GPIO.add_event_detect(18, GPIO.FALLING, callback = decrement, bouncetime = 200)
def increment(channel):
    global count
    if (count<=6):
        count = count+1
    else:
        count = 0
    led()

def decrement(channel):
    global count
    if ((count)>=1):
        (count)-=1
    else:
        (count)=7
    led()

def led():
    global count
    binaryString = bin(count)[2:].zfill(3)
    if GPIO.input(11)!=int(binaryString[2:]):
        GPIO.output(11, not(GPIO.input(11)))
    if GPIO.input(13)!=int(binaryString[1:2]):
        GPIO.output(13, not(GPIO.input(13)))
    if GPIO.input(15)!=int(binaryString[0:1]):
        GPIO.output(15, not(GPIO.input(15)))


# Only run the functions if
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        count = 0
        main()
        while True:
            time.sleep(.3)
		#loop
             #setup gpio ports
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    #except e:
     #   GPIO.cleanup()
      #  print("Some other error occurred")
       # print(e.message)
