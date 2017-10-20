"""
@author: Emre Tekinalp
@date: Oct 17, 2017
@contact: e.tekinalp@icloud.com
@package: audioFlashcard/main
@brief: run a digital vocabulary book
@requires: PyQt5; pygame; romkan; gtts
@version: 1.0.0
"""

__author__ = 'Emre Tekinalp'
__copyright__ = 'Copyright (C) 2017 Digital Epics'
__license__ = 'Gravity of Explosion'
__version__ = '1.0'

# python
import json
import os
import sys

# third party modules
import pygame
import romkan
from gtts import gTTS

# pySide2
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from ui_audioFlashcard import Ui_MainWindow


class DigitalVocabulary(QMainWindow, Ui_MainWindow):
    """Digital Vocabulary UI to play user typed words in english and japanese"""

    def __init__(self, parent=None):
        """Initialize DigitalVocabulary class.

        :param parent: specifies the parent window of this child UI
        :type parent: QtWidget
        """
        super(DigitalVocabulary, self).__init__(parent)
        self.setupUi(self)

        self.__setup_title()

        self.previousBtn.clicked.connect(self.go_to_previous_page)
        self.nextBtn.clicked.connect(self.go_to_next_page)

    def __setup_title(self):
        self.setStyleSheet('background-color: rgb(30, 30, 30);'
                           'color: rgb(255, 255, 255);'
                           'alternate-background-color: rgb(40, 40, 40);'
                           'font-family: Segoe Print;')
        self.pageLab.setText('0')
        self.pageLab.setStyleSheet('font-family: Segoe Print; font-size: 14pt;'
                                   'color: rgb(255, 183, 0);')
        self.nameLed.setStyleSheet('color: rgb(255, 183, 0);')

    def go_to_previous_page(self):
        self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() - 1)
        self.pageLab.setText('%s' % self.stackedWidget.currentIndex())

    def go_to_next_page(self):
        self.stackedWidget.addWidget(VocabPage(self))
        self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() + 1)
        self.pageLab.setText('%s' % self.stackedWidget.currentIndex())

    def japanese_path(self):
        path = os.path.abspath(os.path.join(self.page_path(), 'japanese'))
        if not os.path.exists(path):
            os.mkdir(path)
        return path

    def english_path(self):
        path = os.path.abspath(os.path.join(self.page_path(), 'english'))
        if not os.path.exists(path):
            os.mkdir(path)
        return path

    def config_path(self):
        return os.path.abspath(os.path.join(self.page_path(), 'config.json'))

    def page_path(self):
        page = 'page_%s' % self.stackedWidget.currentIndex()
        path = os.path.abspath(os.path.join(self.data_path(), page))
        if not os.path.exists(path):
            os.mkdir(path)
        return path

    @staticmethod
    def data_path():
        return os.path.abspath(os.path.join(__file__, os.pardir, 'data'))


