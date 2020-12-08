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


class AlphaBetaAgent():
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def __init__(self, depth = '3'):
        self.depth = int(depth)

        """
        Dictionary of moves
        Keys are (Board Fen, and Turn)
        Stored values are depth and best move result. 
        """
        self.transpositionTable = {}
        self.eval = 0

    def getMove(self, chessBoard):
        """
        Returns the minimax action from the current chessBoard using self.depth.
        """
        "*** YOUR CODE HERE ***"
        #Definitions 
        alpha = -math.inf
        beta = math.inf
        bestEval = -math.inf
        bestMove = chess.Move.null()
        self.initEvaluation(chessBoard)

        try:
            move = chess.polyglot.MemoryMappedReader(chessUtil.openingBookPath).weighted_choice(chessBoard).move()
            return move

        except: 
            #Calculate the best move the chess engine should make
            depth = self.depth
           
           #Check the transposition table
            key = (chessBoard.board_fen(), chessBoard.turn)
            if key in self.transpositionTable.keys():
                potentialMove = self.transpositionTable[key]

                #Check to ensure you aren't returning a move with lower search depth
                if depth <= potentialMove[1]:
                    return self.transpositionTable[key][0]

            for move in getMoveOrdering(chessBoard):
                self.pushMove(chessBoard, move)
                eval = -1 * self.negaMax(chessBoard, depth, -beta, -alpha)
                if eval > bestEval:
                    bestEval = eval
                    bestMove = move
                if eval > alpha: 
                    alpha = eval
                self.popMove(chessBoard)

            self.transpositionTable[key] = (bestMove, depth)
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
        for move in getMoveOrdering(chessBoard):
            self.pushMove(chessBoard, move)
            nextEval = -1 * self.negaMax(chessBoard, depthRemaining - 1, -beta, -alpha)
            self.popMove(chessBoard)

            if(nextEval >= beta):
                return nextEval
            if(nextEval > bestEval):
                bestEval = nextEval
            if(nextEval > alpha):
                alpha = nextEval
    
        return bestEval

    def initEvaluation(self, chessBoard):
        """
        The evaluation function takes in the current chessBoard and move and returns an evaluation of the
        resulting position
        """

        evaluation = materialEval(chessBoard)
        evaluation += sum(pieceSquareEval(chessBoard))

        self.eval = evaluation

    def quickEval(self, chessBoard):
        evaluation = self.eval

        if chessBoard.is_checkmate():
            if chessBoard.turn:
                return -9999
            else:
                return 9999
        if chessBoard.is_stalemate():
            return 0
        if chessBoard.is_insufficient_material():
            return 0

        if chessBoard.turn:
            return evaluation
        else: 
            return -evaluation

    def incrementalEval(self, chessBoard, move, turn):
        #update piecequares
        movingPiece = chessBoard.piece_type_at(move.from_square)

        if turn:
            pieceSquareDiff = chessUtil.pieceTables[movingPiece][move.to_square] - \
                              chessUtil.pieceTables[movingPiece][move.from_square] 
            self.eval = self.eval + pieceSquareDiff
            #update castling
            if (move.from_square == chess.E1) and (move.to_square == chess.G1):
                self.eval = self.eval - chessUtil.rookstable[chess.H1]
                self.eval = self.eval + chessUtil.rookstable[chess.F1]
            elif (move.from_square == chess.E1) and (move.to_square == chess.C1):
                self.eval = self.eval - chessUtil.rookstable[chess.A1]
                self.eval = self.eval + chessUtil.rookstable[chess.D1]
        else:
            pieceSquareDiff = chessUtil.pieceTables[movingPiece][move.to_square] - \
                              chessUtil.pieceTables[movingPiece][move.from_square] 
            self.eval = self.eval - pieceSquareDiff
            #update castling
            if (move.from_square == chess.E8) and (move.to_square == chess.G8):
                self.eval = self.eval + chessUtil.rookstable[chess.H8]
                self.eval = self.eval - chessUtil.rookstable[chess.F8]
            elif (move.from_square == chess.E8) and (move.to_square == chess.C8):
                self.eval = self.eval + chessUtil.rookstable[chess.A8]
                self.eval = self.eval - chessUtil.rookstable[chess.D8]            
        
        #update material
        if move.drop != None:
            if turn:
                self.eval = self.eval + chessUtil.pieceValue[move.drop]
            else:
                self.eval = self.eval - chessUtil.pieceValue[move.drop]
                
        #update promotion
        if move.promotion != None:
            if turn:
                self.eval = self.eval + chessUtil.pieceValue[move.promotion]\
                                      - chessUtil.pieceValue[movingPiece]
                self.eval = self.eval - chessUtil.pieceTables[movingPiece][move.to_square]\
                                      + chessUtil.pieceTables[move.promotion][move.to_square]
            else:
                self.eval = self.eval - chessUtil.pieceValue[move.promotion]\
                                      + chessUtil.pieceValue[movingPiece]
                self.eval = self.eval + chessUtil.pieceTables[movingPiece][move.to_square]\
                                      - chessUtil.pieceTables[move.promotion][move.to_square]
                
    def pushMove(self, chessBoard, move):
        self.incrementalEval(chessBoard, move, chessBoard.turn)
        chessBoard.push(move)

    def popMove(self, chessBoard):
        move = chessBoard.pop()
        self.incrementalEval(chessBoard, move, ~chessBoard.turn)

        return move


    def quiesce(self, chessBoard, alpha, beta):
        stand_pat = self.quickEval(chessBoard)
        if( stand_pat >= beta ):
            return beta
        if( alpha < stand_pat ):
            alpha = stand_pat

        for move in getMoveOrdering(chessBoard):
            if chessBoard.is_capture(move):
                self.pushMove(chessBoard, move)   
                score = -1 * self.quiesce(chessBoard, -beta, -alpha)
                self.popMove(chessBoard)

                if( score >= beta ):
                    return beta
                if( score > alpha ):
                    alpha = score  
        return alpha


    def eloTest(self):
        results = []
        for position in chessUtil.eloTestPositions:
            chessBoard = chess.Board(position)
            results.append(self.getMove(chessBoard))
        
        return results

    def bratkoKopecTest(self):
        score = 0
        for position, solution in zip(chessUtil.bratkoKopecPositions, chessUtil.bratkoKopecSolutions):
            print("\nPosition:", position)
            chessBoard = chess.Board(position)
            move = self.getMove(chessBoard)
            moveNotation = chessBoard.san(move)
            print("Move: ", moveNotation)
            print("Solution: ", solution)
            if moveNotation == solution:
                score += 1
        
        return score

