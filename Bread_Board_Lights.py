import RPi.GPIO as GPIO
import time

pins = [11, 12, 13, 15, 16, 18, 22, 7]

def setup():
	GPIO.setmode(GPIO.BOARD)
	for pin in pins:
		GPIO.setup(pin, GPIO.OUT)   
		GPIO.output(pin, GPIO.HIGH) 
def loop():
        while True:
                for pin in pins:
                        GPIO.output(pin, GPIO.LOW)
                        time.sleep(0.5)
                        GPIO.output(pin, GPIO.HIGH)

def destroy():
    for pin in pins:
    	GPIO.output(pin, GPIO.HIGH)
GPIO.cleanup()           

if __name__ == '__main__':   
	setup()
	
 
