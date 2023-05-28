from iq_xoxo.constants import (CORNER_PIECE_ART, L_PIECE_ART, LINE_PIECE_ART,
                               P_PIECE_ART, POINTING_PIECE_ART, T_PIECE_ART,
                               U_PIECE_ART, W_PIECE_ART, WAVING_PIECE_ART,
                               Z_PIECE_ART)
from iq_xoxo.puzzle_piece import PuzzlePiece

LINE_PIECE = PuzzlePiece.from_ascii(LINE_PIECE_ART)
T_PIECE = PuzzlePiece.from_ascii(T_PIECE_ART)
U_PIECE = PuzzlePiece.from_ascii(U_PIECE_ART)
L_PIECE = PuzzlePiece.from_ascii(L_PIECE_ART)
Z_PIECE = PuzzlePiece.from_ascii(Z_PIECE_ART)
P_PIECE = PuzzlePiece.from_ascii(P_PIECE_ART)
W_PIECE = PuzzlePiece.from_ascii(W_PIECE_ART)
CORNER_PIECE = PuzzlePiece.from_ascii(CORNER_PIECE_ART)
POINTING_PIECE = PuzzlePiece.from_ascii(POINTING_PIECE_ART)
WAVING_PIECE = PuzzlePiece.from_ascii(WAVING_PIECE_ART)

PUZZLE_PIECES = [
    LINE_PIECE,
    T_PIECE,
    U_PIECE,
    L_PIECE,
    Z_PIECE,
    P_PIECE,
    W_PIECE,
    CORNER_PIECE,
    POINTING_PIECE,
    WAVING_PIECE,
]
assert len(PUZZLE_PIECES) == 10
