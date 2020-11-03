import chess
import chess.svg
import chess.pgn

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QWidget


# QtWidget to handle the generation of chess window GUI
class ChessWindow(QWidget):
    def __init__(self, frameInterval=500):
        super().__init__()

        # set geometry of container window
        self.setGeometry(100, 100, 800, 800)

        # set geometry of inner svg widget window
        self.widgetSvg = QSvgWidget(parent=self)
        self.widgetSvg.setGeometry(10, 10, 780, 780)

        # default starting chessboard
        self.chessboard = chess.Board()

        # track the moves via index
        self.moves = []
        self.moveIndex = 0

        # flag to mark playback animation
        self.playback = False

        # use Qtimer for playback animation
        self.animationTimer = QTimer(self)
        # frameInterval = ms until next playback frame
        self.animationTimer.setInterval(frameInterval)
        self.animationTimer.timeout.connect(self.renderNextMove)

        # generate svg of chessboard 
        self.chessboardSvg = chess.svg.board(self.chessboard).encode("UTF-8")
        self.widgetSvg.load(self.chessboardSvg)

    # override mouse event method from QWidget
    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.renderNextMove()
        elif QMouseEvent.button() == Qt.RightButton:
            self.renderPreviousMove()
    
    # override key event to start playback animation by pressing space bar 
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            if not self.playback:
                self.animationTimer.start()
                self.playback = True
            elif self.playback:
                self.animationTimer.stop()
                self.playback = False


    # render updated chess.Board
    def renderBoard(self):
        self.chessboardSvg = chess.svg.board(self.chessboard).encode("UTF-8")
        self.widgetSvg.load(self.chessboardSvg)
        self.update()
        return
    
    # render the board produced by prevMove passed in
    def renderPreviousMove(self):
        if self.moveIndex == 0:
            print("No previous move exists.")
            return
        self.chessboard.pop()
        self.moveIndex -= 1
        self.renderBoard()
        return

    # render the board produced by nextMove passed in
    def renderNextMove(self):
        if self.moveIndex == len(self.moves):
            print("No next move exists.")
            return
        self.chessboard.push(self.moves[self.moveIndex])
        self.moveIndex += 1
        self.renderBoard()
        return

    # load pgn and load moves list into class var
    def loadPGN(self, filePath):
        # pass in filePath string to open
        pgn = open(filePath)
        game = chess.pgn.read_game(pgn)
        self.chessboard = game.board()
        for move in game.mainline_moves():
            self.moves.append(move)
        return