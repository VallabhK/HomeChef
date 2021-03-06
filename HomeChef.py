# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomeChef.ui'
"""
# Data Focused Python B1
# Created by: 
# 1. Vallabh Karanjkar-vkaranjk
# 2. Mohini Jain- mohinij
# 3. Rohit Jain- rohitj
# Group 24
"""


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTextBrowser
from PyQt5.QtWidgets import QSizePolicy

from youtubeScraper import youtubeScraper
from dataProcessing import getCalorieData
import Background_rc

import matplotlib.pyplot as plt
import numpy as np
import v5_pdf_scraping as pdfs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time


class Ui_Form(object):
    #define reset button functionality
    def resetButtonClicked(self):
        self.RecipeInformation.setText("")
        self.textEdit.setText("")
        self.RecipeInformation_2.setText("")
        self.RecipeSearchString.setText("")
        self.Recipe1Label.setText("")
        self.Recipe1Label_2.setText("")
        self.Recipe1Label_3.setText("")
        self.Recipe1Label.setText("")
        self.Recipe1Label_2.setText("")
        self.Recipe1Label_3.setText("")
        self.CalorieValueLabel.setText("")
        self.FatLabel.setText("")
        self.CarbLabel.setText("")
        self.ProteinLabel.setText("")
    #define SearchButton Functionality
    def searchButtonClicked(self):

        searchString = self.RecipeSearchString.toPlainText()

        if (len(searchString) > 0):

            # Scrape PDF data to get recipe based on user input
            recipeData = pdfs.get_recipe(searchString)
            self.RecipeInformation.setText(recipeData[0])
            
            if(len(recipeData[1]) == 0):
                return
            # Youtube Data Processing
            recipeLinks = []
            recipeLinks = youtubeScraper(recipeData)

            recipesMainLinks = recipeLinks.split(",")

            self.Recipe1Label.setOpenExternalLinks(True)
            self.Recipe1Label_2.setOpenExternalLinks(True)
            self.Recipe1Label_3.setOpenExternalLinks(True)

            recipeNames = []
            linkTemplate = r'<a href={0}>{1}</a>'

            for recipes in recipeData[1]:
                recipeNames.append(recipes)

                           
            self.Recipe1Label.setTextFormat(QtCore.Qt.RichText)
            self.Recipe1Label_2.setTextFormat(QtCore.Qt.RichText)
            self.Recipe1Label_3.setTextFormat(QtCore.Qt.RichText)
            
            self.Recipe1Label.setText(" ")
            self.Recipe1Label_2.setText(" ")
            self.Recipe1Label_3.setText(" ")
            
            print(recipeLinks)
            
            self.Recipe1Label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            if(len(recipeNames)>0):
                self.Recipe1Label.setText(linkTemplate.format(recipesMainLinks[0], recipeNames[0]))
                if(len(recipeNames)>1):
                    self.Recipe1Label_2.setText(linkTemplate.format(recipesMainLinks[1], recipeNames[1]))
                    if(len(recipeNames)>2):
                        self.Recipe1Label_3.setText(linkTemplate.format(recipesMainLinks[2], recipeNames[2]))

            # Calorie Data Processing
            NutritionList = []
            NutritionList = getCalorieData(searchString)
            #Access the links 
            self.CalorieValueLabel.setText(NutritionList[0])
            self.FatLabel.setText(NutritionList[1])
            self.CarbLabel.setText(NutritionList[2])
            self.ProteinLabel.setText(NutritionList[3])

        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Error")
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Please enter a valid food item")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(580, 599)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(580, 599))
        Form.setMaximumSize(QtCore.QSize(580, 599))
        self.RecipeSearchString = QtWidgets.QTextEdit(Form)
        self.RecipeSearchString.setEnabled(True)
        self.RecipeSearchString.setGeometry(QtCore.QRect(250, 190, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        self.RecipeSearchString.setFont(font)
        self.RecipeSearchString.setStyleSheet("border-radius:50;")
        self.RecipeSearchString.setObjectName("RecipeSearchString")
        self.RecipeSearchString.setPlaceholderText("Please enter 1 main food ingredient")
        self.RecipeInformation = QtWidgets.QTextEdit(Form)
        self.RecipeInformation.setGeometry(QtCore.QRect(220, 310, 341, 141))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        self.RecipeInformation.setFont(font)
        self.RecipeInformation.setStyleSheet("border: 0")
        self.RecipeInformation.setObjectName("RecipeInformation")
        self.CalorieInfo = QtWidgets.QGraphicsView(Form)
        self.CalorieInfo.setGeometry(QtCore.QRect(10, 470, 561, 121))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        self.CalorieInfo.setFont(font)
        self.CalorieInfo.setObjectName("CalorieInfo")
        self.ChefLogo = QtWidgets.QLabel(Form)
        self.ChefLogo.setGeometry(QtCore.QRect(-10, 30, 291, 271))
        self.ChefLogo.setStyleSheet("")
        self.ChefLogo.setText("")
        self.ChefLogo.setPixmap(QtGui.QPixmap(":/newPrefix/ChefLogo_NoBackground.png"))
        self.ChefLogo.setScaledContents(True)
        self.ChefLogo.setObjectName("ChefLogo")
        self.ChefLogo_2 = QtWidgets.QLabel(Form)
        self.ChefLogo_2.setGeometry(QtCore.QRect(200, -110, 441, 441))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ChefLogo_2.sizePolicy().hasHeightForWidth())
        self.ChefLogo_2.setSizePolicy(sizePolicy)
        self.ChefLogo_2.setMinimumSize(QtCore.QSize(441, 441))
        self.ChefLogo_2.setMaximumSize(QtCore.QSize(441, 441))
        self.ChefLogo_2.setSizeIncrement(QtCore.QSize(441, 441))
        self.ChefLogo_2.setBaseSize(QtCore.QSize(441, 441))
        self.ChefLogo_2.setText("")
        self.ChefLogo_2.setPixmap(QtGui.QPixmap(":/HomeCheflogo/homechef_Logo_NoBackground.png"))
        self.ChefLogo_2.setScaledContents(True)
        self.ChefLogo_2.setObjectName("ChefLogo_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 581, 601))
        self.label_2.setStyleSheet("background-image: url(:/BG/Untitled design.png);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/BG/Untitled design.png"))
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.searchButton = QtWidgets.QPushButton(Form)
        self.searchButton.setGeometry(QtCore.QRect(420, 240, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.searchButton.setFont(font)
        self.searchButton.setAutoFillBackground(False)
        self.searchButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 141, 2, 255), stop:0.507463 rgba(0, 167, 4, 255), stop:1 rgba(0, 139, 0, 255));\n"
"color: rgb(255, 255, 255);")
        self.searchButton.setText("SEARCH")
        self.searchButton.setFlat(False)
        self.searchButton.setObjectName("searchButton")
        self.ResetButton = QtWidgets.QPushButton(Form)
        self.ResetButton.setGeometry(QtCore.QRect(250, 240, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ResetButton.setFont(font)
        self.ResetButton.setAutoFillBackground(False)
        self.ResetButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 141, 2, 255), stop:0.507463 rgba(0, 167, 4, 255), stop:1 rgba(0, 139, 0, 255));\n"
