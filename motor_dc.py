from machine import Pin, PWM

'''
motorX = 0 -> parado; motorX = 1 -> movimentando
sentidoX = 0 -> frente; sentidoX = 1 -> tras
MAPEAMENTO:
0000 -> 1111 -> A parado, B parado
0001 -> 1111 -> A parado, B parado
0010 -> 1110 -> A parado, B frente
0011 -> 1101 -> A parado, B tras
0100 -> 1111 -> A parado, B parado
0101 -> 1111 -> A parado, B parado
0110 -> 1110 -> A parado, B frente
0111 -> 1101 -> A parado, B tras
1000 -> 1111 -> A parado, B parado
1001 -> 1111 -> A parado, B parado
1010 -> 0101 -> A frente, B frente
1011 -> 0110 -> A frente, B tras
1100 -> 1011 -> A tras, B parado
1101 -> 1011 -> A tras, B parado
1110 -> 1001 -> A tras, B frente
1111 -> 1010 -> A tras, B tras
'''

class MotorDC:

	def __init__(self, IN1=18, IN2=19, IN3=22, IN4=23, PW1=5, PW2=21):
		self.in1 = Pin(IN1, Pin.OUT)
		self.in2 = Pin(IN2, Pin.OUT)
		self.in3 = Pin(IN3, Pin.OUT)
		self.in4 = Pin(IN4, Pin.OUT)
		self.pw1 = PWM(Pin(PW1, Pin.OUT))
		self.pw2 = PWM(Pin(PW2, Pin.OUT))

	def move(self, motorA=1, sentidoA=0, motorB=1, sentidoB=0, pwm=0, freq=1000, duty=1000):
		values = [[1,1,1,1], [1,1,1,1], [1,1,1,0], [1,1,0,1], [1,1,1,1], [1,1,1,1], [1,1,1,0], [1,1,0,1], [1,1,1,1], [1,1,1,1], [0,1,0,1], [0,1,1,0], [1,0,1,1], [1,0,1,1], [1,0,0,1], [1,0,1,0]]
		x = (motorA*8) + (sentidoA*4) + (motorB*2) + (sentidoB*1)

		if pwm:
			self.pw1.freq(freq)
			self.pw1.duty(duty)
			self.pw2.freq(freq)
			self.pw2.duty(duty)

		self.in1.value(values[x][0])
		self.in2.value(values[x][1])
		self.in3.value(values[x][2])
		self.in4.value(values[x][3])