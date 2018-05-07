import time

class KoTTiming:
    def __init__(self,touchTimeDown,touchTimeUp):
        self.touchTimeDown = touchTimeDown
	self.touchTimeUp = touchTimeUp

    def sleepNormalJumpTime(self):
        time.sleep(.5)

    def sleepOneField(self):
        time.sleep(.3)

    def sleepForJumpOnEndOfField(self):
	time.sleep(.3-self.touchTimeDown)

    def sleepForHighJumpFromCorner(self):
	time.sleep(.2)
