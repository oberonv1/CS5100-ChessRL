import chess
import chess.svg

from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QApplication, QWidget



class ChessWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 500, 500)

        self.widgetSvg = QSvgWidget(parent=self)
        self.widgetSvg.setGeometry(10, 10, 480, 480)


        self.chessboard = chess.Board('r1bqkb1r/pppp1Qpp/2n2n2/4p3/2B1P3/8/PPPP1PPP/RNB1K1NR b KQkq - 0 4')

        self.chessboardSvg = chess.svg.board(self.chessboard, size=200).encode("UTF-8")
        self.widgetSvg.load(self.chessboardSvg)

if __name__ == "__main__":
    app = QApplication([])
    window = ChessWindow()
    window.show()
    app.exec()