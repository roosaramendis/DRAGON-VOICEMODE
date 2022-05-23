

import wmi
global p
p = wmi.WMI()


class processlist:
    def __init__(self):
        self.processing_applist = []

    def getprocess(self):
        for process in p.Win32_Process():
            
            if not(process.Name in self.processing_applist):
                self.processing_applist.append(process.Name)
        return self.processing_applist

    def isprocess_runing(self,processname):
        if processname in self.processing_applist:
            print(processname + "is running")



