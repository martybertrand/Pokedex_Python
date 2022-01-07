from typing import Text
from PyQt5.QtWidgets import (QGridLayout, QPushButton, QRadioButton, QWidget, QSlider, QHBoxLayout,
                             QLabel, QMessageBox, QLineEdit, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage, QPalette, QBrush, QTextBlock
import sys
import requests


class App(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
        self.setGeometry(20, 40, 1050, 1000)
        self.setWindowTitle('Pokemon')
        self.setStyleSheet("background-color: white")
        self.show()

    def initUI(self):

        grid = QGridLayout()

        self.btnPokedex = QPushButton("Pokedex", self)
        self.btnPokedex.clicked.connect(self.clickPokedex)

        self.btnSearchTeam = QPushButton("My Team", self)
        self.btnSearchTeam.clicked.connect(self.clickSearchTeam)
        
        grid.addWidget(self.btnPokedex,0,0)
        grid.addWidget(self.btnSearchTeam,0,1)

        self.setLayout(grid)


    def clickPokedex(self):
        print("pokedex")
        label = QLabel("uiiii")
        label.setGeometry(500,500,100,1000)


    def clickSearchTeam(self):
        print("Search Team")

def main():
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()