from gui.ChessWindow import ChessWindow
from PyQt5.QtWidgets import QApplication

import chess
import chess.svg
from IPython.display import SVG
import multiAgents 

board = chess.Board()

multiagent = multiAgents.AlphaBetaAgent()

while (len(board.move_stack) < 30) and not board.is_game_over():
    result = multiagent.getAction(board)
    if board.turn == chess.WHITE:
        print("White plays", result)
    else: 
        print("Black plays", result)
    board.push(result)

# begin GUI instantiation
if __name__ == "__main__":
    app = QApplication(['chess'])
    window = ChessWindow(200)
    window.loadChessBoard(board)
    window.show()
    app.exec()