# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

from machine import Pin
from time import sleep

class Main:

    RED_BTN = 5
    GREEN_BTN = 22
    
    robot = None

    def __init__(self):
        self.greenBtn = Pin(self.GREEN_BTN, Pin.IN)
        # self.greenBtn.irq(trigger=Pin.IRQ_RISING, handler=self.start)
        self.greenBtn.irq(lambda p: self.start())

        self.redBtn = Pin(self.RED_BTN, Pin.IN)
        self.redBtn.irq(lambda p: self.stop())

    def start(self):
        if self.robot:
            self.robot.stop()
            self.robot = None
        from robot import Robot4All
        self.robot = Robot4All()
        self.robot.start()

    def stop(self):
        self.robot.stop()

if __name__ == "__main__":
    main = Main()