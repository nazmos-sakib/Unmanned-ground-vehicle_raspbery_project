#!/usr/bin/env python3

from time import sleep
import RPi.GPIO as GPIO
from gpiozero import Motor
from pynput.keyboard import Key, Listener   #key board realease and press
#import threading

# seting the pins for use!

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

#GPIO.cleanup()

motor_right = Motor(forward = 3,backward = 2)
motor_left = Motor(forward = 27,backward = 22)


GPIO.setup(14,GPIO.OUT) #right enabal
GPIO.setup(17,GPIO.OUT)#left enabal


#GPIO.output(14, True)
#GPIO.output(17, True)


def froward():
    print("moving forward")
    motor_left.forward()
    motor_right.forward()
    GPIO.output(14, True)
    GPIO.output(17, True)

def left():
    print("moving left")
    motor_left.forward()
    GPIO.output(17, True)

def right():
    print("moving right")
    motor_right.forward()
    GPIO.output(14, True)

def backward():
    print("moving backward")
    motor_left.backward()
    motor_right.backward()
    GPIO.output(14, True)
    GPIO.output(17, True)


def froward_release():
    print("froward moving stop")
    motor_left.stop()
    motor_right.stop()
    GPIO.output(14, False)
    GPIO.output(17, False)


def left_release():
    print("left moving stop")
    motor_left.stop()
    GPIO.output(17, False)


def right_release():
    print("right moving stop")
    motor_right.stop()
    GPIO.output(14, False)


def backward_release():
    print("backward moving stop")
    motor_left.stop()
    motor_right.stop()
    GPIO.output(14, False)
    GPIO.output(17, False)




def on_press(key):
    #print(key)
    asd = str(key)
    
    #print(len(asd),type(asd))
    if (asd == "'w'"):  #forward
        froward()

    if (asd == "'a'"):  #left
        left()

    if (asd == "'d'"):  #right
        right()

    if (asd == "'s'"):  #backward
        backward()
    #GPIO.cleanup()



def on_release(key):
    asd = str(key)
    if (asd == "'w'"):  #forward
        froward_release()
        
    if (asd == "'a'"):  #left
        left_release()

    if (asd == "'d'"):  #right
        right_release()

    if (asd == "'s'"):  #backward
        backward_release()

    #GPIO.cleanup()
    if key == Key.esc:
        backward_release()
        #GPIO.cleanup()
        # Stop listener
        return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()



'''
try:
    while 1:
        a = raw_input()
        if (a = 'w'):
            froward()
        elif (a = 'a'):
            left()
        elif (a = 'd'):
            right()
        elif (a = 's'):
            backward()
        else:
            motor_left.stop()
            motor_right.stop()

except:
    motor_left.stop()
    motor_right.stop()
    GPIO.output(4, False)
    GPIO.output(17, False)
'''

GPIO.cleanup()
