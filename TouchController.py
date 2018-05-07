import TouchRobot
import KoTTiming
import operator
import time
import SNESController
import ReplayController

gamepad = SNESController.SNESController()
myRobot = TouchRobot.TouchRobot(60,-30,.1,.05)
timings = KoTTiming.KoTTiming(myRobot.touchDownTime,myRobot.touchUpTime)
replay = ReplayController.ReplayController()

def aBtn():
    myRobot.touch()
    replay.add("A")
    replay.printFileEnd(10)

def mainLoop():
    replay.loadFile("replay")
    gamepad.setCallbackFor("A",aBtn)
    gamepad.listen()

    while True:
	command = raw_input("Command: ")
	print("Perform Command: "+str(command))
	performCommand(command)


def performCommand(command):
    print("Perform Command: "+str(command))
    if command == "T":
	for i in range(1):
	    myRobot.touch()
	    time.sleep(.317)
	    myRobot.touch()
	    timings.sleepNormalJumpTime()
	    time.sleep(.8)
	    myRobot.touch()
	    time.sleep(.1)
	    myRobot.touch()
	    time.sleep(1.5)
	    myRobot.touch()
	    time.sleep(1) #ruckweg mitte
            myRobot.touch()
	    time.sleep(1)
	    myRobot.touch()
	    time.sleep(.1)
	    myRobot.touch()
	    timings.sleepNormalJumpTime()
	    myRobot.touch() # links wand
	    timings.sleepNormalJumpTime()
            #time.sleep(1)
	    myRobot.touch()
	    timings.sleepNormalJumpTime()
	    myRobot.touch()
	    timings.sleepNormalJumpTime()
	    myRobot.touch() # mittlere Plattform
            time.sleep(.3*4)
	    myRobot.touch()
	    time.sleep(.2)
	    myRobot.touch()
	    timings.sleepNormalJumpTime()
	    time.sleep(.2)
	    myRobot.touch() #obere plattform
	    timings.sleepNormalJumpTime()
	    time.sleep(.3*3)
	    time.sleep(.2)
	    myRobot.touch()
    if command == "S":
        myRobot.stop()
