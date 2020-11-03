from gui.ChessWindow import ChessWindow
from PyQt5.QtWidgets import QApplication

# begin GUI instantiation
if __name__ == "__main__":
    app = QApplication(['chess'])
    window = ChessWindow(200)
    window.loadPGN('data/Nakamura.pgn')
    window.show()
    app.exec()