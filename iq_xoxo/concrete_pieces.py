from enum import Enum
from typing import Dict, List, Tuple

from iq_xoxo.puzzle_piece import PuzzlePiece, PuzzlePieceSquare


class PuzzlePieceNames(str, Enum):
    LINE_PIECE = "LINE_PIECE"
    T_PIECE = "T_PIECE"
    U_PIECE = "U_PIECE"
    L_PIECE = "L_PIECE"
    Z_PIECE = "Z_PIECE"
    P_PIECE = "P_PIECE"
    W_PIECE = "W_PIECE"
    CORNER_PIECE = "CORNER_PIECE"
    POINTING_PIECE = "POINTING_PIECE"
    WAVING_PIECE = "WAVING_PIECE"


line_piece_art = ["XOXOX"]
LINE_PIECE = PuzzlePiece.from_ascii(PuzzlePieceNames.LINE_PIECE, line_piece_art)

t_piece_art = ["XOX", ".X.", ".O."]
T_PIECE = PuzzlePiece.from_ascii(PuzzlePieceNames.T_PIECE, t_piece_art)

u_piece_art = ["X.X", "OXO"]
U_PIECE = PuzzlePiece.from_ascii(PuzzlePieceNames.U_PIECE, u_piece_art)

l_piece_art = [
    "X.",
    "O.",
    "X.",
    "OX",
]
L_PIECE = PuzzlePiece.from_ascii(PuzzlePieceNames.L_PIECE, l_piece_art)

z_piece_art = [
    ".XO",
    ".O",
    "OX",
]
Z_PIECE = PuzzlePiece.from_ascii(PuzzlePieceNames.Z_PIECE, z_piece_art)

p_piece_art = ["XO", "OX", "X."]
P_PIECE = PuzzlePiece.from_ascii(PuzzlePieceNames.P_PIECE, p_piece_art)

w_piece_art = ["X..", "OX.", ".OX,"]
W_PIECE = PuzzlePiece.from_ascii(PuzzlePieceNames.W_PIECE, w_piece_art)

corner_piece_art = ["X..", "O..", "XOX"]
CORNER_PIECE = PuzzlePiece.from_ascii(PuzzlePieceNames.CORNER_PIECE, corner_piece_art)

pointing_piece_art = ["X.", "OX", "X.", "O."]
POINTING_PIECE = PuzzlePiece.from_ascii(
    PuzzlePieceNames.POINTING_PIECE, pointing_piece_art
)

waving_piece_art = [".O", "OX", "X.", "O."]
WAVING_PIECE = PuzzlePiece.from_ascii(PuzzlePieceNames.WAVING_PIECE, waving_piece_art)

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

VARIATIONS: Dict[str, List[PuzzlePiece]] = {
    piece.name: piece.get_variations() for piece in PUZZLE_PIECES
}
