from HomeChef import *


#def searchButtonClicked(self):
#    self.RecipeSearchString.setText("")
#    self.PleaseEnterLabel.setText("")
#
#    self.RecipeInformation.setText("\nRecipe Place holder\n")
#    self.textEdit.setText("\n\nPlace Holder for Youtube Links\n")
#    self.textEdit.wordWrapMode(True)


#self.searchButton.clicked.connect(self.searchButtonClicked)
#self.CancelButton.clicked.connect(self.closeButtonClicked)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


#If the background images change please use the below command to make sure all the
#elements are properly placed
#pyrcc5 .\elements\Background.qrc -o Background_rc.py

#Then to convert the UI file in python use the following command
#pyuic5 -o HomeChef.py -x HomeChef.ui
