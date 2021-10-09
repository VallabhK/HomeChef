# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomeChef.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(580, 603)
        Form.setWindowTitle("")
        self.RecipeSearchString = QtWidgets.QTextEdit(Form)
        self.RecipeSearchString.setEnabled(True)
        self.RecipeSearchString.setGeometry(QtCore.QRect(250, 190, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        self.RecipeSearchString.setFont(font)
        self.RecipeSearchString.setStyleSheet("border-radius:50;")
        self.RecipeSearchString.setObjectName("RecipeSearchString")
        self.CancelButton = QtWidgets.QPushButton(Form)
        self.CancelButton.setGeometry(QtCore.QRect(530, 10, 41, 41))
        self.CancelButton.setObjectName("CancelButton")
        self.VideoRecommeder = QtWidgets.QGraphicsView(Form)
        self.VideoRecommeder.setGeometry(QtCore.QRect(10, 290, 191, 171))
        self.VideoRecommeder.setObjectName("VideoRecommeder")
        self.RecipeInformation = QtWidgets.QTextEdit(Form)
        self.RecipeInformation.setGeometry(QtCore.QRect(210, 290, 361, 171))
        self.RecipeInformation.setObjectName("RecipeInformation")
        self.CalorieInfo = QtWidgets.QGraphicsView(Form)
        self.CalorieInfo.setGeometry(QtCore.QRect(10, 470, 561, 121))
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
        self.ChefLogo_2.setText("")
        self.ChefLogo_2.setPixmap(QtGui.QPixmap(":/HomeCheflogo/homechef_Logo_NoBackground.png"))
        self.ChefLogo_2.setScaledContents(True)
        self.ChefLogo_2.setObjectName("ChefLogo_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(290, 240, 131, 41))
        self.label.setStyleSheet("background-image: url(:/Search/SearchButton.png);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/Search/SearchButton.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 240, 131, 41))
        self.pushButton_2.setStyleSheet("color : rgba(0, 0, 0,0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(320, 190, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.ChefLogo_2.raise_()
        self.label.raise_()
        self.RecipeSearchString.raise_()
        self.CancelButton.raise_()
        self.VideoRecommeder.raise_()
        self.RecipeInformation.raise_()
        self.CalorieInfo.raise_()
        self.ChefLogo.raise_()
        self.pushButton_2.raise_()
        self.label_3.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.CancelButton.setText(_translate("Form", "CLOSE"))
        self.pushButton_2.setText(_translate("Form", "PushButton"))
        self.label_3.setText(_translate("Form", "Please enter a food item!"))

#import Background_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

