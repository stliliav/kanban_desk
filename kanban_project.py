import sys
from pygame import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
class Application(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = "KANBAN BOARD"
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

        self.firstdo = QLineEdit(self)
        self.firstdo.setGeometry(80, 80, 249, 30)
        self.firstdo.setStyleSheet("background-image: url(white.jpg); font-size: 20px; ")
        self.firstdo.show()

        self.seconddo = QLineEdit(self)
        self.seconddo.setGeometry(80, 145, 249, 30)
        self.seconddo.setStyleSheet("background-image: url(white.jpg); font-size: 20px; ")
        self.seconddo.show()

        self.thirddo = QLineEdit(self)
        self.thirddo.setGeometry(80, 210, 249, 30)
        self.thirddo.setStyleSheet("background-image: url(white.jpg); font-size: 20px; ")
        self.thirddo.show()

        self.fourthdo = QLineEdit(self)
        self.fourthdo.setGeometry(80, 260, 249, 30)
        self.fourthdo.setStyleSheet("background-image: url(white.jpg); font-size: 20px; ")
        self.fourthdo.show()

        self.fifthdo = QLineEdit(self)
        self.fifthdo.setGeometry(80, 325, 249, 30)
        self.fifthdo.setStyleSheet("background-image: url(white.jpg); font-size: 20px; ")
        self.fifthdo.show()

        self.sixthdo = QLineEdit(self)
        self.sixthdo.setGeometry(80, 390, 249, 30)
        self.sixthdo.setStyleSheet("background-image: url(white.jpg); font-size: 20px; ")
        self.sixthdo.show()

        self.seventhdo = QLineEdit(self)
        self.seventhdo.setGeometry(83, 465, 245, 30)
        self.seventhdo.setStyleSheet("background-image: url(white.jpg); font-size: 20px; ")
        self.fourthdo.show()

        self.eightdo = QLineEdit(self)
        self.eightdo.setGeometry(83, 525, 245, 30)
        self.eightdo.setStyleSheet("background-image: url(white.jpg); font-size: 20px; ")
        self.eightdo.show()

        self.ninedo = QLineEdit(self)
        self.ninedo.setGeometry(83, 590, 245, 30)
        self.ninedo.setStyleSheet("background-image: url(white.jpg); font-size: 20px; ")
        self.ninedo.show()
        
        self.tendo = QLineEdit(self)
        self.tendo.setGeometry(83, 670, 245, 30)
        self.tendo.setStyleSheet("background-image: url(white.jpg); font-size: 20px; ")
        self.tendo.show()

        self.elevendo = QLineEdit(self)
        self.elevendo.setGeometry(83, 735, 245, 30)
        self.elevendo.setStyleSheet("background-image: url(white.jpg); font-size: 20px; ")
        self.elevendo.show()

        self.twelvedo = QLineEdit(self)
        self.twelvedo.setGeometry(83, 800, 245, 30)
        self.twelvedo.setStyleSheet("background-image: url(white.jpg); font-size: 20px; ")
        self.twelvedo.show()
        
        self.firstprog = QLineEdit(self)
        self.firstprog.setGeometry(420, 80, 275, 30)
        self.firstprog.setStyleSheet("background-image: url(white.jpg); font-size: 20px; ")
        self.firstprog.show()

        self.secondprog = QLineEdit(self)
        self.secondprog.setGeometry(420, 145, 275, 30)
        self.secondprog.setStyleSheet("background-image: url(white.jpg); font-size: 20px; ")
        self.secondprog.show()

        self.thirdprog = QLineEdit(self)
        self.thirdprog.setGeometry(420, 210, 275, 30)
        self.thirdprog.setStyleSheet("background-image: url(white.jpg); font-size: 20px; ")
        self.thirdprog.show()

        self.fourthprog = QLineEdit(self)
        self.fourthprog.setGeometry(420, 260, 275, 30)
        self.fourthprog.setStyleSheet("background-image: url(white.jpg); font-size: 20px; ")
        self.fourthprog.show()

        self.fifthprog = QLineEdit(self)
        self.fifthprog.setGeometry(420, 325, 275, 30)
        self.fifthprog.setStyleSheet("background-image: url(white.jpg); font-size: 20px; ")
        self.fifthprog.show()

        self.sixthprog = QLineEdit(self)
        self.sixthprog.setGeometry(420, 390, 275, 30)
        self.sixthprog.setStyleSheet("background-image: url(white.jpg); font-size: 20px; ")
        self.sixthprog.show()

        self.seventhprog = QLineEdit(self)
        self.seventhprog.setGeometry(420, 465, 275, 30)
        self.seventhprog.setStyleSheet("background-image: url(white.jpg); font-size: 20px; ")
        self.seventhprog.show()

        self.eightprog = QLineEdit(self)
        self.eightprog.setGeometry(420, 525, 275, 30)
        self.eightprog.setStyleSheet("background-image: url(white.jpg); font-size: 20px; ")
        self.eightprog.show()

        self.nineprog = QLineEdit(self)
        self.nineprog.setGeometry(420, 590, 275, 30)
        self.nineprog.setStyleSheet("background-image: url(white.jpg); font-size: 20px; ")
        self.nineprog.show()

        self.tenprog = QLineEdit(self)
        self.tenprog.setGeometry(420, 670, 275, 30)
        self.tenprog.setStyleSheet("background-image: url(white.jpg); font-size: 20px; ")
        self.tenprog.show()

        self.elevenprog = QLineEdit(self)
        self.elevenprog.setGeometry(420, 735, 275, 30)
        self.elevenprog.setStyleSheet("background-image: url(white.jpg); font-size: 20px; ")
        self.elevenprog.show()

        self.twelveprog = QLineEdit(self)
        self.twelveprog.setGeometry(420, 800, 275, 30)
        self.twelveprog.setStyleSheet("background-image: url(white.jpg); font-size: 20px; ")
        self.twelveprog.show()

        self.firsttest = QLineEdit(self)
        self.firsttest.setGeometry(795, 83, 250, 30)
        self.firsttest.setStyleSheet("background-image: url(white.jpg); font-size: 20px; ")
        self.firsttest.show()

        self.secondtest = QLineEdit(self)
        self.secondtest.setGeometry(795, 145, 250, 30)
        self.secondtest.setStyleSheet("background-image: url(white.jpg); font-size: 20px; ")
        self.secondtest.show()

        self.thirdtest = QLineEdit(self)
        self.thirdtest.setGeometry(795, 210, 250, 30)
        self.thirdtest.setStyleSheet("background-image: url(white.jpg); font-size: 20px; ")
        self.thirdtest.show()

        self.fourthtest = QLineEdit(self)
        self.fourthtest.setGeometry(795, 258, 250, 30)
        self.fourthtest.setStyleSheet("background-image: url(white.jpg); font-size: 20px; ")
        self.fourthtest.show()

        self.fifthtest = QLineEdit(self)
        self.fifthtest.setGeometry(795, 320, 250, 30)
        self.fifthtest.setStyleSheet("background-image: url(white.jpg); font-size: 20px; ")
        self.fifthtest.show()

        self.sixthtest = QLineEdit(self)
        self.sixthtest.setGeometry(795, 385, 250, 30)
        self.sixthtest.setStyleSheet("background-image: url(white.jpg); font-size: 20px; ")
        self.sixthtest.show()

        self.seventhtest = QLineEdit(self)
        self.seventhtest.setGeometry(795, 465, 250, 30)
        self.seventhtest.setStyleSheet("background-image: url(white.jpg); font-size: 20px; ")
        self.seventhtest.show()

        self.eighttest = QLineEdit(self)
        self.eighttest.setGeometry(795, 525, 250, 30)
        self.eighttest.setStyleSheet("background-image: url(white.jpg); font-size: 20px; ")
        self.eighttest.show()

        self.ninetest = QLineEdit(self)
        self.ninetest.setGeometry(795, 590, 250, 30)
        self.ninetest.setStyleSheet("background-image: url(white.jpg); font-size: 20px; ")
        self.ninetest.show()

        self.tentest = QLineEdit(self)
        self.tentest.setGeometry(795, 670, 250, 30)
        self.tentest.setStyleSheet("background-image: url(white.jpg); font-size: 20px; ")
        self.tentest.show()

        self.eleventest = QLineEdit(self)
        self.eleventest.setGeometry(795, 735, 250, 30)
        self.eleventest.setStyleSheet("background-image: url(white.jpg); font-size: 20px; ")
        self.eleventest.show()

        self.twelvetest = QLineEdit(self)
        self.twelvetest.setGeometry(795, 800, 250, 30)
        self.twelvetest.setStyleSheet("background-image: url(white.jpg); font-size: 20px; ")
        self.twelvetest.show()
        
        self.firstdid = QLineEdit(self)
        self.firstdid.setGeometry(1140, 83, 260, 30)
        self.firstdid.setStyleSheet("background-image: url(white.jpg); font-size: 20px; ")
        self.firstdid.show()

        self.seconddid = QLineEdit(self)
        self.seconddid.setGeometry(1140, 145, 260, 30)
        self.seconddid.setStyleSheet("background-image: url(white.jpg); font-size: 20px; ")
        self.seconddid.show()

        self.thirddid = QLineEdit(self)
        self.thirddid.setGeometry(1140, 210, 260, 30)
        self.thirddid.setStyleSheet("background-image: url(white.jpg); font-size: 20px; ")
        self.thirddid.show()

        self.fourthdid = QLineEdit(self)
        self.fourthdid.setGeometry(1140, 255, 260, 30)
        self.fourthdid.setStyleSheet("background-image: url(white.jpg); font-size: 20px; ")
        self.fourthdid.show()

        self.fifthdid = QLineEdit(self)
        self.fifthdid.setGeometry(1140, 320, 260, 30)
        self.fifthdid.setStyleSheet("background-image: url(white.jpg); font-size: 20px; ")
        self.fifthdid.show()

        self.sixthdid = QLineEdit(self)
        self.sixthdid.setGeometry(1140, 385, 260, 30)
        self.sixthdid.setStyleSheet("background-image: url(white.jpg); font-size: 20px; ")
        self.sixthdid.show()

        self.seventhdid = QLineEdit(self)
        self.seventhdid.setGeometry(1140, 465, 260, 30)
        self.seventhdid.setStyleSheet("background-image: url(white.jpg); font-size: 20px; ")
        self.fourthdid.show()

        self.eightdid = QLineEdit(self)
        self.eightdid.setGeometry(1140, 525, 260, 30)
        self.eightdid.setStyleSheet("background-image: url(white.jpg); font-size: 20px; ")
        self.eightdid.show()

        self.ninedid = QLineEdit(self)
        self.ninedid.setGeometry(1140, 590, 260, 30)
        self.ninedid.setStyleSheet("background-image: url(white.jpg); font-size: 20px; ")
        self.ninedid.show()

        self.tendid = QLineEdit(self)
        self.tendid.setGeometry(1140, 668, 260, 30)
        self.tendid.setStyleSheet("background-image: url(white.jpg); font-size: 20px; ")
        self.tendid.show()

        self.elevendid = QLineEdit(self)
        self.elevendid.setGeometry(1140, 730, 260, 30)
        self.elevendid.setStyleSheet("background-image: url(white.jpg); font-size: 20px; ")
        self.elevendid.show()

        self.twelvedid = QLineEdit(self)
        self.twelvedid.setGeometry(1140, 795, 260, 30)
        self.twelvedid.setStyleSheet("background-image: url(white.jpg); font-size: 20px; ")
        self.twelvedid.show()
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Application()
    sys.exit(app.exec_())
