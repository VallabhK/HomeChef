# Data Focused Python B1
"""
# Data Focused Python B1
# Created by: 
# 1. Vallabh Karanjkar-vkaranjk
# 2. Mohini Jain- mohinij
# 3. Rohit Jain- rohitj
# Group 24
"""
#This is the entry point of the application


from HomeChef import *

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