class VocabPage(QWidget):
    def __init__(self, parent=None):
        super(VocabPage, self).__init__(parent)

        # public variables
        self.layout = QVBoxLayout()
        self.tableWidget = QTableWidget()
        self.label = QLabel()
        self.lineEdit = QLineEdit()
        self.lang_mode = 0
        self.soundfiles = list()
        self.page_data = dict()
        self.data = dict()

        # private methods
        self.__setup_page()
        self.__setup_data()

        # connections
        self.tableWidget.currentCellChanged.connect(self.change_lang_mode)
        self.tableWidget.cellChanged.connect(self.default_to_hiragana)
        self.lineEdit.textChanged.connect(self.set_topic_data)

    def __setup_page(self):
        self.label.setText('Topic:')
        self.label.setStyleSheet('font-size: 12pt;')
        self.lineEdit.setPlaceholderText('Please enter topic name')
        self.lineEdit.setStyleSheet('qproperty-frame: false; font-size: 12pt;'
                                    'color: rgb(255, 183, 0);')
        # layout
        hlayout = QHBoxLayout()
        hlayout.addWidget(self.label)
        hlayout.addWidget(self.lineEdit)
        self.layout.addLayout(hlayout)
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

        # tableWidget
        self.tableWidget.setRowCount(12)
        self.tableWidget.setColumnCount(2)
        english_item = QTableWidgetItem('english')
        japanese_item = QTableWidgetItem('japanese')

        # set headers and rows
        self.tableWidget.setHorizontalHeaderItem(0, english_item)
        self.tableWidget.setHorizontalHeaderItem(1, japanese_item)
        # self.tableWidget.verticalHeader().setResizeMode(QHeaderView.Stretch)
        # self.tableWidget.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget.setColumnWidth(0, self.window().width() * 0.4)
        self.tableWidget.setColumnWidth(1, self.window().width() * 0.4)
        self.tableWidget.setFrameStyle(QFrame.NoFrame)
        self.tableWidget.setAlternatingRowColors(True)

        # stylesheets
        style = ('::section {background-color: rgb(28, 28, 28);'
                 'color: rgb(183, 10, 70); border: 1px solid rgb(30, 30, 30);}')
        self.tableWidget.horizontalHeader().setStyleSheet(style)
        self.tableWidget.verticalHeader().setStyleSheet(style)
        style = ('QTableCornerButton::section{background: rgb(28, 28, 28);}'
                 'QTableWidget{selection-background-color: rgba(150, 170, 255, 80);}')
        self.tableWidget.setStyleSheet(style)

    def __setup_data(self):
        page = 'page_%s' % (self.window().stackedWidget.currentIndex() + 1)
        path = os.path.abspath(os.path.join(self.window().data_path(), page, 'config.json'))
        if not os.path.exists(path):
            return
        with open(path) as data_file:
            data = json.load(data_file)
        if not data:
            return
        for page in data:
            if page == 'topic':
                self.lineEdit.setText(data[page])
                continue
            for cell, text in data[page].items():
                row, col = cell.split(',')
                item = QTableWidgetItem(text)
                self.tableWidget.setItem(int(row), int(col), item)
                if int(col):
                    item = QTableWidgetItem(romkan.to_hiragana(text))
                    self.tableWidget.setItem(int(row), int(col), item)
        self.data = data

    def change_lang_mode(self):
        self.lang_mode = 0

    def default_to_hiragana(self, row, col):
        items = self.tableWidget.selectedItems()
        if items:
            for item in items:
                if item.column():
                    if not self.lang_mode:
                        item.setText(romkan.to_hiragana(item.text()))
        item = self.tableWidget.item(row, col)
        if item:
            self.page_data['%s,%s' % (row, col)] = item.text()
            if col:
                self.page_data['%s,%s' % (row, col)] = romkan.to_roma(item.text())
        self.data['page_%s' % self.window().pageLab.text()] = self.page_data
        self.update_config(self.data)

    def set_topic_data(self):
        self.data['topic'] = self.lineEdit.text()

    def contextMenuEvent(self, event):
        if self.get_japanese_items():
            menu = QMenu(self)
            # create
            hiragana = QAction('Show Hiragana', self)
            katakana = QAction('Show Katakana', self)
            romanji = QAction('Show Romanji', self)
            listen = QAction('Listen', self)
            # trigger
            hiragana.triggered.connect(self.to_hiragana)
            katakana.triggered.connect(self.to_katakana)
            romanji.triggered.connect(self.to_romanji)
            listen.triggered.connect(self.listen_japanese)
            # add
            menu.addAction(hiragana)
            menu.addAction(katakana)
            menu.addAction(romanji)
            menu.addAction(listen)
            # add other required actions
            menu.popup(QCursor.pos())
        elif self.get_english_items():
            menu = QMenu(self)
            listen = QAction('Listen', self)
            listen.triggered.connect(self.listen_english)
            menu.addAction(listen)
            menu.popup(QCursor.pos())

    def to_hiragana(self):
        self.lang_mode = 0
        for item in self.get_japanese_items():
            item.setText(romkan.to_hiragana(romkan.to_roma(item.text())))

    def to_katakana(self):
        self.lang_mode = 1
        for item in self.get_japanese_items():
            item.setText(romkan.to_katakana(romkan.to_roma(item.text())))

    def to_romanji(self):
        self.lang_mode = 2
        for item in self.get_japanese_items():
            item.setText(romkan.to_roma(item.text()))

    def get_japanese_items(self):
        return [i for i in self.tableWidget.selectedItems() if i.column()]

    def listen_japanese(self):
        pygame.mixer.init()
        for i, item in enumerate(self.get_japanese_items()):
            file_name = '%s.mp3' % romkan.to_roma(item.text().replace(' ', '_'))
            path = os.path.join(self.window().japanese_path(), file_name)
            self.soundfiles.append(path)
            if not os.path.exists(path):
                tts = gTTS(text=item.text(), lang='ja')
                tts.save(path)
            pygame.mixer.music.load(path)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(20000)

    def listen_english(self):
        pygame.mixer.init()
        for item in self.get_english_items():
            file_name = '%s.mp3' % item.text().replace(' ', '_')
            path = os.path.join(self.window().english_path(), file_name)
            self.soundfiles.append(path)
            if not os.path.exists(path):
                tts = gTTS(text=item.text(), lang='en')
                tts.save(path)
            if not os.path.exists(path):
                return
            pygame.mixer.music.load(path)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(20000)

    def get_english_items(self):
        return [i for i in self.tableWidget.selectedItems() if not i.column()]

    def update_config(self, data):
        path = self.window().config_path()
        result = dict()
        if os.path.exists(path):
            with open(path) as data_file:
                result = json.load(data_file)
        for key, value in result.items():
            if isinstance(value, dict):
                value.update(data[key])
            else:
                result[key] = data[key]
        with open(path, 'w') as outfile:
            json.dump(result, outfile, indent=4, sort_keys=True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DigitalVocabulary()
    window.show()
    sys.exit(app.exec_())
