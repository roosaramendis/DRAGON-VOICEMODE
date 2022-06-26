

import wmi
import time
global p
p = wmi.WMI()


class processlist:
    def __init__(self):
        self.processing_applist = []

    def getprocess(self,delaytime=0.01):
        for process in p.Win32_Process():
            time.sleep(delaytime)
            if not(process.Name in self.processing_applist):
                self.processing_applist.append(process.Name)
        return self.processing_applist

    def isprocess_runing(self,processname):
        self.getprocess()
        print(str(self.processing_applist))
        if processname in self.processing_applist:
            print(processname + "is running")
            return True
        else:
            return False    



