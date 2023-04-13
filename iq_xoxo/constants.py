from enum import Enum

BOARD_HEIGHT = 5
BOARD_WIDTH = 10


class PuzzlePieceEnum(Enum):
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


NUM_PIECES = len(PuzzlePieceEnum)

PUZZLE_PIECE_NAMES = {
    PuzzlePieceEnum.LINE_PIECE: "LINE_PIECE",
    PuzzlePieceEnum.T_PIECE: "T_PIECE",
    PuzzlePieceEnum.U_PIECE: "U_PIECE",
    PuzzlePieceEnum.L_PIECE: "L_PIECE",
    PuzzlePieceEnum.Z_PIECE: "Z_PIECE",
    PuzzlePieceEnum.P_PIECE: "P_PIECE",
    PuzzlePieceEnum.W_PIECE: "W_PIECE",
    PuzzlePieceEnum.CORNER_PIECE: "CORNER_PIECE",
    PuzzlePieceEnum.POINTING_PIECE: "POINTING_PIECE",
    PuzzlePieceEnum.WAVING_PIECE: "WAVING_PIECE",
}
