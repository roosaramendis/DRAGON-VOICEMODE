from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QFile, QTextStream
from PyQt5 import QtCore
from PyQt5.QtCore import QSettings,Qt
import threading
from PyQt5.QtCore import QProcess
import time
import sys
import detect_running_apps
#from charset_normalizer import detect
import voice_mode_ui, voice_mode_settings_ui,info,addprogramsforoverlay_py,overlay_dialog_py,overlay_py
import subprocess
import os
import pickle

class openoverlaydialog_thread(QtCore.QThread):
    def __init__(self, parent=None):
        super(openoverlaydialog_thread,self).__init__(parent)
    def run(self):
        print("treah called in main")
        overlay_dialog = QtWidgets.QDialog()
        overlay_dialog.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint )#| Qt.X11BypassWindowManagerHint)
        overlay_dialog.setAttribute(Qt.WA_X11DoNotAcceptFocus,True)
        ui = overlay_dialog_py.Ui_Dialog()
        ui.setupUi(overlay_dialog)
        overlay_dialog.exec_()



class overlaydialog(QtWidgets.QMainWindow, overlay_dialog_py.Ui_Dialog):
    def __init__(self, parent=None):
        super (overlaydialog, self).__init__(parent)
        self.setupUi(self)



class overlay_window(QtWidgets.QMainWindow, overlay_py.Ui_overlay):
    def __init__(self, parent=None):
        super(overlay_window, self).__init__(parent)
        self.setupUi(self)
        time.sleep(0.2)
        #self.t1 = openoverlaydialog_thread()
        #self.t1.start()
        #self.actionsettings.triggered.connect(self.on_pushButton_clicked)
        self.dialog = overlaydialog(self)
    def on_pushButton_clicked(self):
        self.dialog.show()    







def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    overlay = QtWidgets.QDialog()
    overlay.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint )#| Qt.X11BypassWindowManagerHint)
    overlay.setAttribute(Qt.WA_TransparentForMouseEvents,True)
    overlay.setAttribute(Qt.WA_TranslucentBackground,True)
    overlay.setAttribute(Qt.WA_X11DoNotAcceptFocus,True) 
    #overlay.setAttribute(Qt.WA_X11TransparentForInput,True)
    ui = overlay_py.Ui_overlay()
    ui.setupUi(overlay)
    overlay.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main() 