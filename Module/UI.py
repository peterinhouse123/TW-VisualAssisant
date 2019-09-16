



import time
from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget)
from PyQt5.QtGui import QIcon, QPixmap


class App(QWidget):

    def __init__(self,image):
        super().__init__()
        self.title = '萌妹子通知'
        self.left = 1100
        self.top= 100
        self.image = image
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create widget
        label = QLabel(self)
        pixmap = QPixmap(self.image)
        label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())

        self.show()


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    ex = App(image="../imageUnityGirl02.png")
    sys.exit(app.exec_())
