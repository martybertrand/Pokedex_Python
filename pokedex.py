from typing import Text
from PyQt5.QtWidgets import (QGridLayout, QPushButton, QRadioButton, QWidget, QSlider, QHBoxLayout,
                             QLabel, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage, QPalette, QBrush, QTextBlock
import sys
import requests


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
        self.setGeometry(20, 40, 1050, 1000)
        self.setWindowTitle('Pokemon')
        self.setStyleSheet("background-color: white")

    def initUI(self): 
        
        grid = QGridLayout()

        #Slider for switch into Pokdex
        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setRange(1, 151)
        sld.setPageStep(5)
        sld.valueChanged.connect(self.changeValue)

        #Titre Pokemon
        Titre = QPixmap("pokemon.png")
        self.titre = QLabel(self)
        self.titre.setPixmap(Titre)

        #Template Pokedex
        Template = QPixmap("template_pokemon.jpg")
        self.template = QLabel(self)
        self.template.setPixmap(Template)
        #self.template.setGeometry(30, 100, 1200, 1000)

        #Initialisation de mes variables
        pvPoke = "PV : "
        otherformPoke = "Other form"
        shinyPoke = "Shiny"

        url = "https://pokeapi.co/api/v2/pokemon/"
        r_pokemon = requests.get(url+ str("1"))
        pokemons = r_pokemon.json()
        namePoke = pokemons["name"].capitalize()
        typePoke = pokemons["types"][0]["type"]["name"].capitalize()
        heightPoke = str(pokemons["height"])
        weightPoke = str(pokemons["weight"])
        abilityPoke = pokemons["abilities"][0]["ability"]["name"].capitalize()
        baseStatPoke = str(pokemons["stats"][0]["base_stat"])
        idPoke = '1'

        #Image pokemon de base
        lienImg = "sprites/sprites/pokemon/"
        r_image = lienImg + str("1.png")
        image = QPixmap(r_image)
        image_resized = image.scaled(300, 300)

        #Image pokemon si autre forme
        lienImgOther = "sprites/sprites/pokemon/"
        r_imageOther = lienImgOther + str("1-mega.png")
        r_imageOtherX = lienImgOther + str("1-mega-x.png")
        r_imageOtherY = lienImgOther + str("1-mega-y.png")
        
        if r_imageOther:
            imageOther = QPixmap(r_imageOther)
            image_resizedOther = imageOther.scaled(100, 100)
            self.imageOther = QLabel(self)
            self.imageOther.setPixmap(image_resizedOther)
            self.imageOther.setStyleSheet('QLabel { background: none; border-radius: 3px;}')
        if r_imageOtherX:
            imageOtherX = QPixmap(r_imageOtherX)
            image_resizedOtherX = imageOtherX.scaled(100,100)
            self.imageOtherX = QLabel(self)
            self.imageOtherX.setPixmap(image_resizedOtherX)
            self.imageOtherX.setStyleSheet('QLabel { background: none; border-radius: 3px;}')
        if r_imageOtherY:
            imageOtherY = QPixmap(r_imageOtherY)
            image_resizedOtherY = imageOtherY.scaled(100,100)
            self.imageOtherY = QLabel(self)
            self.imageOtherY.setPixmap(image_resizedOtherY)
            self.imageOtherY.setStyleSheet('QLabel { background: none; border-radius: 3px;}')

        #Image pokemon shiny
        lienImgShiny = "sprites/sprites/pokemon/shiny/"
        r_imageShiny = lienImgShiny + str("1.png")
        r_imageShiny = QPixmap(r_imageShiny)
        image_resizedShiny = r_imageShiny.scaled(100, 100)

        #QLabel de mes widget
        self.imgShiny = QLabel(self)
        self.imgShiny.setPixmap(image_resizedShiny)
        self.otherForm = QLabel(otherformPoke, self)
        self.shiny = QLabel(shinyPoke, self)
        self.baseStatPokemon = QLabel(baseStatPoke, self)
        self.pv = QLabel(pvPoke, self)
        self.heightPokemon = QLabel(heightPoke, self)
        self.ability = QLabel(abilityPoke, self)
        self.logo = QLabel(self)
        self.logo.setPixmap(image_resized)
        self.label = QLabel(namePoke, self)
        self.id = QLabel(idPoke, self)
        self.type = QLabel(typePoke, self)
        self.weightPokemon = QLabel(weightPoke, self)

        #Style Widgets
        self.otherForm.setStyleSheet('QLabel { font-size:15px;background: none; border-radius: 3px;}')
        self.shiny.setStyleSheet('QLabel { font-size:15px;background: none; border-radius: 3px;}')
        self.label.setStyleSheet('QLabel { font-size:30px;color: white; background: none; border-radius: 3px;}')
        self.logo.setStyleSheet('QLabel { background: none; border-radius: 3px;}')
        self.imgShiny.setStyleSheet('QLabel { background: none; border-radius: 3px;}')
        self.id.setStyleSheet('QLabel { font-size:20px; color: white; background: none; border-radius: 3px;}')
        self.type.setStyleSheet('QLabel { font-size:20px;background: none; border-radius: 3px;}')
        self.pv.setStyleSheet('QLabel { font-size:20px;background: none; border-radius: 3px;}')
        self.titre.setStyleSheet('QLabel { background: none ; }')
        self.baseStatPokemon.setStyleSheet('QLabel { font-size:20px;background: none; border-radius: 3px;}')
        self.template.setStyleSheet('QLabel { background: none; margin-top: 30px;width: 100%; text-align:center;}')
        self.heightPokemon.setStyleSheet('QLabel { font-size:20px;background: none; border-radius: 3px;}')
        self.weightPokemon.setStyleSheet('QLabel { font-size:20px;background: none; border-radius: 3px;}')
        self.ability.setStyleSheet('QLabel { font-size:20px;background: none; border-radius: 3px;}')
        self.titre.setAlignment(Qt.AlignCenter)
        self.template.setAlignment(Qt.AlignCenter)
        self.label.setMinimumWidth(200)

        #Disposition Widgets
        self.imageOther.setGeometry(450,750,100,100)
        self.imageOtherX.setGeometry(450,750,100,100)
        self.imageOtherY.setGeometry(560,750,100,100)
        self.imgShiny.setGeometry(840,715,150,150)
        self.otherForm.setGeometry(450,690,100,100)
        self.shiny.setGeometry(870,690,100,100)
        self.baseStatPokemon.setGeometry(720,440,100,100)
        self.pv.setGeometry(660,440,100,100)
        self.logo.setGeometry(100, 600, 300, 300)
        self.id.setGeometry(550,340,100,100)
        self.label.setGeometry(690,340,100,100)
        self.type.setGeometry(720,500,100,100)
        self.heightPokemon.setGeometry(720,550,100,100)
        self.weightPokemon.setGeometry(720,600,100,100)
        self.ability.setGeometry(720,650,100,100)
        grid.addWidget(sld, 1, 0)
        #grid.addWidget(self.type, 3, 0)
        #grid.addWidget(self.id, 3, 0)
        #grid.addWidget(self.label, 4, 0)
        #grid.addWidget(self.logo, 5, 2)
        grid.addWidget(self.titre, 0, 0)
        grid.addWidget(self.template, 2,0)
            
        #Windows
        self.setLayout(grid)

        self.show()

        
    def changeValue(self, value):
        url = "https://pokeapi.co/api/v2/pokemon/"
                    
        r_pokemon = requests.get(url+ str(value))
        pokemons = r_pokemon.json()
        namePoke = pokemons["name"].capitalize()           
        typePoke = pokemons["types"][0]["type"]["name"].capitalize()
        heightPoke = str(pokemons['height'])
        weightPoke = str(pokemons['weight'])
        abilityPoke = pokemons["abilities"][0]["ability"]["name"].capitalize()
        idPoke = str(value)
        baseStatPoke = str(pokemons["stats"][0]["base_stat"])
        
        #Pokemon base
        lienImg = "sprites/sprites/pokemon/"
        r_image = lienImg + str(value) + str(".png")
        image = QPixmap(r_image)
        image_resized = image.scaled(300, 300)

        #Pokemon Shiny
        lienImgShiny = "sprites/sprites/pokemon/shiny/"
        r_imageShiny = lienImgShiny + str(value) + str(".png")
        r_imageShiny = QPixmap(r_imageShiny)
        image_resizedShiny = r_imageShiny.scaled(100, 100)
        
        #Pokemon other form
        lienImgOther = "sprites/sprites/pokemon/"
        r_imageOther = lienImgOther + str(value) + str("-mega.png")
        r_imageOtherX = lienImgOther + str(value) + str("-mega-x.png")
        r_imageOtherY = lienImgOther + str(value) + str("-mega-y.png")
        if r_imageOther:
            imageOther = QPixmap(r_imageOther)
            image_resizedOther = imageOther.scaled(100, 100)
        if r_imageOtherX:
            imageOtherX = QPixmap(r_imageOtherX)
            image_resizedOtherX = imageOtherX.scaled(100, 100)
        if r_imageOtherY:
            imageOtherY = QPixmap(r_imageOtherY)
            image_resizedOtherY = imageOtherY.scaled(100, 100)


        self.imageOtherX.setPixmap(image_resizedOtherX)
        self.imageOtherY.setPixmap(image_resizedOtherY)  
        self.imageOther.setPixmap(image_resizedOther)
        self.imgShiny.setPixmap(image_resizedShiny)
        self.baseStatPokemon.setText(baseStatPoke)
        self.heightPokemon.setText(heightPoke)
        self.weightPokemon.setText(weightPoke)
        self.ability.setText(abilityPoke)
        self.logo.setPixmap(image_resized)
        self.label.setText(namePoke)
        self.id.setText(idPoke)
        self.type.setText(typePoke)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()