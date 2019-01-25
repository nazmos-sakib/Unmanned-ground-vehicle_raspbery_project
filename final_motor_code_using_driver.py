import time
import RPi.GPIO as GPIO
from gpiozero import Motor

# Next we setup the pins for use!
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

GPIO.setup(4,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
motor = Motor(forward = 27,backward = 22)

'''
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
'''

print('Starting motor sequence!')

GPIO.output(4, True)
GPIO.output(17, True)

try:
    while 1:
        motor.forward()
        time.sleep(5)
        motor.backward()
        time.sleep(5)
except:
    motor.stop()


'''
while True:
  try:
    # Makes the motor spin one way for 3 seconds
    GPIO.output(27, True)
    GPIO.output(22, False)
    time.sleep(5)
    # Spins the other way for a further 3 seconds
    GPIO.output(27, False)
    GPIO.output(22, True)
    time.sleep(3)
  except(KeyboardInterrupt):
    # If a keyboard interrupt is detected then it exits cleanly!
    print('Finishing up!')
    GPIO.output(27, False)
    GPIO.output(22, False)
    #quit()
    break
'''
