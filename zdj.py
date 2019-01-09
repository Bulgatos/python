import sys
import  cv2
from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QLabel, QDesktopWidget, QPushButton, QAction, QTextEdit, QMessageBox, QFileDialog,QFrame
from PyQt5.QtGui import QIcon, QFont, QPixmap
 
class coding(QDialog):
    def __init__(self):
        super().__init__()
        self.title = 'Projekt'
        self.left = 500
        self.top = 500
        self.width = 650
        self.height = 650
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 1000, 600)
        self.setWindowTitle('Single Browse')

        self.label1 = QLabel(self)
        self.label1.setFrameShape(QFrame.Box)
        self.label1.setGeometry(20, 10, 451, 451)
        pixmap = QPixmap('jpg.jpg')
        self.label1.setPixmap(pixmap)
        self.label2 =QLabel(self)
        self.label2.setFrameShape(QFrame.Box)
        self.label2.setGeometry(481, 10, 451, 451)
        btn = QPushButton('Browse', self)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(self.browse)
        btn.move(775, 500)       
        self.show()

    def browse(self):
        filePath = QFileDialog.getOpenFileName(self, 'a file','*.jpg')
        fileHandle = open(filePath[0], 'rb')
        pixmap = QPixmap(filePath[0])
        self.label1.setPixmap(pixmap)
        print("Work!")



def main():
    app = QApplication(sys.argv)
    w = coding()
    app.exec_()


if __name__ == '__main__':
    main()
