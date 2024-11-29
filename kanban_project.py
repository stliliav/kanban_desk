import sys
from pygame import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow
class Application(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = "Kanban board"
        self.left = 300
        self.top = 100
        self.width = 1401
        self.height = 872
        self.main_scr()

    def main_scr(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowIcon(QIcon(r"C:\Users\user\AppData\Local\Programs\Microsoft VS Code\tools\icon.jpg"))
        #main_win.setStyleSheet("background-image: url();")
        self.setStyleSheet("background-image : url(background_kanban.png); ")
   
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Application()
    sys.exit(app.exec_())

    