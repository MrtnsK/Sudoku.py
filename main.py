# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bt.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import numpy as np
import check
import solver
import datetime
import time

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(406, 316)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(310, 10, 81, 31))
		self.label.setObjectName("label")
		self.time = QtWidgets.QLabel(self.centralwidget)
		self.time.setGeometry(QtCore.QRect(310, 40, 149, 14))
		self.time.setObjectName("time")
		self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
		self.layoutWidget.setGeometry(QtCore.QRect(310, 60, 77, 54))
		self.layoutWidget.setObjectName("layoutWidget")
		self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
		self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
		self.pushButton.setObjectName("pushButton")
		self.verticalLayout_2.addWidget(self.pushButton)
		self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
		self.pushButton_2.setObjectName("pushButton_2")
		self.verticalLayout_2.addWidget(self.pushButton_2)
		self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
		self.plainTextEdit.setGeometry(QtCore.QRect(20, 10, 251, 251))
		self.plainTextEdit.setObjectName("plainTextEdit")
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 406, 21))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)
		
		self.grid = np.zeros((9,9))
		self.pushButton.clicked.connect(self.get_input)
		self.pushButton_2.clicked.connect(self.solve)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.label.setText(_translate("MainWindow", "Time taken:"))
		self.time.setText(_translate("MainWindow", "0"))
		self.pushButton.setText(_translate("MainWindow", "input"))
		self.pushButton_2.setText(_translate("MainWindow", "solve"))

	def get_input(self):
		tmp = self.plainTextEdit.toPlainText()
		if check.fill_grid(self.grid, tmp.strip()) == -1:
			self.error("La grille semble incorrect")
		else:
			self.plainTextEdit.setPlainText(check.layout(self.grid))

	def solve(self):
		if check.check_valid(self.grid) is True:
			tmp = datetime.datetime.now()
			solver.solver(self.grid)
			tmp = datetime.datetime.now() - tmp
			self.plainTextEdit.setPlainText(check.layout(self.grid))
			self.time.setText(f"{tmp.total_seconds()} s")
		else :
			self.error("La grille semble invalide")
			
	def error(self, msg_Error):
		msg = QMessageBox()
		msg.setIcon(QMessageBox.Critical)
		msg.setText(msg_Error)
		msg.setWindowTitle("Error")
		msg.setStandardButtons(QMessageBox.Ok)
		msg.exec()

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MenuWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MenuWindow)
	MenuWindow.show()
	sys.exit(app.exec_())
