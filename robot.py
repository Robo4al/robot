import _thread

from machine import Pin
from time import sleep
from motor_dc import MotorDC

class Robot4All:

    RUNNING = False
    SLEEP = 1

    def __init__(self):
        self.motor = MotorDC()

    def stop(self):
        self.RUNNING = False
        self.motor.move(0, 0, 0, 0)
        self.thread = None

    def start(self):
        self.RUNNING = True
        self.thread = _thread.start_new_thread(self.run, ())

    def run(self):
        while self.RUNNING:
            # BLOCKLY CODE --------------
            self.motor.move(1, 1, 1, 1)
            # --------------
            sleep(self.SLEEP)

if __name__ == "__main__":
    robot = Robot4All()

    redBtn = Pin(5, Pin.IN)
    redBtn.irq(lambda p: robot.stop())
    
    robot.run()