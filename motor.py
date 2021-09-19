import time
import RPi.GPIO as GPIO
from time import sleep

in1 = 14
in2 = 15
en = 4
temp1=1
laser =18


#///motor
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(laser, GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(laser, GPIO.LOW)
p=GPIO.PWM(en,1000)
p.start(100)
p.ChangeDutyCycle(100)  
#GPIO.cleanup()



