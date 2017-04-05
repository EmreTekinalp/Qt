import sys

from PySide.QtGui import *
from PySide.QtCore import *
import romkan

import ui_list_widget
reload(ui_list_widget)
from ui_list_widget import Ui_MainWindow


class TableWidgetData(QTableWidget):
    def __init__(self, parent=None):
        super(TableWidgetData, self).__init__(parent)
        self.name_item = QTableWidgetItem('name')
        self.driver_item = QTableWidgetItem('driver')
        self.skin_item = QTableWidgetItem('skin mesh')
        self.sim_item = QTableWidgetItem('sim mesh')
        self.start_item = QTableWidgetItem('start frame')
        self.end_item = QTableWidgetItem('end frame')

        self._name = None
        self._driver = None

        # private methods
        self.__setup()

    def __setup(self):
        """Setup the initial state of the TableWidget"""
        self.setRowCount(6)
        self.setColumnCount(1)
        self.horizontalHeader().hide()
        self.horizontalHeader().setStretchLastSection(True)
        self.verticalHeader().setStretchLastSection(True)
        self.verticalHeader().setAlternatingRowColors(True)
        self.setVerticalHeaderItem(0, self.name_item)
        self.setVerticalHeaderItem(1, self.driver_item)
        self.setVerticalHeaderItem(2, self.skin_item)
        self.setVerticalHeaderItem(3, self.sim_item)
        self.setVerticalHeaderItem(4, self.start_item)
        self.setVerticalHeaderItem(5, self.end_item)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        self.table.setItem(1, -1, self.item)
        self.item.setText(value)

    @property
    def driver(self):
        return self._driver

    @driver.setter
    def driver(self, value):
        self._driver = value
        self.table.setItem(1, 0, self.item)
        self.item.setText(value)


class ListWidget(QMainWindow, Ui_MainWindow):
    """Example of a tableWidget class with custom functionality."""

    def __init__(self, parent=None):
        """Initialize ListWidget class"""
        super(ListWidget, self).__init__(parent)
        self.setupUi(self)
        self.createBtn.clicked.connect(self.add_item)
        self.pagesWidget = QStackedWidget()
        self.horizontalLayout.addWidget(self.pagesWidget, 1)
        self.tables = list()
        self.listWidget.itemClicked.connect(self.do_something)

    def add_item(self):
        """Add a new item to the list view"""
        self.listWidget.addItem('RENAME')
        # item = self.listWidget.item(self.listWidget.count() - 1)
        table = TableWidgetData(self)
        self.tables.append(table)
        self.pagesWidget.addWidget(table)
        self.pagesWidget.setCurrentIndex(self.listWidget.count() - 1)
        print self.pagesWidget.currentIndex(), self.pagesWidget.count()

    def do_something(self):
        self.pagesWidget.setCurrentIndex(self.listWidget.currentRow())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ListWidget()
    window.show()
    sys.exit(app.exec_())
