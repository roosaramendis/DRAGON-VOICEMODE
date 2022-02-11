# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'voice mode.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from time import time
from PyQt5 import QtCore, QtGui, QtWidgets
import os
from PyQt5.QtCore import QSettings
import pathlib
import sounddevice as sd
import pyaudio
import audio
import re
import pickle
import globle_key_listener
import mic_to_output
import time


global mydir
mydir = os.path.dirname(os.path.realpath(__file__))
global audiofiledir
audiofiledir = [""]
global userpath
userpath =os.path.expanduser('~')
global selectedaudios
selectedaudios = []
global deviceslistin
deviceslistin =[]
global deviceslistout
deviceslistout =[]
global deviceslist
deviceslist =[]
global hotkeydict
hotkeydict ={}
global selectedoutputdevicetext
selectedoutputdevicetext = ['']
global selectedinputdevicetext
selectedinputdevicetext = ['']
global modifirekeyslist
modifirekeyslist = ['Key.alt_l','Key.alt_gr']
global isaudioplaying
isaudioplaying = [False]
global hearituselfcalledtimes
hearituselfcalledtimes = [0]
global stopstreaminmicintoout
stopstreaminmicintoout  = [False]
global overridehearuselfdevice
overridehearuselfdevice = [0]
global hearmyselfdevice
hearmyselfdevice = ['']
global hearmyselfvolume
hearmyselfvolume = [1]

def setisaudioplaying(isplaying):
    isaudioplaying.clear()
    isaudioplaying.append(isplaying)
    print(str(isaudioplaying[0])+" here")

def getstopstreaminmicintoout():
    print(stopstreaminmicintoout[0])
    return stopstreaminmicintoout[0]


class playaudio_thread(QtCore.QThread):
    
    def __init__(self,selecetedfilepath,deviceindex, parent=None):
        super(playaudio_thread,self).__init__(parent)
        self.selecetedfilepath = selecetedfilepath
        self.deviceindex = deviceindex
    def run(self):
        audio.playaudio_class().playaudio(self.selecetedfilepath,self.deviceindex,1024)    

class hearituself_thread(QtCore.QThread):
    suicidefunc = QtCore.pyqtSignal(str)
    def __init__(self,selectedinputdevice,selectedoutputdevice,volume, parent=None):
        super(hearituself_thread,self).__init__(parent)
        self.selectedinputd = selectedinputdevice
        self.selectedoutputd =selectedoutputdevice
        self.volume =volume
    def run(self):
        
        while True:
            time.sleep(0.5)
            #print(str(audio.getisaudioplaying())+" in while")
            if audio.playaudio_class().getisaudioplaying() == True:
                
                hearituselfcalledtimes[0] += 1
                print("hearit u self started") 
                if hearituselfcalledtimes[0] <2: 
                    try:
                        mic_to_output.startmictooutputcall(self.selectedinputd,self.selectedoutputd,self.volume/100)
                    except:
                        print("print err") 
            else:            
                hearituselfcalledtimes[0] = 0
                #print(str(hearituselfcalledtimes[0])+"hearituself called times")
                stopstreaminmicintoout[0] = True
                mic_to_output.stopmictoinput()
                #self.suicidefunc.emit("terminate")
class mictoout_thread(QtCore.QThread):
    
    def __init__(self,selectedinputdevice,selectedoutputdevice, parent=None):
        super(mictoout_thread,self).__init__(parent)
        self.selectedinputd = selectedinputdevice
        self.selectedoutputd =selectedoutputdevice
    def run(self):
        try:
            mic_to_output.startmictooutput(self.selectedinputd,self.selectedoutputd)
        except:
            print("print err")    

class gblkeylistener_thread(QtCore.QThread):
    
    def __init__(self, parent=None):
        super(gblkeylistener_thread,self).__init__(parent)
    def run(self):
        try:
            globle_key_listener.starlistener(hotkeydict,deviceslist.index(selectedoutputdevicetext[0]))
        except:
            pass
