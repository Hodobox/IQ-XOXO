from copy import deepcopy
from dataclasses import dataclass
from typing import List, Set, Tuple


@dataclass
class PuzzlePieceSquare:
    x: int
    y: int
    symbol: bool


class PuzzlePiece:
    def __init__(self, name: str, squares: List[PuzzlePieceSquare]):
        self.squares = squares
        self.name = name

    @classmethod
    def from_ascii(cls, name: str, ascii: List[str]) -> "PuzzlePiece":
        squares: List[PuzzlePieceSquare] = []

        for y, row in enumerate(ascii[::-1]):
            for x, c in enumerate(row):
                if c in "XO":
                    squares.append(PuzzlePieceSquare(x, y, c == "X"))

        return PuzzlePiece(name, squares)

    def to_ascii(self) -> List[str]:
        R = max([s.y for s in self.squares]) + 1
        C = max([s.x for s in self.squares]) + 1

        ascii = [["." for _ in range(C)] for __ in range(R)]
        for s in self.squares:
            ascii[s.y][s.x] = "OX"[s.symbol]

        return ["".join(row) for row in ascii[::-1]]

    def __str__(self) -> str:
        return f"{self.name}\n" + "\n".join(self.to_ascii())

    def __repr__(self) -> str:
        return self.__class__.__name__ + "\n" + self.__str__()

    def _get_rotated(self) -> "PuzzlePiece":
        rotated_squares = [PuzzlePieceSquare(s.y, -s.x, s.symbol) for s in self.squares]
        miny = min([s.y for s in rotated_squares])
        for s in rotated_squares:
            s.y -= miny
        return PuzzlePiece(self.name, rotated_squares)

    def _get_flipped(self) -> "PuzzlePiece":
        flipped_squares = [
            PuzzlePieceSquare(-s.x, s.y, not s.symbol) for s in self.squares
        ]
        minx = min([s.x for s in flipped_squares])
        for s in flipped_squares:
            s.x += -minx
        return PuzzlePiece(self.name, flipped_squares)

    def get_variations(self) -> "List[PuzzlePiece]":
        variations: List[PuzzlePiece] = []
        uniques: Set[Tuple[Tuple[int, int, bool], ...]] = set()

        for flip in [False, True]:
            variation = deepcopy(self)
            if flip:
                variation = variation._get_flipped()

            for _ in range(4):
                unique_repr = tuple(
                    sorted([(s.x, s.y, s.symbol) for s in variation.squares])
                )

                if unique_repr not in uniques:
                    variations.append(variation)
                    uniques.add(unique_repr)
                variation = variation._get_rotated()

        return variations
