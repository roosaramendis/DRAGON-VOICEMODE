# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\mendis\Documents\GitHub\DRAGON-VOICEMODE\voice mode settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSettings


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 480)
        self.settingval = QSettings("Dragon Voide Mode","settings vals")
        self.enablenitify = QtWidgets.QCheckBox(Dialog)
        self.enablenitify.setGeometry(QtCore.QRect(40, 40, 341, 17))
        self.enablenitify.setObjectName("enablenitify")
        self.enablenitify.setChecked(self.settingval.value("enable notify") == 2)
        self.enablenitify.stateChanged.connect(self.setenablenotify)
        self.enableoverlay = QtWidgets.QCheckBox(Dialog)
        self.enableoverlay.setGeometry(QtCore.QRect(40, 90, 421, 20))
        self.enableoverlay.setObjectName("enableoverlay")
        self.enableoverlay.setChecked(self.settingval.value("overlay enable") == 2)
        self.enableoverlay.stateChanged.connect(self.setenabloverlay)
        self.info = QtWidgets.QPushButton(Dialog)
        self.info.setObjectName(u"info")
        self.info.setGeometry(QtCore.QRect(30, 450, 75, 23))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def setenablenotify(self,stateindex):
        print("notify"+str(stateindex))
        self.settingval.setValue("enable notify",stateindex)

    def setenabloverlay(self,stateindex):
        print("overlay"+str(stateindex))
        self.settingval.setValue("overlay enable",stateindex)    

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Settings"))
        self.enablenitify.setText(_translate("Dialog", "enable notifications"))
        self.enableoverlay.setText(_translate("Dialog", "enable game overlay"))
        self.info.setText(_translate("Dialog", u"Info", None))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