"color: rgb(255, 255, 255);")
        self.ResetButton.setText("RESET")
        self.ResetButton.setFlat(False)
        self.ResetButton.setObjectName("ResetButton")
        self.YoutubeLabel = QtWidgets.QLabel(Form)
        self.YoutubeLabel.setGeometry(QtCore.QRect(50, 280, 111, 61))
        self.YoutubeLabel.setStyleSheet("background-image: url(:/Youtube/youtube-logo-png-46020.png);")
        self.YoutubeLabel.setText("")
        self.YoutubeLabel.setPixmap(QtGui.QPixmap(":/Youtube/youtube-logo-png-46020.png"))
        self.YoutubeLabel.setScaledContents(True)
        self.YoutubeLabel.setObjectName("YoutubeLabel")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(10, 290, 191, 171))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.RecipeLabel = QtWidgets.QLabel(Form)
        self.RecipeLabel.setGeometry(QtCore.QRect(360, 290, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.RecipeLabel.setFont(font)
        self.RecipeLabel.setObjectName("RecipeLabel")
        self.CalorieLabel = QtWidgets.QLabel(Form)
        self.CalorieLabel.setGeometry(QtCore.QRect(210, 470, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.CalorieLabel.setFont(font)
        self.CalorieLabel.setObjectName("CalorieLabel")
        self.RecipeInformation_2 = QtWidgets.QTextEdit(Form)
        self.RecipeInformation_2.setGeometry(QtCore.QRect(210, 290, 361, 171))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        self.RecipeInformation_2.setFont(font)
        self.RecipeInformation_2.setObjectName("RecipeInformation_2")
        self.Recipe1Label = QtWidgets.QLabel(Form)
        self.Recipe1Label.setGeometry(QtCore.QRect(20, 340, 171, 16))
        self.Recipe1Label.setText("")
        self.Recipe1Label.setObjectName("Recipe1Label")
        self.Recipe1Label_2 = QtWidgets.QLabel(Form)
        self.Recipe1Label_2.setGeometry(QtCore.QRect(20, 380, 171, 16))
        self.Recipe1Label_2.setText("")
        self.Recipe1Label_2.setObjectName("Recipe1Label_2")
        self.Recipe1Label_3 = QtWidgets.QLabel(Form)
        self.Recipe1Label_3.setGeometry(QtCore.QRect(20, 420, 171, 16))
        self.Recipe1Label_3.setText("")
        self.Recipe1Label_3.setObjectName("Recipe1Label_3")
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.CalorieValueLabel = QtWidgets.QLabel(Form)
        self.CalorieValueLabel.setGeometry(QtCore.QRect(30, 500, 191, 31))
        self.CalorieValueLabel.setText("")
        self.CalorieValueLabel.setObjectName("CalorieValueLabel")
        self.CarbLabel = QtWidgets.QLabel(Form)
        self.CarbLabel.setGeometry(QtCore.QRect(360, 500, 191, 31))
        self.CarbLabel.setText("")
        self.CarbLabel.setObjectName("CarbLabel")
        self.FatLabel = QtWidgets.QLabel(Form)
        self.FatLabel.setGeometry(QtCore.QRect(30, 550, 191, 31))
        self.FatLabel.setText("")
        self.FatLabel.setObjectName("FatLabel")
        self.ProteinLabel = QtWidgets.QLabel(Form)
        self.ProteinLabel.setGeometry(QtCore.QRect(360, 550, 191, 31))
        self.ProteinLabel.setText("")
        self.ProteinLabel.setObjectName("ProteinLabel")
        self.label_2.raise_()
        self.ChefLogo_2.raise_()
        self.RecipeSearchString.raise_()
        self.CalorieInfo.raise_()
        self.ChefLogo.raise_()
        self.searchButton.raise_()
        self.ResetButton.raise_()
        self.textEdit.raise_()
        self.YoutubeLabel.raise_()
        self.CalorieLabel.raise_()
        self.RecipeInformation_2.raise_()
        self.RecipeInformation.raise_()
        self.RecipeLabel.raise_()
        self.Recipe1Label.raise_()
        self.Recipe1Label_2.raise_()
        self.Recipe1Label_3.raise_()
        self.CalorieValueLabel.raise_()
        self.CarbLabel.raise_()
        self.FatLabel.raise_()
        self.ProteinLabel.raise_()

        self.searchButton.clicked.connect(self.searchButtonClicked)
        self.ResetButton.clicked.connect(self.resetButtonClicked)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "HomeChef"))
        self.RecipeLabel.setText(_translate("Form", "Recipe"))
        self.CalorieLabel.setText(_translate("Form", "Calorie Information"))

import Background_rc