class Ui_voicemode(object):
    def setupUi(self, voicemode):
        voicemode.setObjectName("voicemode")
        voicemode.resize(642, 540)
        self.makesettingvals()        
        self.setdefsettingvals()
        self.getsettingvals()
        print(selectedoutputdevicetext[0])
        try:
            datainfile = pickle.load(open(mydir+"/"+"saves/hotkeys.dvm","rb")) #read data in file
            print(datainfile)
            hotkeydictinfile = datainfile
            hotkeydict.update(hotkeydictinfile)
            print(hotkeydict)
        except:
            pass
        self.centralwidget = QtWidgets.QWidget(voicemode)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 651, 461))
        self.tabWidget.setObjectName("tabWidget")
        self.soundboard = QtWidgets.QWidget()
        self.soundboard.setObjectName("soundboard")
        self.asinghk = QtWidgets.QPushButton(self.soundboard)
        self.asinghk.setGeometry(QtCore.QRect(10, 10, 121, 41))
        self.asinghk.setObjectName("asinghk")
        self.asinghk.clicked.connect(self.asinghk_clk)
        self.comboBox = QtWidgets.QComboBox(self.soundboard)
        self.comboBox.setGeometry(QtCore.QRect(10, 60, 51, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit = QtWidgets.QLineEdit(self.soundboard)
        self.lineEdit.setGeometry(QtCore.QRect(90, 60, 41, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.soundboard)
        self.label.setGeometry(QtCore.QRect(70, 60, 16, 21))
        self.label.setObjectName("label")
        self.removehk = QtWidgets.QPushButton(self.soundboard)
        self.removehk.setGeometry(QtCore.QRect(10, 90, 121, 41))
        self.removehk.setObjectName("removehk")
        self.repeat = QtWidgets.QCheckBox(self.soundboard)
        self.repeat.setGeometry(QtCore.QRect(10, 140, 101, 17))
        self.repeat.setObjectName("repeat")
        self.listView = QtWidgets.QListView(self.soundboard)
        self.listView.setGeometry(QtCore.QRect(180, 10, 450, 400))
        self.listView.setObjectName("listView")
        self.refreshlist = QtWidgets.QPushButton(self.soundboard)
        self.refreshlist.setObjectName(u"refreshlist")
        self.refreshlist.setGeometry(QtCore.QRect(10, 160, 121, 23))
        self.refreshlist.clicked.connect(self.refreshlistfunc)
        self.tabWidget.addTab(self.soundboard, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalSlider = QtWidgets.QSlider(self.tab_2)
        self.horizontalSlider.setGeometry(QtCore.QRect(10, 30, 451, 22))
        self.horizontalSlider.setMaximum(200)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.sampelrate = QtWidgets.QLabel(self.tab_2)
        self.sampelrate.setGeometry(QtCore.QRect(10, 0, 151, 21))
        self.sampelrate.setObjectName("sampelrate")
        self.tabWidget.addTab(self.tab_2, "")
        voicemode.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(voicemode)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 642, 21))
        self.menubar.setObjectName("menubar")
        self.about = QtWidgets.QMenu(self.menubar)
        self.about.setObjectName("about")
        voicemode.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(voicemode)
        self.statusbar.setObjectName("statusbar")
        voicemode.setStatusBar(self.statusbar)
        self.menubar.addAction(self.about.menuAction())
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QtCore.QRect(10, 70, 451, 21))
        self.label_2.setText(audiofiledir[0])
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QtCore.QRect(10, 470, 31, 21))
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QtCore.QRect(326, 470, 41, 21))
        self.openaudiopath = QtWidgets.QPushButton(self.tab_2)
        self.openaudiopath.setObjectName(u"openaudiopath")
        self.openaudiopath.setGeometry(QtCore.QRect(490, 70, 121, 23))
        self.openaudiopath.clicked.connect(self.getaudiofiledir)
        self.inputdevice = QtWidgets.QComboBox(self.centralwidget)
        self.inputdevice.setObjectName(u"inputdevice")
        self.inputdevice.setGeometry(QtCore.QRect(50, 470, 261, 22))
        self.outputdevice = QtWidgets.QComboBox(self.centralwidget)
        self.outputdevice.setObjectName(u"outputdevice")
        self.outputdevice.setGeometry(QtCore.QRect(370, 470, 261, 22))
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QtCore.QRect(10, 140, 261, 21))
        self.hearmyselfdevice = QtWidgets.QComboBox(self.tab_2)
        self.hearmyselfdevice.setObjectName(u"hearmyselfdevice")
        self.hearmyselfdevice.setGeometry(QtCore.QRect(290, 140, 321, 22))
        self.overridehearuselfdevice = QtWidgets.QCheckBox(self.tab_2)
        self.overridehearuselfdevice.setObjectName(u"overridehearuselfdevice")
        self.overridehearuselfdevice.setGeometry(QtCore.QRect(10, 110, 191, 17))
           
        self.play = QtWidgets.QPushButton(self.soundboard)
        self.play.setObjectName(u"play")
        self.play.setGeometry(QtCore.QRect(10, 190, 41, 23))
        self.play.clicked.connect(self.play_clk)
        self.stop = QtWidgets.QPushButton(self.soundboard)
        self.stop.setObjectName(u"stop")
        self.stop.setGeometry(QtCore.QRect(90, 190, 41, 23))
        self.stop.clicked.connect(self.stop_clk)
        print(audiofiledir[0])
        self.getaudiolist()
        self.getaudiodevices()
        
        try:
            print(selectedoutputdevicetext[0])
            self.outputdevice.setCurrentText(selectedoutputdevicetext[0])
        except:
            pass
        self.outputdevice.currentTextChanged.connect(self.setdeviceindexfunc)
        try:
            print(selectedinputdevicetext[0])
            self.inputdevice.setCurrentText(selectedinputdevicetext[0])
        except:
            pass
        try:
            if overridehearuselfdevice[0] == 0:
                self.overridehearuselfdevice.setChecked(False)
            elif overridehearuselfdevice[0] == 2:
                self.overridehearuselfdevice.setChecked(True)
        except:
            pass
        self.overridehearuselfdevice.stateChanged.connect(self.setoverridehearuselfval)        
        try:
            self.hearmyselfdevice.setCurrentText(hearmyselfdevice[0])
        except:
            pass
        try:
            self.horizontalSlider.setValue(hearmyselfvolume[0])
        except:
            pass
        self.horizontalSlider.valueChanged.connect(self.sethearmyselfvolumeval)
        self.sampelrate.setText('hear my self volume '+str(self.horizontalSlider.value()))    
        self.hearmyselfdevice.currentTextChanged.connect(self.sethearmyselfdeviceval)   
        self.inputdevice.currentTextChanged.connect(self.setindeviceindexfunc)  
        self.retranslateUi(voicemode)
        self.tabWidget.setCurrentIndex(0)
        self.hotkeylistenercall()
        self.mictooutputcall()
        self.hearituself()
        QtCore.QMetaObject.connectSlotsByName(voicemode)


    def hearituself(self):
        if overridehearuselfdevice[0] == 2:
            self.thread3 = hearituself_thread(selectedinputdevice=deviceslist.index(sd.query_devices(kind='input')['name']),selectedoutputdevice=deviceslist.index(hearmyselfdevice[0]),volume=self.horizontalSlider.value())
        if overridehearuselfdevice[0] == 0:
            self.thread3 = hearituself_thread(selectedinputdevice=deviceslist.index(sd.query_devices(kind='input')['name']),selectedoutputdevice=deviceslist.index(sd.query_devices(kind='output')['name']),volume=self.horizontalSlider.value())    
        self.thread3.start()
        self.thread3.suicidefunc.connect(self.stophearituself)

    def stophearituself(self,msg):
        print(msg)
        self.thread3.setTerminationEnabled(True)
        self.thread3.terminate()
        #time.sleep(0.5)
        #self.hearituself()

    def mictooutputcall(self):
        try:
            self.thread2 = mictoout_thread(selectedinputdevice=deviceslist.index(selectedinputdevicetext[0]),selectedoutputdevice=deviceslist.index(selectedoutputdevicetext[0]))
            self.thread2.start()
        except:
            pass

    def hotkeylistenercall(self):
        self.thread1 = gblkeylistener_thread()
        self.thread1.start()

    def makesettingvals(self):
        self.settingval = QSettings("Dragon Voide Mode","settings vals")

    def setdefsettingvals(self):
        settingkeylist = self.settingval.allKeys()
        #print(str(len(settingkeylist)))
        if(settingkeylist == None):
            print("making regedit")
            self.settingval.setValue("audio path",userpath+"/Music")
            self.settingval.setValue("selectedoutputdevicetext",0)
            self.settingval.setValue("selectedinputdevicetext",0)
            self.settingval.setValue("overridehearuselfdevice",0)
            self.settingval.setValue("hearmyselfdevice",0)
            self.settingval.setValue("hearmyselfvolume",100)
        
        elif len(settingkeylist)==0:
            print("set def val")
            self.settingval.setValue("audio path",userpath+"/Music")
            self.settingval.setValue("selectedoutputdevicetext",0)
            self.settingval.setValue("selectedinputdevicetext",0)
            self.settingval.setValue("overridehearuselfdevice",0)
            self.settingval.setValue("hearmyselfdevice",0)
            self.settingval.setValue("hearmyselfvolume",100)

    def getsettingvals(self):
        self.settingval = QSettings("Dragon Voide Mode","settings vals")
        audiofiledir[0] = str(self.settingval.value("audio path"))
        selectedoutputdevicetext[0] = self.settingval.value("selectedoutputdevicetext")
        selectedinputdevicetext[0] = self.settingval.value("selectedinputdevicetext")
        overridehearuselfdevice[0] = self.settingval.value("overridehearuselfdevice")
        hearmyselfdevice[0] = self.settingval.value("hearmyselfdevice")
        hearmyselfvolume[0] = self.settingval.value("hearmyselfvolume")


    def setsettingvals(self):
        self.settingval = QSettings("Dragon Voide Mode","settings vals")
        self.settingval.setValue("selectedoutputdevicetext",selectedoutputdevicetext[0])
        self.settingval.setValue("selectedinputdevicetext",selectedinputdevicetext[0])

    def getaudiofiledir(self):
        audiofiledir[0] = QtWidgets.QFileDialog.getExistingDirectory(None, 'audio folder path',mydir)
        self.label_2.setText(audiofiledir[0])
        self.settingval.setValue("audio path",audiofiledir[0])

    def getaudiolist(self):
        list_of_files = []
        list_of_Afiles = []
        for root, dirs, files in os.walk(audiofiledir[0]):
            for file in files:
                list_of_files.append(os.path.join(root,file))

        for i in list_of_files:
            file_extension = pathlib.Path(i).suffix
            print("File Extension: ", file_extension)
            if file_extension == ".wav" or file_extension == ".mp3":
                list_of_Afiles.append(i)
        self.listviwer(list_of_Afiles)    
    
    def listviwer(self,afilelist):
        """this func getting key of videodic and creating listview with checkbox"""
        global model
        model = QtGui.QStandardItemModel()
        for i in afilelist:
            print(i)
            item = QtGui.QStandardItem(i)
            check = QtCore.Qt.Checked = False
            item.setCheckState(check)
            item.setText(str(i))
            print(item.text()+" lisetview"+" "+str(item.checkState()))
            item.setCheckable(True)
            model.appendRow(item)
            print(model)
        self.listView.setModel(model)                        

    def refreshlistfunc(self):
        self.getaudiolist()

    def getaudiodevices(self):
        print("gettting audio devices")
        p = pyaudio.PyAudio()
        #deviceslist = []
        deviceslist.clear()
        for i in sd.query_devices():
            deviceslist.append(i['name'])
        #print(sd.query_devices(kind='input'))
        self.hearmyselfdevice.addItems(deviceslist)
        for i in range(len(deviceslist)):
            try:
                if sd.query_devices(i,'input')['max_input_channels']>0:
                    #print(sd.query_devices(i,'input')['name'])
                    deviceslistin.append(sd.query_devices(i,'input')['name'])
            except:
                pass
        print(deviceslistin)        
        for i in range(len(deviceslist)):
                
            try:
                if sd.query_devices(i,'output')['max_output_channels']>0:
                    #print(sd.query_devices(i,'output')['name'])
                    deviceslistout.append(sd.query_devices(i,'output')['name'])
            except:
                pass    
        print(deviceslistout)            
        self.inputdevice.addItems(deviceslistin)
        self.outputdevice.addItems(deviceslistout)

    def play_clk(self):
        try:
            self.getcheckditems(model)
            print(selectedaudios)
            selecetedfilepath = selectedaudios[0].replace('\\','/')
            print(selecetedfilepath)
            self.thread4 = playaudio_thread(selecetedfilepath,deviceslist.index(self.outputdevice.currentText()))
            self.thread4.start()
        except:
            pass    
        #audio.playaudio(selecetedfilepath,deviceslist.index(self.outputdevice.currentText()),1024)
    def stop_clk(self):
        pyaudio.PyAudio().__getattribute__('streams')
        audio.playaudio_class().stopstream()
        self.thread4.setTerminationEnabled(True)
        self.thread4.terminate()
            
           
    def getcheckditems(self,models):
        selectedaudios.clear()
        for index in range(models.rowCount()):
            item = models.item(index)
            print(str(QtCore.Qt.Checked))
            if item.checkState() != QtCore.Qt.Checked:
                print(item.text()+" getcheck"+" "+str(item.checkState()))
                i = item.text()
                selectedaudios.append(i)
                #selectedvideos.append(item.text()    
        print(selectedaudios)
    
    def setdeviceindexfunc(self,text):
        print(text)
        dtext = selectedoutputdevicetext[0]
        if text in deviceslist:
            dtext = text
            print("index of text"+str(dtext))
        selectedoutputdevicetext[0] = dtext
        self.setsettingvals() 

    def setindeviceindexfunc(self,text):
        print(str(type(deviceslist)))
        dtext = selectedinputdevicetext[0]
        if text in deviceslist:
            dtext = text
            print("index of text"+str(dtext))
        selectedinputdevicetext[0] = dtext
        
        self.setsettingvals()

    def asinghk_clk(self):
        hkstr = self.lineEdit.text()
        print(hkstr)
        newhklist =[modifirekeyslist[self.comboBox.currentIndex()],hkstr]
        print(newhklist)
        newhk = newhklist[0]+"+"+newhklist[1]
        self.getcheckditems(model)
        hotkeydict[str(newhk)] = selectedaudios[0]
        print(hotkeydict)
        print("save kotkeys in to HDD")
        print(mydir)
        path =  mydir+"/saves"
        if os.path.exists(path)==False:
            print("not exist have to create")  
            os.mkdir(path)
            pickle.dump((hotkeydict),open(path+"/hotkeys"+".dvm","wb"))
            print("saving to "+str(path))
        else:
            pickle.dump((hotkeydict),open(path+"/hotkeys"+".dvm","wb"))
            print("saving to "+str(path))

    def setoverridehearuselfval(self,bval):

        print(bval)
        self.settingval.setValue("overridehearuselfdevice",bval)

    def sethearmyselfdeviceval(self,text):
        print(text)
        self.settingval.setValue("hearmyselfdevice",text)

    def sethearmyselfvolumeval(self):
        self.settingval.setValue("hearmyselfvolume",self.horizontalSlider.value())
        self.sampelrate.setText('hear my self volume '+str(self.horizontalSlider.value()))

    def retranslateUi(self, voicemode):
        _translate = QtCore.QCoreApplication.translate
        voicemode.setWindowTitle(_translate("voicemode", "DRAGON VOICE MODE"))
        self.asinghk.setText(_translate("voicemode", "Add Hot Key"))
        self.comboBox.setItemText(1, _translate("voicemode", "alt_r"))
        self.comboBox.setItemText(0, _translate("voicemode", "alt_l"))
        self.label.setText(_translate("voicemode", "+"))
        self.removehk.setText(_translate("voicemode", "Remove Hot Key"))
        self.repeat.setText(_translate("voicemode", "repeat"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.soundboard), _translate("voicemode", "Sound Board"))
        self.sampelrate.setText(_translate("voicemode", "hear my self volume"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("voicemode", "Tab 2"))
        self.about.setTitle(_translate("voicemode", "about"))
        self.openaudiopath.setText(_translate("voicemode", u"open audio files dir", None))
        self.refreshlist.setText(_translate("voicemode", u"Refresh List", None))
        self.play.setText(_translate("voicemode", u"play", None))
        self.stop.setText(_translate("voicemode", u"stop", None))
        self.label_3.setText(_translate("voicemode", u"input", None))
        self.label_4.setText(_translate("voicemode", u"output", None))
        self.label_5.setText(_translate("voicemode", u"select device to hear your self", None))
        self.overridehearuselfdevice.setText(_translate("voicemode", u"override hear your self device", None))
        #self.label_2.setText(_translate("voicemode", u"TextLabel", None))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    voicemode = QtWidgets.QMainWindow()
    ui = Ui_voicemode()
    ui.setupUi(voicemode)
    voicemode.show()
    sys.exit(app.exec_())
