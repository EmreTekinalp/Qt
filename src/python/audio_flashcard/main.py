import os
import sys
import time

from PySide.QtGui import *
from PySide.QtCore import *
import romkan
from gtts import gTTS
from playsound import playsound

from ui_audioFlashcard import Ui_MainWindow


class VocabPage(QTableWidget):
    def __init__(self, parent=None):
        super(VocabPage, self).__init__(parent)



class AudioPlayer(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(AudioPlayer, self).__init__(parent)
        self.setupUi(self)
        self.__setup_table()
        self.lang_mode = 0
        self.soundfiles = list()

        self.tableWidget.currentCellChanged.connect(self.change_lang_mode)
        self.tableWidget.cellChanged.connect(self.default_to_hiragana)
        self.previousBtn.clicked.connect(self.go_to_previous_page)
        self.nextBtn.clicked.connect(self.go_to_next_page)

    def __setup_table(self):
        english_item = QTableWidgetItem('english')
        english_item.setBackground(QColor(81, 81, 81))
        english_item.setSizeHint(QSize(450, 35))
        self.tableWidget.setHorizontalHeaderItem(0, english_item)
        japanese_item = QTableWidgetItem('japanese')
        self.tableWidget.setHorizontalHeaderItem(1, japanese_item)
        self.tableWidget.verticalHeader().setResizeMode(QHeaderView.Stretch)
        self.tableWidget.setColumnWidth(0, self.width() / 2)
        self.tableWidget.setColumnWidth(1, self.width() / 2)

    def go_to_previous_page(self):
        self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() - 1)

    def go_to_next_page(self):
        self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() + 1)

    def change_lang_mode(self):
        self.lang_mode = 0
        # print("Row %d and Column %d was clicked" % (row, column))

    def default_to_hiragana(self):
        items = self.tableWidget.selectedItems()
        if items:
            for item in items:
                if item.column():
                    if not self.lang_mode:
                        item.setText(romkan.to_hiragana(item.text()))

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
        for item in self.get_japanese_items():
            file_name = '%s.mp3' % romkan.to_roma(item.text().replace(' ', '_'))
            path = os.path.join(self.get_japanese_data_path(), file_name)
            self.soundfiles.append(path)
            if not os.path.exists(path):
                tts = gTTS(text=item.text(), lang='ja')
                tts.save(path)
            playsound(path)

    @staticmethod
    def get_japanese_data_path():
        return os.path.abspath(os.path.join(__file__, os.pardir, 'data', 'japanese'))

    def listen_english(self):
        for item in self.get_english_items():
            file_name = '%s.mp3' % item.text().replace(' ', '_')
            path = os.path.join(self.get_english_data_path(), file_name)
            self.soundfiles.append(path)
            if not os.path.exists(path):
                tts = gTTS(text=item.text(), lang='en')
                tts.save(path)
            playsound(path)

    def get_english_items(self):
        return [i for i in self.tableWidget.selectedItems() if not i.column()]

    @staticmethod
    def get_english_data_path():
        return os.path.abspath(os.path.join(__file__, os.pardir, 'data', 'english'))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AudioPlayer()
    window.show()
    sys.exit(app.exec_())
