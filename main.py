import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton
from PyQt5.QtGui import QPainter, QFont
from PyQt5.QtCore import Qt, QPoint, QTimer
from game import CalculatingGame


class UserInput(QTextEdit):

    def __init__(self, parent):
        super(QTextEdit, self).__init__(parent)
        self.game = None

    def setGame(self, game):
        self.game = game

    def keyPressEvent(self, ev):

        if ev.key() == Qt.Key_Enter - 1:
            if self.game:
                self.game.processValue(self.toPlainText())
            self.setPlainText("")
            return
        QTextEdit.keyPressEvent(self, ev)


class PlayButton(QPushButton):
    def __init__(self, parent, setting):
        super(QPushButton, self).__init__(setting["label"], parent)
        self.pt = parent

        width = 200
        height = 50
        startx = 400 - width
        starty = 0

        self.clicked.connect(self.clickedButton)
        self.resize(width, height)
        self.move(startx + setting["xoffset"], starty + setting["yoffset"])
        self.action = setting["ops"]

    def clickedButton(self):
        game = None
        if '+' in self.action:
            game = CalculatingGame(['+'])
        if '-' in self.action:
            game = CalculatingGame(['-'])
        if '*' in self.action:
            game = CalculatingGame(['*'])
        if '/' in self.action:
            game = CalculatingGame(['/'])
        if '%' in self.action:
            game = CalculatingGame(['%'])
        if '.' in self.action:
            game = CalculatingGame(['+', '-', '*', '/', '%'])
        self.pt.clickedButton(game)


class CalculatingGameWidget(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.resize(800, 550)
        self.setFixedSize(self.size())
        self.timer = QTimer()
        self.timer.timeout.connect(self.stepTimer)
        self.game = None
        self.buttons = []

        self.edit = UserInput(self)
        self.edit.setAlignment(Qt.AlignCenter)
        font = QFont()
        font.setPointSize(32)
        self.edit.setFont(font)
        self.edit.resize(200, 45)
        self.edit.move(300, 500)

        settings = [
            {
                "label": 'Összeadás könnyű',
                "xoffset": 0,
                "yoffset": 0,
                "ops": '+'
            },
            {
                "label": 'Összeadás nehéz',
                "xoffset": 200,
                "yoffset": 0,
                "ops": '++'
            },
            {
                "label": 'Kivonás könnyű',
                "xoffset": 0,
                "yoffset": 50,
                "ops": '-'
            },
            {
                "label": 'Kivonás nehéz',
                "xoffset": 200,
                "yoffset": 50,
                "ops": '--'
            },
            {
                "label": 'Szorzás könnyű',
                "xoffset": 0,
                "yoffset": 100,
                "ops": '*'
            },
            {
                "label": 'Szorzás nehéz',
                "xoffset": 200,
                "yoffset": 100,
                "ops": '**'
            },
            {
                "label": 'Osztás könnyű',
                "xoffset": 0,
                "yoffset": 150,
                "ops": '/'
            },
            {
                "label": 'Osztás nehéz',
                "xoffset": 200,
                "yoffset": 150,
                "ops": '//'
            },
            {
                "label": 'Maradék könnyű',
                "xoffset": 0,
                "yoffset": 200,
                "ops": "%"
            },
            {
                "label": 'Maradék nehéz',
                "xoffset": 200,
                "yoffset": 200,
                "ops": "%%"
            },
            {
                "label": 'Minden könnyű',
                "xoffset": 0,
                "yoffset": 250,
                "ops": '.'
            },
            {
                "label": 'Minden nehéz',
                "xoffset": 200,
                "yoffset": 250,
                "ops": '..'
            }
        ]

        for setting in settings:
            button = PlayButton(self, setting)
            self.buttons.append(button)

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        font = QFont()
        font.setPointSize(32)
        if self.game is None:
            return
        qp.setFont(font)
        for task in self.game.getTasks():
            qp.drawText(QPoint(
                task.getPositionX(),
                task.getPositionY()),
                str(task))
        qp.end()

    def stepTimer(self):
        self.game.stepTimer()
        self.update()

    def clickedButton(self, game):
        self.game = game
        self.edit.setGame(game)
        for btn in self.buttons:
            btn.setVisible(False)
        self.timer.start(100)


def main():
    app = QApplication(sys.argv)
    w = CalculatingGameWidget()
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
