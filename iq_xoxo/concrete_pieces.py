from iq_xoxo.constants import PuzzlePieceEnum

from iq_xoxo.puzzle_piece import PuzzlePiece

line_piece_art = ["XOXOX"]
LINE_PIECE = PuzzlePiece.from_ascii(PuzzlePieceEnum.LINE_PIECE, line_piece_art)

t_piece_art = ["XOX", ".X.", ".O."]
T_PIECE = PuzzlePiece.from_ascii(PuzzlePieceEnum.T_PIECE, t_piece_art)

u_piece_art = ["X.X", "OXO"]
U_PIECE = PuzzlePiece.from_ascii(PuzzlePieceEnum.U_PIECE, u_piece_art)

l_piece_art = [
    "X.",
    "O.",
    "X.",
    "OX",
]
L_PIECE = PuzzlePiece.from_ascii(PuzzlePieceEnum.L_PIECE, l_piece_art)

z_piece_art = [
    ".XO",
    ".O",
    "OX",
]
Z_PIECE = PuzzlePiece.from_ascii(PuzzlePieceEnum.Z_PIECE, z_piece_art)

p_piece_art = ["XO", "OX", "X."]
P_PIECE = PuzzlePiece.from_ascii(PuzzlePieceEnum.P_PIECE, p_piece_art)

w_piece_art = ["X..", "OX.", ".OX,"]
W_PIECE = PuzzlePiece.from_ascii(PuzzlePieceEnum.W_PIECE, w_piece_art)

corner_piece_art = ["X..", "O..", "XOX"]
CORNER_PIECE = PuzzlePiece.from_ascii(PuzzlePieceEnum.CORNER_PIECE, corner_piece_art)

pointing_piece_art = ["X.", "OX", "X.", "O."]
POINTING_PIECE = PuzzlePiece.from_ascii(
    PuzzlePieceEnum.POINTING_PIECE, pointing_piece_art
)

waving_piece_art = [".O", "OX", "X.", "O."]
WAVING_PIECE = PuzzlePiece.from_ascii(PuzzlePieceEnum.WAVING_PIECE, waving_piece_art)

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
