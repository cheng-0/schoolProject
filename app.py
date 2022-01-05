from PyQt5 import QtWidgets, uic, QtCore, QtMultimedia, QtMultimediaWidgets
import sys

class Intro(QtWidgets.QMainWindow):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        super(Intro, self).__init__()
        self.setWindowTitle('Intro')

        uic.loadUi('videoViewWithSkip.ui', self)
        self.player = QtMultimedia.QMediaPlayer()
        url = QtCore.QUrl.fromLocalFile("test.mp3")
        self.player.setMedia(QtMultimedia.QMediaContent(url))
        video = self.findChild(QtMultimediaWidgets.QVideoWidget, "video")
        self.player.setVideoOutput(video)
        self.player.setVolume(50);
        
        self.skipbutton.clicked.connect(self.skipButtonPressed)

    def skipButtonPressed(self):
        self.player.play()
        # self.switch_window.emit()

class Map(QtWidgets.QMainWindow):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        super(Map, self).__init__()
        self.setWindowTitle('Map') # The main Window

        uic.loadUi('map.ui', self)

        self.aPoint.clicked.connect(self.aPointPressed)

    def aPointPressed(self, point):
        self.switch_window.emit()

class Stage(QtWidgets.QMainWindow):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        super(Stage, self).__init__()
        self.setWindowTitle('stage')

        uic.loadUi('firstGameTeach.ui', self)


    def skipButtonPressed(self):
        self.switch_window.emit()



class Controller:

    def __init__(self):
        pass

    def show_intro(self):
        self.intro = Intro()
        self.intro.switch_window.connect(self.show_map)
        self.intro.show()
        

    def show_map(self):
        self.map = Map()
        self.map.switch_window.connect(self.show_stage_A)
        self.intro.close()
        self.map.show()

    def show_stage_A(self):
        self.stage = Stage()
        self.map.close()
        self.stage.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_intro()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()