def getMoveOrdering(chessBoard):
    """
    This function returns to you a sorted list of legal moves by the following priorities: 
    
    Retakes - +100
    Checks - +20 - ez
    Captures - +10 - ez
    Attacks - Valdiff (2x for pin)
    Defensive considerations 
    """
    movelist =[]
    moveScores = {}

    for move in chessBoard.legal_moves:
        movelist.append(move)
        score = 0
        #Consider Square Defense 
        attDefDif = 0
        #Defenders
        for defenders in chessBoard.attackers(chessBoard.turn, move.to_square):
            if chessBoard.piece_type_at(defenders) != None:
                attDefDif += chessUtil.pieceValue[chessBoard.piece_type_at(defenders)]
        #Attackers
        for attackers in chessBoard.attackers(~chessBoard.turn, move.to_square):
            if chessBoard.piece_type_at(attackers) != None:
                attDefDif -= chessUtil.pieceValue[chessBoard.piece_type_at(attackers)]
        score += attDefDif 

        #Consider Checks 
        if chessBoard.gives_check(move):
            score += 20

        #Consider Captures 
        if chessBoard.is_capture(move):
            score += 10

        #Consider Pins and Attacks 
        attackerVal = chessUtil.pieceValue[chessBoard.piece_type_at(move.from_square)]
        chessBoard.push(move)
        for attackedSquare in chessBoard.attacks(move.to_square):
            if chessBoard.color_at(attackedSquare) == ~chessBoard.turn:
                attackedVal = chessUtil.pieceValue[chessBoard.piece_type_at(attackedSquare)]
                if chessBoard.is_pinned(~chessBoard.turn, attackedSquare):    
                    score += 2 * (attackedVal - attackerVal)
                else:
                    score += attackedVal - attackerVal
        chessBoard.pop()

        moveScores[move] = score

    #Sort Move Scores by score and return sorted list
    orderedMoves = dict(sorted(moveScores.items(), key=lambda item: item[1], reverse = True))
    
    return list(orderedMoves.keys())


def materialEval(chessBoard):
    """
    This default evaluation function just returns the score of the board based only on material advantage
    """    
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

    return materialEval

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