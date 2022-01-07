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

        # Create textbox
        self.textbox = QLineEdit("bulbasaur", self)
        self.textbox.move(20, 20)
        self.textbox.resize(280, 40)

        # Create a button in the window
        self.button = QPushButton('Search pokemon', self)
        # connect button to function on_click
        self.button.clicked.connect(self.onClick)

        Template = QPixmap("pokeball_template.png")
        self.template = QLabel(self)
        self.template.setPixmap(Template)
        self.template.setStyleSheet('QLabel { background: none ; margin-top: 30px;}')
        self.template.setAlignment(Qt.AlignCenter)
        
        self.btnAdd = 0
        # Create a button in the window
        self.buttonTeam = QPushButton('Add team', self)
        # connect button to function on_click
        self.buttonTeam.clicked.connect(self.addTeam)
        # Create a button in the window
        self.buttonResetTeam = QPushButton('Reset Team', self)
        # connect button to function on_click
        self.buttonResetTeam.clicked.connect(self.resetTeam)


        lienImg = "sprites/sprites/pokemon/"
        r_image = lienImg  + str("1.png")
        image = QPixmap(r_image)
        image_resized = image.scaled(500, 500)
        self.logo = QLabel(self)
        self.logo.setPixmap(image_resized)
        self.logo.setStyleSheet('QLabel { background: none; border-radius: 3px;}')
        self.logo.setGeometry(290, 110, 500, 500)        

        teamTemp = QPixmap("pokeball_ouverte.png")
        teamTempResized = teamTemp.scaled(150,150)
        self.team = QLabel(self)
        self.team.setPixmap(teamTempResized)
        self.team.setStyleSheet('QLabel { background: none}')
        
        teamTemp1 = QPixmap("pokeball_ouverte.png")
        teamTempResized1 = teamTemp1.scaled(150,150)
        self.team1 = QLabel(self)
        self.team1.setPixmap(teamTempResized1)
        self.team1.setStyleSheet('QLabel { background: none}')

        teamTemp2 = QPixmap("pokeball_ouverte.png")
        teamTempResized2 = teamTemp2.scaled(150,150)
        self.team2 = QLabel(self)
        self.team2.setPixmap(teamTempResized2)
        self.team2.setStyleSheet('QLabel { background: none}')

        teamTemp3 = QPixmap("pokeball_ouverte.png")
        teamTempResized3 = teamTemp3.scaled(150,150)
        self.team3 = QLabel(self)
        self.team3.setPixmap(teamTempResized3)
        self.team3.setStyleSheet('QLabel { background: none}')

        teamTemp4 = QPixmap("pokeball_ouverte.png")
        teamTempResized4 = teamTemp4.scaled(150,150)
        self.team4 = QLabel(self)
        self.team4.setPixmap(teamTempResized4)
        self.team4.setStyleSheet('QLabel { background: none}')

        self.team.setGeometry(0,800,150,150)
        self.team1.setGeometry(200,800,150,150)
        self.team2.setGeometry(400,800,150,150)
        self.team3.setGeometry(600,800,150,150)
        self.team4.setGeometry(800,800,150,150)

        lienImgTeam1 = "sprites/sprites/pokemon/"
        r_imageTeam1 = lienImgTeam1  + str("0.png")
        imageTeam1 = QPixmap(r_imageTeam1)
        image_resizedTeam1 = imageTeam1.scaled(150, 150)
        self.logoTeam1 = QLabel(self)
        self.logoTeam1.setPixmap(image_resizedTeam1)
        self.logoTeam1.setStyleSheet('QLabel { background: none; border-radius: 3px;}')
        self.logoTeam1.setGeometry(60, 800, 150, 150)

        lienImgTeam2 = "sprites/sprites/pokemon/"
        r_imageTeam2 = lienImgTeam2  + str("0.png")
        imageTeam2 = QPixmap(r_imageTeam2)
        image_resizedTeam2 = imageTeam2.scaled(150, 150)
        self.logoTeam2 = QLabel(self)
        self.logoTeam2.setPixmap(image_resizedTeam2)
        self.logoTeam2.setStyleSheet('QLabel { background: none; border-radius: 3px;}')
        self.logoTeam2.setGeometry(260, 800, 150, 150)

        lienImgTeam3 = "sprites/sprites/pokemon/"
        r_imageTeam3 = lienImgTeam3  + str("0.png")
        imageTeam3 = QPixmap(r_imageTeam3)
        image_resizedTeam3 = imageTeam3.scaled(150, 150)
        self.logoTeam3 = QLabel(self)
        self.logoTeam3.setPixmap(image_resizedTeam3)
        self.logoTeam3.setStyleSheet('QLabel { background: none; border-radius: 3px;}')
        self.logoTeam3.setGeometry(460, 800, 150, 150)

        lienImgTeam4 = "sprites/sprites/pokemon/"
        r_imageTeam4 = lienImgTeam4  + str("0.png")
        imageTeam4 = QPixmap(r_imageTeam4)
        image_resizedTeam4 = imageTeam4.scaled(150, 150)
        self.logoTeam4 = QLabel(self)
        self.logoTeam4.setPixmap(image_resizedTeam4)
        self.logoTeam4.setStyleSheet('QLabel { background: none; border-radius: 3px;}')
        self.logoTeam4.setGeometry(660, 800, 150, 150)

        lienImgTeam5 = "sprites/sprites/pokemon/"
        r_imageTeam5 = lienImgTeam5  + str("0.png")
        imageTeam5 = QPixmap(r_imageTeam5)
        image_resizedTeam5 = imageTeam5.scaled(150, 150)
        self.logoTeam5 = QLabel(self)
        self.logoTeam5.setPixmap(image_resizedTeam5)
        self.logoTeam5.setStyleSheet('QLabel { background: none; border-radius: 3px;}')
        self.logoTeam5.setGeometry(860, 800, 150, 150)

        
        grid.addWidget(self.textbox,0,0)
        grid.addWidget(self.button, 1, 0)
        grid.addWidget(self.template, 2,0)
        grid.addWidget(self.buttonTeam, 3, 0)
        grid.addWidget(self.buttonResetTeam, 4, 0)
        space = QLabel("",self)
        space.setStyleSheet('QLabel {background:none}')
        grid.addWidget(space, 5, 0)

        #Windows
        self.setLayout(grid)
        

    def onClick(self):
        textboxValue = self.textbox.text()
        
        
        url = "https://pokeapi.co/api/v2/pokemon/"
                    
        r_pokemon = requests.get(url+ str(textboxValue))
        pokemons = r_pokemon.json()
        namePoke = str(pokemons["id"])
        if namePoke != None:
            lienImg = "sprites/sprites/pokemon/"
            r_image = lienImg + str(namePoke) + str(".png")
            image = QPixmap(r_image)
            image_resized = image.scaled(500, 500)
            self.logo.setPixmap(image_resized)
        else:
            box = QMessageBox()
            box.setText("This pokemon doesn't exist")
            box.setWindowTitle("Error: Name")
            box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        
    def addTeam(self):
        textboxValue = self.textbox.text()
        url = "https://pokeapi.co/api/v2/pokemon/"
        r_pokemon = requests.get(url+ str(textboxValue))
        pokemons = r_pokemon.json()
        namePoke = str(pokemons["id"])

        if self.buttonTeam.clicked:
            self.btnAdd += 1
            print(self.btnAdd)
        
        match self.btnAdd:
            case 1:  
                lienImgTeam1 = "sprites/sprites/pokemon/"
                r_imageTeam1 = lienImgTeam1  + str(namePoke)  + str(".png")
                imageTeam1 = QPixmap(r_imageTeam1)
                image_resizedTeam1 = imageTeam1.scaled(150, 150)
                self.logoTeam1.setPixmap(image_resizedTeam1)
            case 2:
                lienImgTeam2 = "sprites/sprites/pokemon/"
                r_imageTeam2 = lienImgTeam2  + str(namePoke)  + str(".png")
                imageTeam2 = QPixmap(r_imageTeam2)
                image_resizedTeam2 = imageTeam2.scaled(150, 150)
                self.logoTeam2.setPixmap(image_resizedTeam2)
            case 3:
                lienImgTeam3 = "sprites/sprites/pokemon/"
                r_imageTeam3 = lienImgTeam3  + str(namePoke)  + str(".png")
                imageTeam3 = QPixmap(r_imageTeam3)
                image_resizedTeam3 = imageTeam3.scaled(150, 150)
                self.logoTeam3.setPixmap(image_resizedTeam3)
            case 4:
                lienImgTeam4 = "sprites/sprites/pokemon/"
                r_imageTeam4 = lienImgTeam4  + str(namePoke)  + str(".png")
                imageTeam4 = QPixmap(r_imageTeam4)
                image_resizedTeam4 = imageTeam4.scaled(150, 150)
                self.logoTeam4.setPixmap(image_resizedTeam4)
            case 5:
                lienImgTeam5 = "sprites/sprites/pokemon/"
                r_imageTeam5 = lienImgTeam5  + str(namePoke)  + str(".png")
                imageTeam5 = QPixmap(r_imageTeam5)
                image_resizedTeam5 = imageTeam5.scaled(150, 150)
                self.logoTeam5.setPixmap(image_resizedTeam5)


    def resetTeam(self):
        if self.buttonResetTeam.clicked:
            self.btnAdd = 0
            print(self.btnAdd)
            lienImgTeam1 = "sprites/sprites/pokemon/"
            r_imageTeam1 = lienImgTeam1  + str("0.png")
            imageTeam1 = QPixmap(r_imageTeam1)
            image_resizedTeam1 = imageTeam1.scaled(150, 150)
            self.logoTeam1.setPixmap(image_resizedTeam1)
            self.logoTeam2.setPixmap(image_resizedTeam1)
            self.logoTeam3.setPixmap(image_resizedTeam1)
            self.logoTeam4.setPixmap(image_resizedTeam1)
            self.logoTeam5.setPixmap(image_resizedTeam1)

def main():
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()