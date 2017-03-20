import sys

from PySide.QtGui import *
from PySide.QtCore import *
import romkan

import ui_tableWidget
reload(ui_tableWidget)
from ui_tableWidget import Ui_MainWindow


class MyWidget(QWidget):
    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent)
        self.is_pressed = False
        self.setStyleSheet('background-color: rgba(0, 0, 0, 0);')

    def enterEvent(self, event):
        if not self.is_pressed:
            self.setStyleSheet('background-color: rgb(255, 170, 0);'
                               'color: rgb(0, 0, 0)')

    def leaveEvent(self, event):
        if not self.is_pressed:
            self.setStyleSheet('background-color: rgba(0, 0, 0, 0);'
                               'color: rgb(0, 0, 0)')

    def mousePressEvent(self, event):
        self.setStyleSheet('background-color: rgb(110, 100, 220);')
        self.is_pressed = True
        for w in self.window().rows:
            if w.parent() != self:
                w.parent().is_pressed = False
                w.parent().setStyleSheet('background-color: rgba(0, 0, 0, 0);')

    def mouseDoubleClickEvent(self, event):
        print 'hahaha'


class TableWidget(QMainWindow, Ui_MainWindow):
    """Example of a tableWidget class with custom functionality."""

    def __init__(self, parent=None):
        """Initialize TableWidget class"""
        super(TableWidget, self).__init__(parent)
        self.setupUi(self)
        self.tableWidget.setColumnCount(1)
        self.createBtn.clicked.connect(self.create_row)
        self.rows = list()
        self.widgets = list()

    def create_row(self):
        """Once clicked on the create button generate a new row with widgets."""
        rows = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(rows + 1)
        # create a row with a custom widget
        widget = MyWidget(self)
        widget.setObjectName('MyWidget')
        layout = QHBoxLayout()
        widget.setLayout(layout)
        # labels
        label = QLabel('  %s. quick info' % rows)
        label.setStyleSheet('QLabel{color: rgb(200, 200, 200);}'
                            'QWidget:hover{color: rgb(0, 0, 0);}')
        # buttons
        removeBtn = QPushButton('X')
        removeBtn.setMaximumWidth(50)
        removeBtn.setMaximumHeight(100)
        removeBtn.setStyleSheet('QPushButton{'
                                'background-color: rgb(200, 50, 100);'
                                'border: none;}'
                                'QPushButton:hover{'
                                'background-color: rgb(255, 50, 100);'
                                'border: none;}')

        # layout
        layout.addWidget(label, Qt.AlignRight)
        layout.addWidget(removeBtn, Qt.AlignLeft)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        # implement the widget to the row
        self.tableWidget.setCellWidget(rows, 0, widget)
        self.rows.append(removeBtn)

        # make sure to enable removing the row via the remove button
        removeBtn.clicked.connect(self.remove_row)

    def remove_row(self):
        """Based on the index in the row list, delete the entire row."""
        for f in [self.tableWidget.removeRow, self.rows.pop]:
            f(self.rows.index(self.sender()))

    def double(self):
        print "double Clicked"
        return

    def contextMenuEvent(self, event):
        self.menu = QMenu(self)
        renameAction = QAction('Rename', self)
        renameAction.triggered.connect(lambda: self.renameSlot(event))
        self.menu.addAction(renameAction)
        # add other required actions
        self.menu.popup(QCursor.pos())

    def renameSlot(self, event):
        print "renaming slot called"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TableWidget()
    window.show()
    sys.exit(app.exec_())
