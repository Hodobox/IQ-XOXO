from enum import Enum
from typing import Dict, List

BOARD_HEIGHT = 5
BOARD_WIDTH = 10
NUM_BITS = BOARD_HEIGHT * BOARD_WIDTH
BITMASK_FINISHED = (1 << (NUM_BITS)) - 1


class PuzzlePieceType(Enum):
    LINE_PIECE = 0
    T_PIECE = 1
    U_PIECE = 2
    L_PIECE = 3
    Z_PIECE = 4
    P_PIECE = 5
    W_PIECE = 6
    CORNER_PIECE = 7
    POINTING_PIECE = 8
    WAVING_PIECE = 9


NUM_PIECES = len(PuzzlePieceType)
SQUARES_PER_PIECE = 5

PUZZLE_PIECE_NAMES = {
    PuzzlePieceType.LINE_PIECE: "LINE_PIECE",
    PuzzlePieceType.T_PIECE: "T_PIECE",
    PuzzlePieceType.U_PIECE: "U_PIECE",
    PuzzlePieceType.L_PIECE: "L_PIECE",
    PuzzlePieceType.Z_PIECE: "Z_PIECE",
    PuzzlePieceType.P_PIECE: "P_PIECE",
    PuzzlePieceType.W_PIECE: "W_PIECE",
    PuzzlePieceType.CORNER_PIECE: "CORNER_PIECE",
    PuzzlePieceType.POINTING_PIECE: "POINTING_PIECE",
    PuzzlePieceType.WAVING_PIECE: "WAVING_PIECE",
}


LINE_PIECE_ART = ["XOXOX"]
T_PIECE_ART = ["XOX", ".X.", ".O."]
U_PIECE_ART = ["X.X", "OXO"]
L_PIECE_ART = [
    "X.",
    "O.",
    "X.",
    "OX",
]
Z_PIECE_ART = [
    ".XO",
    ".O",
    "OX",
]
P_PIECE_ART = ["XO", "OX", "X."]
W_PIECE_ART = ["X..", "OX.", ".OX,"]
CORNER_PIECE_ART = ["X..", "O..", "XOX"]
POINTING_PIECE_ART = ["X.", "OX", "X.", "O."]
WAVING_PIECE_ART = [".O", "OX", "X.", "O."]

PUZZLE_PIECE_ARTS: Dict[PuzzlePieceType, List[str]] = {
    PuzzlePieceType.LINE_PIECE: LINE_PIECE_ART,
    PuzzlePieceType.T_PIECE: T_PIECE_ART,
    PuzzlePieceType.U_PIECE: U_PIECE_ART,
    PuzzlePieceType.L_PIECE: L_PIECE_ART,
    PuzzlePieceType.Z_PIECE: Z_PIECE_ART,
    PuzzlePieceType.P_PIECE: P_PIECE_ART,
    PuzzlePieceType.W_PIECE: W_PIECE_ART,
    PuzzlePieceType.CORNER_PIECE: CORNER_PIECE_ART,
    PuzzlePieceType.POINTING_PIECE: POINTING_PIECE_ART,
    PuzzlePieceType.WAVING_PIECE: WAVING_PIECE_ART,
}
assert len(PUZZLE_PIECE_ARTS) == 10
