import sys
import os
from PyQt5 import QtCore, QtWidgets, QtMultimedia, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QSlider
from p import Ui_Form


class Example(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(Example, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('MediaPlayer')
        self.mplPlayer = QtMultimedia.QMediaPlayer()
        files = ['imagine-dragons_-_radioactive.mp3', '01-_01.mp3', 'eminem_-_not-afraid.mp3']
        self.playlist = QtMultimedia.QMediaPlaylist()
        for f in files:
            url = QtCore.QUrl.fromLocalFile(os.path.abspath(f))
            self.playlist.addMedia(QtMultimedia.QMediaContent(url))
        self.mplPlayer.setPlaylist(self.playlist)

        self.Button_play.clicked.connect(self.handlePlay_Pause)
        self.Button_stop.clicked.connect(self.handleStop)
        self.Button_next.clicked.connect(self.handleNext)
        self.Button_prev.clicked.connect(self.handlePrev)
        self.Button_shuffle.clicked.connect(self.mix)


    def mix(self):
        self.Button_shuffle.clicked.connect(self.playlist.shuffle)

    def handleNext(self):
        self.Button_next.clicked.connect(self.playlist.next)


    def handlePrev(self):
        self.Button_prev.clicked.connect(self.playlist.previous)

    def handlePlay_Pause(self):
        if self.Button_play.text() == '‣':
            self.Button_play.setText('||')
            # self._buffer.seek(0)
            self.mplPlayer.play()
        else:
            self.Button_play.setText('‣')
            self.mplPlayer.pause()

    def handleStop(self):
        self.mplPlayer.stop()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())


