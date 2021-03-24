import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(16, GPIO.IN)
GPIO.setup(36,GPIO.OUT, initial=GPIO.LOW)

while True:
    print(GPIO.input(16))
    if(GPIO.input(16)== 1):
        GPIO.output(36,1)
        if(GPIO.input(16) == 0)
            time.sleep(5)
            GPIO.output(36,0)
    time.sleep(1)


