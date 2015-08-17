from NNet import *

class Anduril():

    def __init__(self):
        self.Net = NNet()
        return 
    
    def init(self,sconfig,classreg = 0, numcores = 1, gradd = 0, costfunc = 0, epoch = 1):
        self.Net.init(sconfig,classreg,numcores,gradd,costfunc,epoch)

    def func_arch(self,flayer):
        if type(flayer) != str:
            print "flayer must be a string"
            return
        else:
            self.Net.func_arch(flayer)
        return

    def load(self,filename, mode = 0, sep1 = ",", sep2 = " "):
        if (type(filename) == str) and (type(mode) == int) and (type(sep1) == str) and (type(sep2) == str):
            self.Net.load(filename,mode,sep1,sep2)
            return
        else:
            print "Invalid input, files not loaded!"
            return;

    def test_file(self,filename, netname = " ", sep1 = ",", sep2 = " "):
        if (type(filename) == str) and (type(netname) == str) and (type(sep1) == str) and (type(sep2) == str):
            self.Net.test_file(filename, netname, sep1, sep2)
            return
        else:
            print "Invalid input type!"
            return

    def train_net(self,lrate, mode = 1, verbose = 1, logfile = " "):
        if (type(lrate) == float) and (type(mode) == int) and (type(verbose) == int) and (type(logfile) == str):
            self.Net.train_net(lrate,mode,verbose,logfile)
            return
        else:
            print "Invalid input, network not trained!"
            return

    def train_rprop(self,mode = 1, verbose = 1, logfile = " ",tmax = 1.0):
        if (type(mode) == int) and (type(verbose) == int) and (type(logfile) == str) and (type(tmax) == float):
            self.Net.train_rprop(mode,verbose,logfile,tmax)
            return
        else:
            print "Invalid input, network not trained!"
            return

    def d_trainrprop(self,mode = 0, verbose = 0, logfile = " ", tmax = 1.0):
        if (type(mode) == int) and (type(verbose) == int) and (type(logfile) == str) and (type(tmax) == float):
            self.Net.d_trainrprop(mode,verbose,logfile,tmax)
            return
        else:
            print "Invalid input, network not trained!"
            return

    def test_net(self,verbose = 0):
        if (type(verbose) == int):
            self.Net.test_net(verbose)
            return
        else:
            print "Invalid input!"
            return

    def savenet(self,netname):
        if (type(netname) == str):
            self.Net.savenet(netname)
            return
        else:
            print "Invalid input, netname must be a string!"
            return

    def loadnet(self,netname):
        if (type(netname) == str):
            self.Net.loadnet(netname)
            return
        else:
            print "Invalid input, netname must be a string!"
            return

    def snets(self):
        self.Net.snets()
        return
