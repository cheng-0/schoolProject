import sys
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class VideoWindow(QMainWindow):
     def __init__(self):
         super(VideoWindow, self).__init__()
         self.setWindowTitle('QMediaPlayer TEST')
         self.resize(640, 480)

         # QMediaPlayer
         self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
         self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile('hellomovie.mp4')))

         # Set widget
         self.videoWidget = QVideoWidget()
         self.videoWidget.setGeometry(self.pos().x(), self.pos().y(), self.width(), self.height())
         self.setCentralWidget(self.videoWidget)
         self.mediaPlayer.setVideoOutput(self.videoWidget)

         # Play
         self.mediaPlayer.play()


if __name__ == '__main__':
     app = QApplication([])
     window = VideoWindow()
     window.show()
     sys.exit(app.exec_())