from gui.ChessWindow import ChessWindow
from PyQt5.QtWidgets import QApplication


import chess
import chess.svg
import argparse
import multiAgents

# begin GUI instantiation
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Show chess GUI with preloaded or live games.')
    parser.add_argument('-p','--pgn',  dest='filepath', 
                        help='Preload pgn file from the given file path.')
    parser.add_argument('-l', dest='live', action='store_true',
                        help='Start live AI vs AI game.')
    parser.add_argument('-m', dest='max_moves', type=int, default=30,
                        help='Maximum number of moves for AI to play against each other.')
    parser.add_argument('-d', dest='depth', type=int, default=2,
                        help='Maximum tree depth for AI algorithm to reach.')
    parser.add_argument('-f', dest='frame_interval', type=int, default=200,
                        help='Set the time between animation frames in ms.')

    args = parser.parse_args()

    app = QApplication(['Chess AI'])
    window = ChessWindow(args.frame_interval)

    # if args.filepath != None:
    #     window.loadPGN(args.filepath)
    # elif args.live:
    #     window.loadAI(multiAgents.AlphaBetaAgent(args.depth), maxMoves=args.max_moves)
    # else:
    #     window.loadPGN('data/Nakamura.pgn')

    print("Starting Test...")
    agent = multiAgents.AlphaBetaAgent()
    score = agent.bratkoKopecTest()
    print("Score: ", score)

    window.show()
    app.exec()
