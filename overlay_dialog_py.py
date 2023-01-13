# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\mendis\Documents\GitHub\DRAGON-VOICEMODE\overlay_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSettings,Qt,QFile,QTextStream,QSettings
import pickle
import os

global mydir
mydir = os.path.dirname(os.path.realpath(__file__))
global hotkeydict
hotkeydict ={}

class TableModel(QtCore.QAbstractTableModel):
    
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            
            return self.datalist[index.row()][index.column()]

    def rowCount(self, index):
        try:
            self.keylist =[]
            self.vallist = []
            self.datalist = []
            for i in self._data.keys():
                self.keylist.append(i)
                self.vallist.append(self._data.get(i))
                dl = (str(self._data.get(i)),str(i))
                self.datalist.append(dl)
            return len(self.datalist)
        except:
            pass
    def columnCount(self, index):
        try:
            return len(self.datalist[0])
        except:
            pass 

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(845, 679)
        Dialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        Dialog.setAttribute(Qt.WA_X11DoNotAcceptFocus,True)
        Dialog.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint )
        
        stylef = QFile("style1.css") 
        stylef.open(QFile.ReadOnly | QFile.Text)
        stylesheet = QTextStream(stylef)
        stylesheetstr =stylesheet.readAll()
        Dialog.setStyleSheet(stylesheetstr)
        try:
            self.settingval = QSettings("DragonVoiceMode","settings vals")
        except:
            pass
        self.mydir = self.settingval.value("mydir")
        try:
            datainfile = pickle.load(open(self.mydir+"/"+"saves/hotkeys.dvm","rb")) #read data in file
            print(datainfile)
            hotkeydictinfile = datainfile
            hotkeydict.update(hotkeydictinfile)
            print(hotkeydict)
        except:
            pass
        
        try:

            Dialog.setWindowOpacity(float(self.settingval.value("opacity"))/100)    
        except:
            Dialog.setWindowOpacity(0.8)

        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 100, 821, 561))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        '''self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(0, 20, 821, 471))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)'''
        self.tableView = QtWidgets.QTableView(self.tab)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QtCore.QRect(0, 20, 821, 471))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.hearmyselfvolume_sb = QtWidgets.QSpinBox(Dialog)
        self.hearmyselfvolume_sb.setGeometry(QtCore.QRect(20, 50, 81, 31))
        self.hearmyselfvolume_sb.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.hearmyselfvolume_sb.setMaximum(200)
        self.hearmyselfvolume_sb.setStepType(QtWidgets.QAbstractSpinBox.AdaptiveDecimalStepType)
        self.hearmyselfvolume_sb.setObjectName("hearmyselfvolume_sb")
        self.hearmyselfvolume_sb.setValue(int(self.settingval.value("hearmyselfvolume")))
        self.hearmyselfvolume_sb.valueChanged.connect(self.sethearmyselfvolume)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(130, 50, 191, 31))
        self.label.setObjectName("label")
        self.soundboardvolume_sb = QtWidgets.QSpinBox(Dialog)
        self.soundboardvolume_sb.setGeometry(QtCore.QRect(260, 50, 81, 31))
        self.soundboardvolume_sb.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.soundboardvolume_sb.setMaximum(200)
        self.soundboardvolume_sb.setStepType(QtWidgets.QAbstractSpinBox.AdaptiveDecimalStepType)
        self.soundboardvolume_sb.setObjectName("soundboardvolume_sb")
        self.soundboardvolume_sb.setValue(int(self.settingval.value("soundboardvolume")))
        self.soundboardvolume_sb.valueChanged.connect(self.setsoundboardvolume)
        
        self.exit = QtWidgets.QPushButton(Dialog)
        self.exit.setObjectName(u"exit")
        self.exit.setGeometry(QtCore.QRect(740, 10, 91, 91))
        self.exit.clicked.connect(self.exit_button_clicked)

        self.opacity_sb = QtWidgets.QSpinBox(Dialog)
        self.opacity_sb.setGeometry(QtCore.QRect(540, 50, 81, 31))
        self.opacity_sb.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.opacity_sb.setMaximum(200)
        self.opacity_sb.setStepType(QtWidgets.QAbstractSpinBox.AdaptiveDecimalStepType)
        self.opacity_sb.setObjectName("opacity_sb")
        try:
            self.opacity_sb.setValue(int(self.settingval.value("opacity")))
        except:
            pass    
        self.opacity_sb.valueChanged.connect(self.set_opacity)

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(380, 50, 150, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(630, 50, 100, 31))
        self.label_3.setObjectName("label_3")
        if len(hotkeydict.keys()) != 0:
            self.settableview(hotkeydict)
        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
    def settableview(self,dic):
        global tablemodel
        try:
            tablemodel = QtGui.QStandardItemModel()
        
            dic = dic
            print(str(enumerate(dic)))
            tablemodel = TableModel(dic)
            self.tableView.setModel(tablemodel)
            self.tableView.resizeColumnsToContents()
        except:
            pass  
    
    def sethearmyselfvolume(self,value):
        self.settingval.setValue("hearmyselfvolume",value)

    def setsoundboardvolume(self,value):
        self.settingval.setValue("soundboardvolume",value)

    def set_opacity(self,value):
        self.settingval.setValue("opacity",value)
        
        #Dialog.setWindowOpacity(float(self.settingval.value("opacity"))/100)

    def exit_button_clicked(self):
        self.close()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Tab 2"))
        self.label.setText(_translate("Dialog", "hear my self volume"))
        self.label_2.setText(_translate("Dialog", "sound board volume"))
        self.label_3.setText(_translate("Dialog", "opatcity"))
        self.exit.setText(_translate("Dialog", u"Exit", None))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
