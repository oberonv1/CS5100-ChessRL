import chess

openingBookPath = (r"C:/Users/xephy/OneDrive/Documents/Education/Classes/Northeastern/CS 5100/"
                   r"Final Project/CS5100-ChessRL/data/the-generated-opening-book.bin")

pieceValue = {
  chess.PAWN  : 1,
  chess.KNIGHT: 3,
  chess.BISHOP: 3.5,
  chess.ROOK: 5,
  chess.QUEEN: 9,
  chess.KING: 50
}

pawntable = [
 0,  0,  0,  0,  0,  0,  0,  0,
 5, 10, 10,-20,-20, 10, 10,  5,
 5, -5,-10,  0,  0,-10, -5,  5,
 0,  0,  0, 20, 20,  0,  0,  0,
 5,  5, 10, 25, 25, 10,  5,  5,
10, 10, 20, 30, 30, 20, 10, 10,
50, 50, 50, 50, 50, 50, 50, 50,
 0,  0,  0,  0,  0,  0,  0,  0]

knightstable = [
-50,-40,-30,-30,-30,-30,-40,-50,
-40,-20,  0,  5,  5,  0,-20,-40,
-30,  5, 10, 15, 15, 10,  5,-30,
-30,  0, 15, 20, 20, 15,  0,-30,
-30,  5, 15, 20, 20, 15,  5,-30,
-30,  0, 10, 15, 15, 10,  0,-30,
-40,-20,  0,  0,  0,  0,-20,-40,
-50,-40,-30,-30,-30,-30,-40,-50]

bishopstable = [
-20,-10,-10,-10,-10,-10,-10,-20,
-10,  5,  0,  0,  0,  0,  5,-10,
-10, 10, 10, 10, 10, 10, 10,-10,
-10,  0, 10, 10, 10, 10,  0,-10,
-10,  5,  5, 10, 10,  5,  5,-10,
-10,  0,  5, 10, 10,  5,  0,-10,
-10,  0,  0,  0,  0,  0,  0,-10,
-20,-10,-10,-10,-10,-10,-10,-20]

rookstable = [
  0,  0,  0,  5,  5,  0,  0,  0,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
  5, 10, 10, 10, 10, 10, 10,  5,
 0,  0,  0,  0,  0,  0,  0,  0]

queenstable = [
-20,-10,-10, -5, -5,-10,-10,-20,
-10,  0,  0,  0,  0,  0,  0,-10,
-10,  5,  5,  5,  5,  5,  0,-10,
  0,  0,  5,  5,  5,  5,  0, -5,
 -5,  0,  5,  5,  5,  5,  0, -5,
-10,  0,  5,  5,  5,  5,  0,-10,
-10,  0,  0,  0,  0,  0,  0,-10,
-20,-10,-10, -5, -5,-10,-10,-20]

kingstable = [
 20, 30, 10,  0,  0, 10, 30, 20,
 20, 20,  0,  0,  0,  0, 20, 20,
-10,-20,-20,-20,-20,-20,-20,-10,
-20,-30,-30,-40,-40,-30,-30,-20,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30]

pieceTables = {
  chess.PAWN  : pawntable,
  chess.KNIGHT: knightstable,
  chess.BISHOP: bishopstable,
  chess.ROOK: rookstable,
  chess.QUEEN: queenstable,
  chess.KING: kingstable
}

eloTestPositions = [
  "r1b3k1/6p1/P1n1pr1p/q1p5/1b1P4/2N2N2/PP1QBPPP/R3K2R b - - 0 1",
  "2nq1nk1/5p1p/4p1pQ/pb1pP1NP/1p1P2P1/1P4N1/P4PB1/6K1 w - - 0 1",
  "8/3r2p1/pp1Bp1p1/1kP5/1n2K3/6R1/1P3P2/8 w - - 0 1",
  "8/4kb1p/2p3pP/1pP1P1P1/1P3K2/1B6/8/8 w - - 0 1",
  "b1R2nk1/5ppp/1p3n2/5N2/1b2p3/1P2BP2/q3BQPP/6K1 w - - 0 1",
  "3rr1k1/pp3pbp/2bp1np1/q3p1B1/2B1P3/2N4P/PPPQ1PP1/3RR1K1 w - - 0 1",
  "r1b1qrk1/1ppn1pb1/p2p1npp/3Pp3/2P1P2B/2N5/PP1NBPPP/R2Q1RK1 b - - 0 1",
  "2R1r3/5k2/pBP1n2p/6p1/8/5P1P/2P3P1/7K w - - 0 1",
  "2r2rk1/1p1R1pp1/p3p2p/8/4B3/3QB1P1/q1P3KP/8 w - - 0 1",
  "r1bq1rk1/p4ppp/1pnp1n2/2p5/2PPpP2/1NP1P3/P3B1PP/R1BQ1RK1 b - - 0 1"
]

