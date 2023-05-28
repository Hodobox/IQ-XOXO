from functools import reduce
from typing import Dict, List

from iq_xoxo.constants import BOARD_HEIGHT, BOARD_WIDTH, PUZZLE_PIECE_CHARS
from iq_xoxo.puzzle_piece import (PuzzlePiece, PuzzlePieceSquare,
                                  squares_to_bitmask)


class Board:
    def __init__(self, pieces: List[PuzzlePiece] = []):
        types = [p.type for p in pieces]
        assert len(pieces) == len(types)

        masks = [p.to_bitmask() for p in pieces]
        assert sum(masks) == reduce(lambda m, a: m | a, masks, 0)

        self.mask = sum(masks)
        self.masks = masks
        self.pieces_used = types

    @classmethod
    def from_ascii(cls, ascii: List[str]) -> "Board":
        if len(ascii) != BOARD_HEIGHT:
            raise ValueError(
                f"Board must have {BOARD_HEIGHT} rows, input has {len(ascii)}"
            )

        same_char: Dict[str, List[PuzzlePieceSquare]] = {}

        for y, row in enumerate(ascii[::-1]):
            if len(row) != BOARD_WIDTH:
                raise ValueError(
                    f"Board must have {BOARD_WIDTH} columns, a row in the input has {len(row)}"
                )

            for x, c in enumerate(row):
                if c not in same_char:
                    same_char[c] = []

                same_char[c].append(
                    PuzzlePieceSquare(x, y, True if (x + y + 1) % 2 else False)
                )

        pieces: List[PuzzlePiece] = []
        for char, squares in same_char.items():
            if char == ".":
                continue

            piece = PuzzlePiece(squares)
            pieces.append(piece)

        return Board(pieces)

    def to_ascii(self) -> List[str]:
        res = [["." for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
        for piece_mask in self.masks:
            piece = PuzzlePiece.from_bitmask(piece_mask)
            for square in piece.squares:
                res[square.y][square.x] = PUZZLE_PIECE_CHARS[piece.type]

        return ["".join(row) for row in res][::-1]

    def __str__(self) -> str:
        return "\n".join(self.to_ascii())


PUZZLE_56 = [
    ".W........",
    ".WW...T..C",
    "..WWTTT..C",
    "......TCCC",
    "..........",
]
BOARD_56 = Board.from_ascii(PUZZLE_56)
