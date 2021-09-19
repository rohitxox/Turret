from ServoPWM import pwm
from pyPS4Controller.controller import Controller
import time
from time import sleep
from motor import *


in1 = 14
in2 = 15
en = 4
temp1=1
x = 375
y = 375


servo_min = 150
servo_max = 600
joy_stick = 32767


pwm.set_pwm(1, 0, 375)
pwm.set_pwm(2, 0, 375)
pwm.set_pwm(3, 0, 170)



print("""
      Turret commands:
      up; down: left; right arrows to control pitch and yaw
      X; initiate motor
      R2; trigger
      L2; Reload
      option; exit
      
      
      """)


class MyController(Controller):
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)


#For the motor
    def on_x_press(self):
        p.ChangeDutyCycle(50)
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        #pass
        
    
    def on_L2_press(self, value):
        p.ChangeDutyCycle(70)
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
    
    
    def on_L2_release(self):
        sleep(1)
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW) 
    
    def on_R2_press(self, value):
        pwm.set_pwm(3, 0, 430)

        
    
    def on_R2_release(self):
        print("Missile unleashed")
        sleep(1)
        pwm.set_pwm(3, 0, 170)
        print("Reload")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)       
        #GPIO.cleanup()
    
    

    def on_left_arrow_press(self):
        z1 = 1
        #print(z)
        if z1 == 1:
            global x
            x += 7
            #print(x)
            pwm.set_pwm(1, 0, x)
        
            
    
    def on_right_arrow_press(self):
        z2 = 1
        #print(z)
        if z2 == 1:
            global x
            x -= 7
            #print(x)
            pwm.set_pwm(1, 0, x)
            
            
    def on_up_arrow_press(self):
        z3 = 1
        #print(z)
        if z3 == 1:
            global y
            y -= 7
            print(y)
            pwm.set_pwm(4, 0, y)
        #pulse = round((y / 4096) * 1000)
        #print(pulse)            
            
    def on_down_arrow_press(self):
        z4 = 1
        #print(z)
        if z4 == 1:
            global y
            y += 7
            print(y)
            pwm.set_pwm(4, 0, y)  
        #pulse = round((y / 4096) * 1000)
        #print(pulse)  
    
    def on_options_press(self):
        #pwm.set_pwm(2, 0, 375-(90+20))
        GPIO.cleanup()
        exit()
            
    def on_share_press(self):
        pwm.set_pwm(2, 0, 375-(90+20))
    
    
    def on_share_release(self):
        pass
        
    def on_up_down_arrow_release(self):
        pass
    
    
    def on_left_right_arrow_release(self):
        pass


controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.listen()
