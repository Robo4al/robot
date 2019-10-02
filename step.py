import time
from machine import Pin

class StepMotor:
	
	def __init__(self, PIN1=18, PIN2=19, PIN3=22, PIN4=23):
		self.in1 = Pin(PIN1, Pin.OUT)
		self.in2 = Pin(PIN2, Pin.OUT)
		self.in3 = Pin(PIN3, Pin.OUT)
		self.in4 = Pin(PIN4, Pin.OUT)
	
	'''
	a) phase IN4
	b) phase IN4 and IN3
	c) phase IN3	
	d) phase IN3 and IN2
	e) phase IN2
	f) phase IN2 and IN1
	g) phase IN1
	h) phase IN1 and IN4
	'''
	def step(self, left, sleepMs=5, stepCount=1):
		values = [[0,0,0,1], [0,0,1,1], [0,0,1,0], [0,1,1,0], [0,1,0,0], [1,1,0,0], [1,0,0,0], [0,0,1,1]]
		if left:
			values.reverse()
		for count in range(stepCount):
			for value in values:
				self.in1.value(value[0])
				self.in2.value(value[1])
				self.in3.value(value[2])
				self.in4.value(value[3])
				time.sleep_ms(sleepMs)




motor = StepMotor()
motor.step(False, stepCount=4096)