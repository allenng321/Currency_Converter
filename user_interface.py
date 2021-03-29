import sys
import random
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.uic import loadUi
from apiclient import currency_client

client = currency_client(api_key="ad8e91b6f4b93492773d")
# res = client.get_data("HKD", "USD", 1)
# print(res)

class Currency(QtWidgets.QMainWindow):
    def __init__(self):
        super(Currency, self).__init__()
        loadUi("user.ui", self)
        self.convertButton.clicked.connect(self.convertFunc)
        self.initialBox.addItems(client.currencyList)
        self.targetBox.addItems(client.currencyList)
        

    def convertFunc(self):
        initialCurrency = str(self.initialBox.currentText())
        targetCurrency = str(self.targetBox.currentText())
        amount = int(self.amount.text())

        res = client.get_data(initialCurrency, targetCurrency, amount)
        text = "{} {} = {} {}".format(amount, initialCurrency, res, targetCurrency)
        self.outputText.setText(text)
        

app = QtWidgets.QApplication(sys.argv)

mainWindow = Currency()

widget = QtWidgets.QStackedWidget()
widget.addWidget(mainWindow)
widget.setFixedWidth(464)
widget.setFixedHeight(357)
widget.show()

app.exec_()