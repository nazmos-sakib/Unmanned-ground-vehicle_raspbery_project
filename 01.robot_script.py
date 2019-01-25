#!/usr/bin/env python3

import time
import RPi.GPIO as GPIO
from gpiozero import Motor
from pynput.keyboard import Key, Listener   #key board realease and press
#import threading

# seting the pins for use!

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

GPIO.cleanup()

motor_left = Motor(forward = 3,backward = 2)
motor_right = Motor(forward = 27,backward = 22)


GPIO.setup(4,GPIO.OUT) #left enabal
GPIO.setup(17,GPIO.OUT)#right enabal


#GPIO.output(4, True)
#GPIO.output(17, True)

def froward():
    motor_left.forward()
    motor_right.forward()
    GPIO.output(4, True)
    GPIO.output(17, True)

def left():
    motor_left.forward()
    GPIO.output(4, True)

def right():
    motor_right.forward()
    GPIO.output(17, True)

def backward():
    motor_left.backward()
    motor_right.backward()
    GPIO.output(4, True)
    GPIO.output(17, True)


def froward_release():
    motor_left.stop()
    motor_right.stop()
    GPIO.output(4, False)
    GPIO.output(17, False)


def left_release():
    motor_left.stop()
    GPIO.output(4, False)


def right_release():
    motor_right.stop()
    GPIO.output(17, True)


def backward_release():
    motor_left.stop()
    motor_right.stop()
    GPIO.output(4, False)
    GPIO.output(17, False)




def on_press(key):
    #print(key)
    asd = str(key)
    
    #print(len(asd),type(asd))
    if (asd == "'w'"):  #forward
        froward()

    if (asd == "'a'"):  #left
        left()

    if (asd == "'s'"):  #right
        right()

    if (asd == "'d'"):  #backward
        backward()
    GPIO.cleanup()



def on_release(key):
    asd = str(key)
    if (asd == "'w'"):  #forward
        froward_release()
        
    if (asd == "'a'"):  #left
        left_release()

    if (asd == "'s'"):  #right
        right_release()

    if (asd == "'d'"):  #backward
        backward_release()

    GPIO.cleanup()
    if key == Key.esc:
        backward_release()
        GPIO.cleanup()
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