eloMeterPositions = [
  "1rb1k2r/2p2ppp/2p5/4p3/2P1n1q1/3Q4/PPPB2PP/2KR2NR w k - 0 1",
  "5q2/1p2k3/p2p4/5bp1/1B6/P2P1P2/2K3P1/1Q6 w - - 0 1",
  "8/R7/1p2k3/2p1q1p1/2P1Q3/1P2K1P1/7r/8 w - - 0 1",
  "8/8/8/6p1/5kP1/7K/8/8 w - - 0 1",
  "r3q2k/5Q1p/1pb2bp1/5p2/2B5/PP3N2/K1P3P1/8 w - - 0 1",
  "1b3rk1/2q3p1/p7/2p3N1/2p4P/2P3n1/1PQ3P1/4R1K1 w - - 0 1",
  "7k/q5pp/1P6/8/8/8/6PP/7K w - - 0 1",
  "5rk1/2b2ppp/pp3n2/2p1p1B1/4P3/2NP4/PPP2PPP/5RK1 w - - 0 1",
  "8/8/8/1Pk5/8/8/2P3K1/8 w - - 0 1",
  "r3k2r/5ppp/p3p3/1p1p4/1PpP4/2P1P3/P3KPPP/RR6 w kq - 0 1",
  "3R1rk1/p5pp/1p1Q4/5qP1/4Nn2/1P6/P5PP/7K w - - 0 1",
  "rr3b1k/2p2p2/b4N1p/q3p3/2P5/8/PP3P2/KN1R2R1 w - - 0 1",
  "8/1q4k1/8/8/8/6K1/8/1R6 w - - 0 1",
  "8/8/8/5K2/8/4R3/p2k4/8 w - - 0 1",
  "k7/8/3r4/8/4N3/5K2/5P2/8 w - - 0 1",
  "2r3r1/4Nppk/5b2/qppP4/8/1P3P2/P1P3P1/1K1RR3 w - - 0 1",
  "8/2P5/3K4/5b2/1p6/6k1/8/8 w - - 0 1",
  "7k/1K6/8/4q3/8/2B5/2P5/8 w - - 0 1",
  "1r2r3/p1q2p1k/R5p1/3p3b/7Q/1P4R1/3B1PPP/6K1 w - - 0 1",
  "r2qr2k/6pp/pp1p4/3Pn1N1/8/1P4P1/P2Q3P/R3R1K1 w - - 0 1",
  "3r1r1k/p3bpR1/1p1p1n1p/4pP1q/2N1P3/1P2BPQP/P4K2/6R1 w - - 0 1",
  "2r3k1/1ppq1pp1/p1n2n1p/8/3P4/1PBQ1N1P/P4PP1/3R2K1 w - - 0 1",
  "4br2/p1q1p1k1/4Q1p1/1pN2n2/1P1b4/8/P3B1PP/4BR1K w - - 0 1",
  "R7/5qpk/1p6/2p1rb1p/2Q5/2P3P1/1P3P1P/7K w - - 0 1",
  "r2q1rk1/1ppn1ppp/p2np3/3p4/B2P4/2P1PN2/P1P1QPPP/R4RK1 w - - 0 1",
  "6r1/pkpq3p/6p1/2P5/2NPnP2/1P5R/7K/3Q4 w - - 0 1",
  "r2qk2r/ppp2ppp/1n1p1nb1/8/2PP4/2NB2P1/PP3PP1/R1BQ1RK1 w kq - 0 1",
  "2b5/ppp1k1pp/2n1p3/1BNp1p2/3P3P/PP2P1P1/1P1K1P2/8 w - - 0 1",
  "1r3rk1/5ppp/8/1pbN3Q/2p1P3/2Bn1P2/1P3qPP/RR5K w - - 0 1",
  "r4rk1/2qnppb1/4p1p1/4P1N1/1p1P1P2/1P6/1KP1N3/3R2QR w - - 0 1",
  "8/8/3p4/2k5/4P3/8/8/1K6 w - - 0 1",
  "8/p7/8/PP1k4/1K6/8/8/8 w - - 0 1",
  "7R/8/8/8/3kp3/8/r7/4K3 w - - 0 1",
  "8/8/5k2/8/p7/8/1PK5/8 w - - 0 1",
  "3B2k1/1b3p1p/p5p1/1p5q/3Q4/1P3P2/P1r3PP/3R2K1 w - - 0 1",
  "3k1r2/4R3/2pB4/pqP2b1p/3P4/2Pp2P1/8/2K1Q3 w - - 0 1",
  "r3r1k1/4b1pp/3p3P/6P1/2p1b1q1/4B3/PP1Q2B1/K5RR w - - 0 1",
  "4r1k1/p4p1p/1p3qpB/3b4/1P1R4/P1Q5/5PPP/6K1 w - - 0 1",
  "8/p7/Pp1kB3/1Ppn2K1/2P5/8/8/8 w - - 0 1",
  "8/8/2N5/8/8/4k3/p6K/8 w - - 0 1",
  "rr4k1/R1Q2ppp/4pq2/8/7n/3P4/2P2NPP/5R1K w - - 0 1",
  "rr3nk1/6q1/2p1pRP1/3pP1Qp/6p1/2P3P1/N6P/K1R5 w - - 0 1",
  "r2qr1k1/1bpn1p1p/1p3bp1/p3p3/P1P5/4PN1P/1PQ1BPPB/R2R2K1 w - - 0 1",
  "8/6P1/5K1r/8/8/8/8/3k4 w - - 0 1",
  "3rkn2/1Q2b2p/2p1p3/p2q4/n3NP2/2P1K1R1/P2B3P/2N5 w - - 0 1",
  "r4r1k/1p1bbppp/1qp1pn2/4B3/3P3P/1P1B1QR1/P3NPP1/1K1R4 w - - 0 1",
  "r2qrnk1/pp2bppp/2p1bn2/3p2B1/3P4/2NBPN2/PPQ2PPP/1R3RK1 w - - 0 1",
  "r3kb1r/pp4p1/2p1p1p1/4p3/8/2PqPQ1P/PP1N2P1/1R2K2R w Kkq - 0 1",
  "3kN2b/2p4P/2p2p2/2P2P1K/8/8/8/8 w - - 0 1",
  "r4r2/2k2qpp/pRbbR3/P2p1P2/P1pP2P1/2B2Q2/2B5/6K1 w - - 0 1",
  "r2q1rk1/pbp1bppp/1p2pn2/6B1/3P4/3B1N2/PPP1QPPP/R4RK1 w - - 0 1",
  "r1bqk2r/pp1n1ppp/2p2n2/3p4/P2Pp3/2P1P3/2PN1PPP/R1BQKB1R w KQkq - 0 1",
  "5rk1/R6p/3pp3/2p1n2r/2q5/2B5/1PQ2PPP/5RK1 w - - 0 1",
  "rn2k2r/1bQ1qpp1/p3p3/2bp4/P2N3p/2PB4/1P3PPP/R1B1R1K1 w kq - 0 1",
  "5N2/4P3/7k/6r1/8/8/8/4K3 w - - 0 1",
  "rr4k1/1q3ppp/1bQRp3/6P1/4P3/P4N2/1P6/K3R3 w - - 0 1",
  "8/8/5p2/5p2/5P2/3p3B/5k1P/3K4 w - - 0 1",
  "r2k3r/pp3pb1/3p3p/1BpP2p1/Q7/P1P2q2/1P3P2/R3R1K1 w - - 0 1",
  "8/8/8/4p1p1/8/5P2/6K1/3k4 w - - 0 1",
  "4r2k/5Qpp/8/2N5/3n2p1/8/2P3PP/4qR1K w - - 0 1",
  "2r2rk1/1R3pp1/n3pP1n/q2p4/p2P1NP1/R2Q1P1p/2N4P/6K1 w - - 0 1",
  "r6k/1p4pp/p2q4/1r3P2/2npQ2P/6P1/R1PB1P2/2K1R3 w - - 0 1",
  "8/8/8/8/3p1B2/4p3/5p2/5K1k w - - 0 1",
  "rn2k2r/p4pp1/1p2p2p/1P1pPn1P/2qP4/5N2/2PB1PP1/RQ2K2R w KQkq - 0 1",
  "6k1/p1P5/P1r5/2p1K3/8/8/2R5/8 w - - 0 1",
  "r4rk1/pb1qn1pp/1pnNp3/3pPp2/PP1P1P2/5N2/3Q2PP/R3KB1R w KQ - 0 1",
  "2k4r/p1b2p2/Pp1r1q1p/1Pp1p3/4P1pP/2P1R1P1/5PB1/1RQ3K1 w - - 0 1",
  "r3k1nr/pp1nq1p1/1bp1b2p/3pPp2/3P1B2/2PB1N2/PP1NQ1PP/R3K2R w KQkq - 0 1",
  "4k2r/1p3ppp/p1n5/2r1p3/4P3/2N5/PP2KPPP/2RR4 w k - 0 1",
  "3rr1k1/3nbppp/p1R2n2/qp1Bp1B1/4P3/5N1P/PP3PP1/2RQ2K1 w - - 0 1",
  "r1bq1rk1/ppp2pp1/2np1n1p/3Np1NQ/7P/1B1P4/PPP2PP1/2KR3R w - - 0 1",
  "r4r2/6kp/2pqppp1/pbR5/3P4/4QN2/PP3PPP/2R3K1 w - - 0 1",
  "rnbq1rk1/ppp4p/3p2p1/3Pp2n/2P1Pp1b/2N2P2/PP1QNBPP/2KR1B1R w - - 0 1",
  "4r1k1/1b4pp/p1p1r3/2Pp1qb1/PP2p3/2N3B1/4RPPP/3RQ1K1 w - - 0 1",
  "2r5/pp2kp2/3q1p1Q/3Pp3/6b1/1B6/P1P3PP/1K3R2 w - - 0 1",
  "r4r2/pppqbpk1/2n1b2p/4p1p1/3pP3/3P2PP/PPPN1PBK/R2Q1RN1 w - - 0 1"
]


