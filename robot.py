import _thread

from machine import Pin
from time import sleep

class Robot4All:

    RUNNING = False
    LED = 2
    SLEEP = 1

    def __init__(self):
        self.led = Pin(self.LED, Pin.OUT)
        self.led.value(False)

    def stop(self):
        self.RUNNING = False
        self.led.value(False)

    def start(self):
        self.RUNNING = True
        _thread.start_new_thread(self.run, ())

    def run(self):
        while self.RUNNING:
            sleep(self.SLEEP)
            self.led.value(not self.led.value())

if __name__ == "__main__":
    robot = Robot4All()

    redBtn = Pin(5, Pin.IN)
    redBtn.irq(lambda p: robot.stop())
    
    robot.run()