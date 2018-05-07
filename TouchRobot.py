#!/usr/bin/env python
# coding: Latin-1

# Load library functions we want
from explorerhat import motor
import time

class TouchRobot:
    def __init__(self,downPower,upPower,touchDownTime,touchUpTime):
        self.touchDownTime = touchDownTime
        self.touchUpTime = touchUpTime
	self.downPower = downPower
	self.upPower = upPower

    def move_by_raw(self,power,seconds):
        motor.one.speed(power)
        time.sleep(seconds)
        motor.stop()

    def touch(self):
        self.move_by_raw(self.downPower,self.touchDownTime)
        self.move_by_raw(self.upPower,self.touchUpTime)

    def getTouchTime(self):
        return self.touchDownTime+self.touchUpTime

    def stop(self):
        self.motor.stop()
