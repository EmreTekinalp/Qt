# This shows how to color a cell in a tableWidget
from PySide import QtGui, QtCore

table = QtGui.QTableWidget()
tableItem = QtGui.QTableWidgetItem()

# initiate table
table.setWindowTitle('My Table Escalation')
table.resize(400, 250)
table.setRowCount(4)
table.setColumnCount(2)

# set data
table.setItem(0,0, QtGui.QTableWidgetItem("Item (1,1)"))
table.setItem(0,1, QtGui.QTableWidgetItem("Item (1,2)"))
table.setItem(1,0, QtGui.QTableWidgetItem("Item (2,1)"))
table.setItem(1,1, QtGui.QTableWidgetItem("Item (2,2)"))
table.setItem(2,0, QtGui.QTableWidgetItem("Item (3,1)"))
table.setItem(2,1, QtGui.QTableWidgetItem("Item (3,2)"))
table.setItem(3,0, QtGui.QTableWidgetItem("Item (4,1)"))
table.setItem(3,1, QtGui.QTableWidgetItem("Item (4,2)"))
table.item(3, 0).setBackground(QtCore.Qt.red)
table.show()
