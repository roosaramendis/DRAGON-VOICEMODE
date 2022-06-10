#created by: sidhas roosara mendis (DRAGON) 
#github link:

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QFile, QTextStream
from PyQt5 import QtCore
from PyQt5.QtCore import QSettings,Qt
import threading
from PyQt5.QtCore import QProcess
import time
import sys
import voice_mode_ui, voice_mode_settings_ui,info,addprogramsforoverlay_py,overlay_py


class openoverlay_thread(QtCore.QThread):
    def __init__(self, parent=None):
        super(openoverlay_thread,self).__init__(parent)
    def run(self):
        print("treah called in main")
        overlay = QtWidgets.QDialog()
        overlay.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint )#| Qt.X11BypassWindowManagerHint)
        overlay.setAttribute(Qt.WA_TransparentForMouseEvents,True)
        overlay.setAttribute(Qt.WA_TranslucentBackground,True)
        overlay.setAttribute(Qt.WA_X11DoNotAcceptFocus,True)
        ui = overlay_py.Ui_overlay()
        ui.setupUi(overlay)
        overlay.exec_()
        

class ovelay(QtWidgets.QMainWindow, overlay_py.Ui_overlay):
    def __init__(self, parent=None):
        super(ovelay, self).__init__(parent)
        self.setupUi(self)
        self

class addappsforovelay(QtWidgets.QMainWindow, addprogramsforoverlay_py.Ui_addprogramsforoverlay):
    def __init__(self, parent=None):
        super(addappsforovelay, self).__init__(parent)
        self.setupUi(self)

class info(QtWidgets.QMainWindow, info.Ui_Frame):
    def __init__(self, parent=None):
        super(info, self).__init__(parent)
        self.setupUi(self)

class settings_window(QtWidgets.QMainWindow, voice_mode_settings_ui.Ui_Dialog):
    def __init__(self, parent=None):
        super (settings_window, self).__init__(parent)
        self.setupUi(self)
        self.info.clicked.connect(self.credits_clk1)
        self.dialog1 = info(self)
        self.add_overlay_programs.clicked.connect(self.aop_clk)
        self.dialog2 = addappsforovelay(self)
    def credits_clk1(self):
        self.dialog1.show()    

    def aop_clk(self):
        self.dialog2.show()

class voice_mode_window(QtWidgets.QMainWindow, voice_mode_ui.Ui_voicemode):
    def __init__(self, parent=None):
        super(voice_mode_window, self).__init__(parent)
        self.setupUi(self)
        time.sleep(0.2)
        self.t1 = openoverlay_thread()
        self.t1.start()
        self.actionsettings.triggered.connect(self.on_pushButton_clicked)
        self.dialog = settings_window(self)
        #self.showoverlaycall()
        

        

    def on_pushButton_clicked(self):
        self.dialog.show()
    def showoverlaycall(self):
        t1 = threading.Thread(target=self.showoverlay)
        t1.start()

    def showoverlay(self):
        overlay = QtWidgets.QDialog()
        overlay.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint )#| Qt.X11BypassWindowManagerHint)
        overlay.setAttribute(Qt.WA_TransparentForMouseEvents,True)
        overlay.setAttribute(Qt.WA_TranslucentBackground,True)
        overlay.setAttribute(Qt.WA_X11DoNotAcceptFocus,True)
        ui = overlay_py.Ui_overlay()
        ui.setupUi(overlay)
        overlay.exec_()
        #sys.exit(app2.exec_()) 


def main():
    app = QtWidgets.QApplication(sys.argv)
    stylef = QFile("style1.css") 
    stylef.open(QFile.ReadOnly | QFile.Text)
    stylesheet = QTextStream(stylef)
    stylesheetstr =stylesheet.readAll()
    print(stylesheetstr)
    app.setStyleSheet(stylesheetstr)
    main = voice_mode_window()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main() 