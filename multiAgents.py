# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import random, math, chess
import chessUtil
import chess.polyglot

class Agent:
    """
    An agent must define a getAction method, but may also define the
    following methods which will be called if they exist:

    def registerInitialState(self, state): # inspects the starting state
    """

    def __init__(self):
        pass

    def getAction(self, state):
        """
        The Agent will receive a GameState (from either {pacman, capture, sonar}.py) and
        must return an action from Directions.{North, South, East, West, Stop}
        """
        pass


class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxAgent, AlphaBetaAgent.
    """

    def __init__(self, depth = '2'):
        self.depth = int(depth)


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, chessBoard):
        """
        Returns the minimax action from the current chessBoard using self.depth.
        """
        "*** YOUR CODE HERE ***"
        #Definitions 
        alpha = -math.inf
        beta = math.inf
        bestEval = -math.inf
        bestMove = chess.Move.null()

        try:
            move = chess.polyglot.MemoryMappedReader(chessUtil.openingBookPath).weighted_choice(chessBoard).move()
            return move

        except: 
            #Calculate the best move the chess engine should make
            for move in chessBoard.legal_moves:
                chessBoard.push(move)
                eval = -1 * self.negaMax(chessBoard, self.depth, -beta, -alpha)
                if eval > bestEval:
                    bestEval = eval
                    bestMove = move
                if eval > alpha: 
                    alpha = eval
                chessBoard.pop()

            return bestMove


    def negaMax(self, chessBoard, depthRemaining, alpha_prev, beta_prev):
        #Variables 
        alpha = alpha_prev
        beta = beta_prev

        if(depthRemaining == 0):
            #Call Quiescent function
            return self.quiesce(chessBoard, alpha, beta)

        #Recursively search for best score and action! 
        bestEval = -math.inf
        for move in chessBoard.legal_moves:
            chessBoard.push(move)
            nextEval = -1 * self.negaMax(chessBoard, depthRemaining - 1, -beta, -alpha)
            chessBoard.pop()

            if(nextEval >= beta):
                return nextEval
            if(nextEval > bestEval):
                bestEval = nextEval
            if(nextEval > alpha):
                alpha = nextEval
    
        return bestEval

    def evaluationFunction(self, chessBoard):
        """
        The evaluation function takes in the current chessBoard and move and returns an evaluation of the
        resulting position
        """

        evaluation = materialEval(chessBoard)
        evaluation += sum(pieceSquareEval(chessBoard))

        return evaluation

    def quiesce(self, chessBoard, alpha, beta):
        stand_pat = self.evaluationFunction(chessBoard)
        if( stand_pat >= beta ):
            return beta
        if( alpha < stand_pat ):
            alpha = stand_pat

        for move in chessBoard.legal_moves:
            if chessBoard.is_capture(move):
                chessBoard.push(move)        
                score = -1 * self.quiesce(chessBoard, -beta, -alpha)
                chessBoard.pop()

                if( score >= beta ):
                    return beta
                if( score > alpha ):
                    alpha = score  
        return alpha

def materialEval(chessBoard):
    """
    This default evaluation function just returns the score of the board based only on material advantage
    """
    if chessBoard.is_checkmate():
        if chessBoard.turn:
            return -9999
        else:
            return 9999
    if chessBoard.is_stalemate():
        return 0
    if chessBoard.is_insufficient_material():
        return 0
    
    wp = len(chessBoard.pieces(chess.PAWN, chess.WHITE)) 
    bp = len(chessBoard.pieces(chess.PAWN, chess.BLACK))
    wn = len(chessBoard.pieces(chess.KNIGHT, chess.WHITE))
    bn = len(chessBoard.pieces(chess.KNIGHT, chess.BLACK))
    wb = len(chessBoard.pieces(chess.BISHOP, chess.WHITE))
    bb = len(chessBoard.pieces(chess.BISHOP, chess.BLACK))
    wr = len(chessBoard.pieces(chess.ROOK, chess.WHITE))
    br = len(chessBoard.pieces(chess.ROOK, chess.BLACK))
    wq = len(chessBoard.pieces(chess.QUEEN, chess.WHITE))
    bq = len(chessBoard.pieces(chess.QUEEN, chess.BLACK))

    materialEval = 100*(wp-bp) + 320*(wn-bn) + 330*(wb-bb) + 500*(wr-br) + 900*(wq-bq)

    if chessBoard.turn == chess.WHITE:
        return materialEval
    else:
        return -materialEval

def pieceSquareEval(chessBoard):
    """
    This evaluation function returns a score based on where pieces are located. 
    """
    pawnsq = sum([chessUtil.pawntable[i] for i in chessBoard.pieces(chess.PAWN, chess.WHITE)])
    pawnsq= pawnsq + sum([-chessUtil.pawntable[chess.square_mirror(i)] 
                                    for i in chessBoard.pieces(chess.PAWN, chess.BLACK)])
    knightsq = sum([chessUtil.knightstable[i] for i in chessBoard.pieces(chess.KNIGHT, chess.WHITE)])
    knightsq = knightsq + sum([-chessUtil.knightstable[chess.square_mirror(i)] 
                                    for i in chessBoard.pieces(chess.KNIGHT, chess.BLACK)])
    bishopsq= sum([chessUtil.bishopstable[i] for i in chessBoard.pieces(chess.BISHOP, chess.WHITE)])
    bishopsq= bishopsq + sum([-chessUtil.bishopstable[chess.square_mirror(i)] 
                                    for i in chessBoard.pieces(chess.BISHOP, chess.BLACK)])
    rooksq = sum([chessUtil.rookstable[i] for i in chessBoard.pieces(chess.ROOK, chess.WHITE)]) 
    rooksq = rooksq + sum([-chessUtil.rookstable[chess.square_mirror(i)] 
                                    for i in chessBoard.pieces(chess.ROOK, chess.BLACK)])
    queensq = sum([chessUtil.queenstable[i] for i in chessBoard.pieces(chess.QUEEN, chess.WHITE)]) 
    queensq = queensq + sum([-chessUtil.queenstable[chess.square_mirror(i)] 
                                    for i in chessBoard.pieces(chess.QUEEN, chess.BLACK)])
    kingsq = sum([chessUtil.kingstable[i] for i in chessBoard.pieces(chess.KING, chess.WHITE)]) 
    kingsq = kingsq + sum([-chessUtil.kingstable[chess.square_mirror(i)] 
                                    for i in chessBoard.pieces(chess.KING, chess.BLACK)])

    return [pawnsq, knightsq, bishopsq, rooksq, queensq, kingsq]