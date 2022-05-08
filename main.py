#created by: sidhas roosara mendis (DRAGON) 
#github link:

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QFile, QTextStream
import sys
import voice_mode_ui, voice_mode_settings_ui,info

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
    def credits_clk1(self):
        self.dialog1.show()    
class voice_mode_window(QtWidgets.QMainWindow, voice_mode_ui.Ui_voicemode):
    def __init__(self, parent=None):
        super(voice_mode_window, self).__init__(parent)
        self.setupUi(self)
        
        self.actionsettings.triggered.connect(self.on_pushButton_clicked)
        self.dialog = settings_window(self)

    def on_pushButton_clicked(self):
        self.dialog.show()

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