bratkoKopecPositions = [
"1k1r4/pp1b1R2/3q2pp/4p3/2B5/4Q3/PPP2B2/2K5 b - - 0 1",
"3r1k2/4npp1/1ppr3p/p6P/P2PPPP1/1NR5/5K2/2R5 w - - 0 1",
"2q1rr1k/3bbnnp/p2p1pp1/2pPp3/PpP1P1P1/1P2BNNP/2BQ1PRK/7R b - - 0 1",
"rnbqkb1r/p3pppp/1p6/2ppP3/3N4/2P5/PPP1QPPP/R1B1KB1R w KQkq - 0 1",
"r1b2rk1/2q1b1pp/p2ppn2/1p6/3QP3/1BN1B3/PPP3PP/R4RK1 w - - 0 1",
"2r3k1/pppR1pp1/4p3/4P1P1/5P2/1P4K1/P1P5/8 w - - 0 1",
"1nk1r1r1/pp2n1pp/4p3/q2pPp1N/b1pP1P2/B1P2R2/2P1B1PP/R2Q2K1 w - - 0 1",
"4b3/p3kp2/6p1/3pP2p/2pP1P2/4K1P1/P3N2P/8 w - - 0 1",
"2kr1bnr/pbpq4/2n1pp2/3p3p/3P1P1B/2N2N1Q/PPP3PP/2KR1B1R w - - 0 1",
"3rr1k1/pp3pp1/1qn2np1/8/3p4/PP1R1P2/2P1NQPP/R1B3K1 b - - 0 1",
"2r1nrk1/p2q1ppp/bp1p4/n1pPp3/P1P1P3/2PBB1N1/4QPPP/R4RK1 w - - 0 1",
"r3r1k1/ppqb1ppp/8/4p1NQ/8/2P5/PP3PPP/R3R1K1 b - - 0 1",
"r2q1rk1/4bppp/p2p4/2pP4/3pP3/3Q4/PP1B1PPP/R3R1K1 w - - 0 1",
"rnb2r1k/pp2p2p/2pp2p1/q2P1p2/8/1Pb2NP1/PB2PPBP/R2Q1RK1 w - - 0 1",
"2r3k1/1p2q1pp/2b1pr2/p1pp4/6Q1/1P1PP1R1/P1PN2PP/5RK1 w - - 0 1",
"r1bqkb1r/4npp1/p1p4p/1p1pP1B1/8/1B6/PPPN1PPP/R2Q1RK1 w kq - 0 1",
"r2q1rk1/1ppnbppp/p2p1nb1/3Pp3/2P1P1P1/2N2N1P/PPB1QP2/R1B2RK1 b - - 0 1",
"r1bq1rk1/pp2ppbp/2np2p1/2n5/P3PP2/N1P2N2/1PB3PP/R1B1QRK1 b - - 0 1",
"3rr3/2pq2pk/p2p1pnp/8/2QBPP2/1P6/P5PP/4RRK1 b - - 0 1",
"r4k2/pb2bp1r/1p1qp2p/3pNp2/3P1P2/2N3P1/PPP1Q2P/2KRR3 w - - 0 1",
"3rn2k/ppb2rpp/2ppqp2/5N2/2P1P3/1P5Q/PB3PPP/3RR1K1 w - - 0 1",
"2r2rk1/1bqnbpp1/1p1ppn1p/pP6/N1P1P3/P2B1N1P/1B2QPP1/R2R2K1 b - - 0 1",
"r1bqk2r/pp2bppp/2p5/3pP3/P2Q1P2/2N1B3/1PP3PP/R4RK1 b kq - 0 1",
"r2qnrnk/p2b2b1/1p1p2pp/2pPpp2/1PP1P3/PRNBB3/3QNPPP/5RK1 w - - 0 1",
]
bratkoKopecSolutions = ["Qd1+","d5","f5","e6","a4","g6","Nf6","f5","f5","Ne5","f4","Bf5","b4",
             "Qd2 Qe1","Qxg7+","Ne4","h5","Nb3","Rxe4","g4","Nh6","Bxe4","f6","f4"]