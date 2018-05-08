import os.path

class ReplayController:
    def __init__(self):
        self.name = None
        self.cursor = 0

    def setCursor(self,value):
        if value < 0:
            value = 0
        self.cursor = value

    def up(self):
        self.setCursor(self.cursor+1)

    def down(self):
        self.setCursor(self.cursor-1)

    def fileExists(self,name):
        return os.path.exists("./"+name+".txt")

    def clearFile(self):
        if self.name is not None:
            self.createNewFile(self.name)

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

    def changeLine(self, line_num, text):
        if self.name is None:
            return
        file = open(self.name+".txt","r")
        lines = file.read().splitlines()
        lines[line_num] = text
        file.close()
        file = open(self.name+".txt","w")
        file.write("\n".join(lines))    
        file.close()
        
    def deleteLine(self, line_num):
        if self.name is None:
            return
        file = open(self.name+".txt","r")
        lines = file.read().splitlines()
        file.close()
        self.clearFile()
        for i, line in enumerate(lines):
            if(i is not line_num):
                self.add(line)        

    def printFileEnd(self,amount):
        if self.name is not None:
            num_lines = sum(1 for line in open(self.name+'.txt'))
            self.printFile(num_lines-amount,amount)

    def printFileEdit(self):
        amount = 10
        startLine = self.cursor / amount
        self.printFile(startLine,amount,self.cursor)

    def printFile(self,startLine,amount, cursor = -1):
        if self.name is None:
            return      
        with open(self.name+".txt","r") as file:  
            print "File: "+file.name
            for i, line in enumerate(file):
                line = line.strip()
                if i >= startLine and i < startLine+amount:
                    if(i==cursor):
                        print(">("+str(i).zfill(3)+"): "+line)
                    else:
                        print(" ("+str(i).zfill(3)+"): "+line)
                else:
                   pass
    
        print "File printed"
