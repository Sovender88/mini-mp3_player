from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtCore import QUrl, QAbstractListModel, Qt
from PyQt5.QtMultimedia import QMediaPlayer, QMediaPlaylist, QMediaContent
from last_py import Ui_MainWindow
#http://qaru.site/questions/1246590/pyqt-proper-use-of-emit-and-pyqtsignal
#https://www.tutorialspoint.com/python3/string_zfill.htm


def hhmmss(ms):
    ms = int(ms)
    minutes = str(ms // 60000).zfill(2)
    seconds = str(ms // 1000 % 60).zfill(2)
    return "{}:{}".format(minutes, seconds)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.player = QMediaPlayer()
        self.player.play()

        self.playlist = QMediaPlaylist()
        self.player.setPlaylist(self.playlist)

        self.playButton.clicked.connect(self.player.play)
        self.pauseButton.clicked.connect(self.player.pause)
        self.stopButton.clicked.connect(self.player.stop)
        self.volumeSlider.valueChanged.connect(self.player.setVolume)
        self.randomButton.clicked.connect(self.handle_shuffle)

        self.previousButton.clicked.connect(self.playlist.previous)
        self.nextButton.clicked.connect(self.playlist.next)

        self.model = Playlist(self.playlist)
        self.playlistView.setModel(self.model)
        self.playlist.currentIndexChanged.connect(self.position_changed)

        self.player.durationChanged.connect(self.update_duration)
        self.player.positionChanged.connect(self.update_position)
        self.timeSlider.valueChanged.connect(self.player.setPosition)

        self.open_file_action.triggered.connect(self.open)
        #self.setAcceptDrops(True)

    def handle_shuffle(self):
        self.playlist.shuffle()

    def open(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open file", "", "mp3 Audio (*.mp3)")

        if path:
            self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile(path)))

        self.model.layoutChanged.emit()

    def update_duration(self):
        self.timeSlider.setMaximum(self.player.duration())
        duration = self.player.duration()

        if duration >= 0:
            self.totalTimeLabel.setText(hhmmss(duration))

    def update_position(self):
        position = self.player.position()
        if position >= 0:
            self.currentTimeLabel.setText(hhmmss(position))

        self.timeSlider.blockSignals(True)
        self.timeSlider.setValue(position)
        self.timeSlider.blockSignals(False)

    def position_changed(self, i):
        if i > -1:
            x = self.model.index(i)
            self.playlistView.setCurrentIndex(x)


class Playlist(QAbstractListModel):
    def __init__(self, playlist):
        super(Playlist, self).__init__()
        self.playlist = playlist

    def data(self, index, role):
        if role == Qt.DisplayRole:
            media = self.playlist.media(index.row())
            return media.canonicalUrl().fileName()

    def rowCount(self, index):
        return self.playlist.mediaCount()


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

