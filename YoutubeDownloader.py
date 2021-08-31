from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
from pytube import YouTube
from tkinter import *
from moviepy.editor import *

class Pencere(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        self.ustAyarlar()
        self.anaMenu()
        self.show()
    def anaMenu(self):
        widget = QWidget()
        h_box= QHBoxLayout()
        yazi=QLabel("<b>YouTube Linkini Giriniz:</b>")
        self.link=QLineEdit()
        button=QPushButton("İndir")

        button.clicked.connect(self.indir)

        h_box.addWidget(yazi)
        h_box.addWidget(self.link)
        h_box.addWidget(button)

        widget.setLayout(h_box)

        self.setCentralWidget(widget)



    def indir(self):
        url = self.link.text()
        YouTube(url).streams.get_highest_resolution().download()
    def ustAyarlar(self):
        self.setWindowTitle("Produced by Yasin Öncü - Youtube Video Downloader")
        self.setWindowIcon(QIcon("youtube-icon.png"))
        self.setGeometry(250, 250, 600,100)
        self.setMaximumSize(1000,100)
        self.setMinimumSize(600,100)

if __name__=="__main__":
    app = QApplication(sys.argv)
    pencere=Pencere()
    sys.exit(app.exec())