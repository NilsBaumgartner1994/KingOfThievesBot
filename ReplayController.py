import os.path

class ReplayController:
    def __init__(self):
	self.name = None

    def fileExists(self,name):
	return os.path.exists("./"+name+".txt")

    def createNewFile(self,name):
        file = open("./"+name+".txt","w")
	file.close()

    def loadFile(self,name):
	self.name = name
        if not self.fileExists(name):
            self.createNewFile(name)

    def add(self,text):
	if self.name is not None:        
	    with open(self.name+".txt","a") as file:
	        file.write(text+"\n")

    def printFileEnd(self,amount):
	if self.name is None:
            return
	num_lines = sum(1 for line in open(self.name+'.txt'))
	self.printFile(num_lines-amount,amount)

    def printFile(self,startLine,amount):
	if self.name is None:
	    return      
	with open(self.name+".txt","r") as file:  
	    print "File: "+file.name
	    for i, line in enumerate(file):
		line = line.strip()
    	        if i >= startLine and i < startLine+amount:
                    print " ("+str(i).zfill(3)+"): "+line
                else:
                   pass
	
	    print "File printed"
