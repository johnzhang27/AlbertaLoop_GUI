import sys
from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QComboBox, QDialog, QApplication
from PyQt5.QtCore import QSize, QRect
from AlbertaLoop_GUI import Ui_Dialog
class MainWindow(QtWidgets.QWidget, Ui_Dialog):
    def _init_(self):
        super().__init__()
        self.setupUi(self)
#class Camera_ComboBox:
    #selection = ""
    #def _init_(self, selection):
        #self.selection = selection
    #def getSelection(self):
        #return self.selection
#class Display_Camera(QDialog):
    #def _init_(self):
        #super().__init__()
        #self.ui = Ui_Dialog()
        #self.ui.setupUi(self)
        #self.show()
   # def dispcamera(self):
        #resultObj=self.ui.CameraSelection.text()
        #if resultObj == "Front Camera":
           # return 0
        #else:
            #return 1
#combo = CameraSelection()
#combo.addItem(QIcon("path/to/image.png"), "Item 1")
#combo.addItem(QIcon("path/to/image2.png"), "Item 2")

#class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
     #def __init__(self, *args, **kwargs):
        #QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        #self.setupUi(self)

        #self.mediaPlayer = QtMultimedia.QMediaPlayer(self)
        #self.mediaPlayer.setVideoOutput(self.widget)
        #               fileName = "/path/of/your/local_file"
        #               url = QtCore.QUrl.fromLocalFile(fileName)
        #url = QtCore.QUrl("http://clips.vorwaerts-gmbh.de/VfE_html5.mp4")
        #self.mediaPlayer.setMedia(QtMultimedia.QMediaContent(url))
        #self.mediaPlayer.play()
if __name__ == '__main__':
        app = QtWidgets.QApplication(sys.argv)
        Dialog = QtWidgets.QWidget()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        sys.exit(app.exec())
