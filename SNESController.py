#import evdev
from evdev import InputDevice, categorize, ecodes

class SNESController:
    def __init__(self):
        self.gamepad = InputDevice('/dev/input/event0')
	self.initButtonNumbers()
	self.initFunctions()

    def initFunctions(self):
	self.setCallbackFor("A",None)
	self.setCallbackFor("B",None)
        self.setCallbackFor("X",None)
        self.setCallbackFor("Y",None)
	self.setCallbackFor("R1",None)
        self.setCallbackFor("L1",None)
        self.setCallbackFor("START",None)
        self.setCallbackFor("SELECT",None)
        self.setCallbackFor("LEFT",None)
        self.setCallbackFor("RIGHT",None)
        self.setCallbackFor("UP",None)
        self.setCallbackFor("DOWN",None)
        self.setCallbackFor("CENTER",None)
	self.setCallbackFor("RELEASE",None)

    def dummyFunction(self):
	pass

    def initButtonNumbers(self):
        self.aBtn = 289
        self.bBtn = 290
        self.xBtn = 288
        self.yBtn = 291
        self.lBtn = 292
        self.rBtn = 293
        self.selBtn = 296
        self.staBtn = 297

    def setCallbackFor(self, button ,fun = None):
	if fun is None:
	    fun = self.dummyFunction

	if button is "A" :
	    self.aBtnFun = fun
        elif button is "B" : 
	    self.bBtnFun = fun
        elif button is "X" : 
            self.xBtnFun = fun
        elif button is "Y" : 
            self.yBtnFun = fun
        elif button is "R1" : 
            self.r1BtnFun = fun
        elif button is "L1" : 
            self.l1BtnFun = fun
        elif button is "START" : 
            self.startBtnFun = fun
        elif button is "SELECT" : 
            self.selectBtnFun = fun
        elif button is "RELEASE" : 
            self.releaseBtnFun = fun
        elif button is "LEFT" : 
            self.leftBtnFun = fun
        elif button is "RIGHT" : 
            self.rightBtnFun = fun
        elif button is "CENTER" : 
            self.centerBtnFun = fun
        elif button is "DOWN" : 
            self.downBtnFun = fun
        elif button is "UP" : 
            self.upBtnFun = fun

    def press(self, button):
	self.getCallbackFunction(button)()

    def getCallbackFunction(self,button):
	functions = { "A" : self.aBtnFun,
        	      "B" : self.bBtnFun,
                      "X" : self.xBtnFun,
                      "Y" : self.yBtnFun,
                      "R1" : self.r1BtnFun,
                      "L1" : self.l1BtnFun,
                      "START" : self.startBtnFun,
                      "SELECT " : self.selectBtnFun,
                      "RELEASE" : self.releaseBtnFun,
                      "LEFT" : self.leftBtnFun,
                      "RIGHT" : self.rightBtnFun,
                      "CENTER" : self.centerBtnFun,
                      "DOWN" : self.downBtnFun,
		      "UP" : self.upBtnFun,
	}
	return functions[button]



    def listen(self):
        for event in self.gamepad.read_loop():
	    if event.type == ecodes.EV_KEY:
	        if event.value == 1:
        	    if event.code == self.xBtn:
             	        self.press("X")
                    elif event.code == self.bBtn:
                        self.bBtnFun()
                    elif event.code == self.aBtn:
                        self.press("A")
            	    elif event.code == self.yBtn:
                	self.yBtnFun()
            	    elif event.code == self.lBtn:
                	self.l1BtnFun()
            	    elif event.code == self.rBtn:
                	self.r1BtnFun()
            	    elif event.code == self.selBtn:
                	self.selectBtnFun()
            	    elif event.code == self.staBtn:
                	self.startBtnFun()
        	elif event.value == 0:
          	    self.releaseBtnFun()

            elif event.type == ecodes.EV_ABS:
                absevent = categorize(event)
	        if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_X":
        	    if absevent.event.value == 0:
               	        self.leftBtnFun()
             	    elif absevent.event.value == 255:
               	     	self.rightBtnFun()
             	    elif absevent.event.value == 127:
                	self.centerBtnFun()
        	elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_Y":
             	    if absevent.event.value == 0:
                	self.upBtnFun()
             	    elif absevent.event.value == 255:
                	self.downBtnFun()
                    elif absevent.event.value == 127:
                        self.centerBtnFun()
