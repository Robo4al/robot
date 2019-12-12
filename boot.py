# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

from machine import Pin
from time import sleep
from motor_dc import MotorDC

class Main:

    LED_LEFT = 25
    LED_RIGHT = 33

    RED_BTN = 26
    GREEN_BTN = 27
    
    ROBOT = None

    STOPPED = True
    FTP_LOOP = False

    def __init__(self):
        self.ledLeft = Pin(self.LED_LEFT, Pin.OUT)
        self.ledRight = Pin(self.LED_RIGHT, Pin.OUT)
        # Control
        self.greenBtn = Pin(self.GREEN_BTN, Pin.IN)
        self.redBtn = Pin(self.RED_BTN, Pin.IN)
        # Loop
        self.run()

    def run(self):
        while True:
            # Start btn
            if not self.greenBtn.value():
                self.start()
            
            # Stop btn
            if not self.redBtn.value():
                self.stop()

                if self.STOPPED and self.FTP_LOOP:
                    self.FTP_LOOP = False
                elif self.STOPPED:
                    self.FTP_LOOP = True
                else:
                    self.STOPPED = True
            
            # FTP
            self.ledLeft.value(self.STOPPED)
            self.ledRight.value(self.FTP_LOOP)
            
            sleep(.3)


    def start(self):
        self.STOPPED = False
        if self.ROBOT:
            self.ROBOT.stop()
        self.ROBOT = None
        
        from ROBOT import Robot4All
        self.ROBOT = Robot4All()
        self.ROBOT.start()

    def stop(self):
        self.ROBOT.stop()

if __name__ == "__main__":
    main = Main()