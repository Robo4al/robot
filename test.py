from time import sleep
from machine import Pin, PWM

print('eita')

IN1=18
IN2=19
IN3=22
IN4=23

led = Pin(2, Pin.OUT)

in1 = Pin(IN1, Pin.OUT)
in2 = Pin(IN2, Pin.OUT)
in3 = Pin(IN3, Pin.OUT)
in4 = Pin(IN4, Pin.OUT)

in1.value(0)
in2.value(1)
in3.value(1)
in4.value(0)

while True:
    sleep(1)
    led.value(not led.value())