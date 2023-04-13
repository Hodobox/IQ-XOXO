from typing import List, Tuple
from iq_xoxo.constants import PuzzlePieceType
from iq_xoxo.puzzle_piece import PuzzlePiece
from functools import reduce


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
        # TODO
        raise NotImplementedError()
