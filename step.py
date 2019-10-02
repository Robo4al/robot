import time
from machine import Pin

'''
[StepMotor]
Por padrão, ao criar um objeto do tipo StepMotor os pinos utilizados do Roberval serão:

	- PIN1 = 18
	- PIN2 = 19
	- PIN3 = 22
	- PIN4 = 23

* Fases do motor:
	a) phase IN4			= [0,0,0,1]
	b) phase IN4 and IN3	= [0,0,1,1]
	c) phase IN3			= [0,0,1,0]
	d) phase IN3 and IN2	= [0,1,1,0]
	e) phase IN2			= [0,1,0,0]
	f) phase IN2 and IN1	= [1,1,0,0]
	g) phase IN1			= [1,0,0,0]
	h) phase IN1 and IN4	= [1,0,0,1]

* step()

	- Movimento = direita | velocidade = 5ms | passos = 1  
	stepMotor.step(False)  

	- Movimento = direita | velocidade = 10ms | passos = 1
	stepMotor.step(False, 10)  

	- Movimento = esquerda | velocidade = 10ms | passos = 100  
	stepMotor.step(True, 10, 100)  

	- Movimento = direita | velocidade = 5ms | passos = 100  
	stepMotor.step(False, stepCount=100)  

	- Movimento = esquerda | velocidade = 10ms | passos = 1  
	stepMotor.step(True, sleepMs=100) 
'''
class StepMotor:
	
	def __init__(self, PIN1=18, PIN2=19, PIN3=22, PIN4=23):
		self.in1 = Pin(PIN1, Pin.OUT)
		self.in2 = Pin(PIN2, Pin.OUT)
		self.in3 = Pin(PIN3, Pin.OUT)
		self.in4 = Pin(PIN4, Pin.OUT)
	
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



if __name__ == "__main__":
	motor = StepMotor()
	motor.step(False, stepCount=4096)