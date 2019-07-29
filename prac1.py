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
    GPIO.setup(output_channels, GPIO.IN, initial = GPIO.LOW)#setting up all output GPIOs
    GPIO.setup(inputs_channels, GPIO.OUT, initial = GPIO.LOW)#setting up all input GPIOs
    GPIO
    


# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        binaryString="000"
        print(bin(7)+"")
        #main() #setup gpio ports
        #while True: #loop
            
            
            
	    
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)
