from copy import deepcopy
from dataclasses import dataclass
from typing import List, Optional, Set, Tuple

from iq_xoxo.constants import (
    BOARD_WIDTH,
    NUM_BITS,
    PUZZLE_PIECE_ARTS,
    PUZZLE_PIECE_NAMES,
    SQUARES_PER_PIECE,
    PuzzlePieceType,
)


@dataclass
class PuzzlePieceSquare:
    x: int
    y: int
    symbol: bool

    def __str__(self) -> str:
        return f"({self.x},{self.y},{'OX'[self.symbol]})"

    def __repr__(self) -> str:
        return self.__str__()


def squares_from_ascii_art(ascii: List[str]) -> List[PuzzlePieceSquare]:
    squares: List[PuzzlePieceSquare] = []

    for y, row in enumerate(ascii[::-1]):
        for x, c in enumerate(row):
            if c in "XO":
                squares.append(PuzzlePieceSquare(x, y, c == "X"))

    squares = shift_squares(
        squares, -min([s.x for s in squares]), -min([s.y for s in squares])
    )
    return squares


def squares_to_ascii_art(squares: List[PuzzlePieceSquare]) -> List[str]:
    squares = shift_squares(
        squares, -min([s.x for s in squares]), -min([s.y for s in squares])
    )
    R = max([s.y for s in squares]) + 1
    C = max([s.x for s in squares]) + 1

    ascii = [["." for _ in range(C)] for __ in range(R)]
    for s in squares:
        ascii[s.y][s.x] = "OX"[s.symbol]

    return ["".join(row) for row in ascii[::-1]]


def squares_to_bitmask(squares: List[PuzzlePieceSquare]) -> int:
    return sum([1 << (BOARD_WIDTH * s.y + s.x) for s in squares])


def squares_from_bitmask(mask: int) -> List[PuzzlePieceSquare]:
    squares: List[PuzzlePieceSquare] = []
    for bit in range(NUM_BITS):
        if mask & (1 << bit):
            x = bit % BOARD_WIDTH
            y = bit // BOARD_WIDTH
            symbol = True if (x + y + 1) % 2 else False
            squares.append(PuzzlePieceSquare(x, y, symbol))
    return squares


def rotate_squares(squares: List[PuzzlePieceSquare]) -> List[PuzzlePieceSquare]:
    rotated_squares = [PuzzlePieceSquare(s.y, -s.x, s.symbol) for s in squares]
    miny = min([s.y for s in rotated_squares])
    for s in rotated_squares:
        s.y -= miny
    return rotated_squares


def flip_squares(squares: List[PuzzlePieceSquare]) -> List[PuzzlePieceSquare]:
    flipped_squares = [PuzzlePieceSquare(-s.x, s.y, not s.symbol) for s in squares]
    minx = min([s.x for s in flipped_squares])
    for s in flipped_squares:
        s.x -= minx
    return flipped_squares


def shift_squares(
    squares: List[PuzzlePieceSquare], dx: int, dy: int
) -> List[PuzzlePieceSquare]:
    return [PuzzlePieceSquare(s.x + dx, s.y + dy, s.symbol) for s in squares]


def get_puzzle_piece_square_variations(
    squares: List[PuzzlePieceSquare],
) -> List[List[PuzzlePieceSquare]]:
    variations: List[List[PuzzlePieceSquare]] = []
    uniques: Set[Tuple[Tuple[int, int, bool], ...]] = set()

    for flip in [False, True]:
        variation = deepcopy(squares)
        if flip:
            variation = flip_squares(variation)

        for _ in range(4):
            unique_repr = tuple(sorted([(s.x, s.y, s.symbol) for s in variation]))

            if unique_repr not in uniques:
                variations.append(variation)
                uniques.add(unique_repr)
            variation = rotate_squares(variation)

    return variations


def infer_puzzle_piece_type_from_squares(
    squares: List[PuzzlePieceSquare],
) -> PuzzlePieceType:
    if len(squares) != SQUARES_PER_PIECE:
        raise ValueError(
            f"Puzzle piece must have {SQUARES_PER_PIECE} squares, has {len(squares)}"
        )

    squares = shift_squares(
        squares, -min([s.x for s in squares]), -min([s.y for s in squares])
    )
    ascii = squares_to_ascii_art(squares)

    for type, model_art in PUZZLE_PIECE_ARTS.items():
        model_squares = squares_from_ascii_art(model_art)
        for variation in get_puzzle_piece_square_variations(model_squares):
            variation_art = squares_to_ascii_art(variation)
            if variation_art == ascii:
                return type

    raise ValueError(f"No puzzle piece matches given squares")


class PuzzlePiece:
    def __init__(
        self, squares: List[PuzzlePieceSquare], type: Optional[PuzzlePieceType] = None
    ):
        self.squares = squares
        self.type = type or infer_puzzle_piece_type_from_squares(squares)

    @classmethod
    def from_ascii(cls, ascii: List[str]) -> "PuzzlePiece":
        return PuzzlePiece(squares_from_ascii_art(ascii))

    def to_ascii(self) -> List[str]:
        return squares_to_ascii_art(self.squares)

    @classmethod
    def from_bitmask(cls, mask: int) -> "PuzzlePiece":
        return PuzzlePiece(squares_from_bitmask(mask))

    def to_bitmask(self) -> int:
        return squares_to_bitmask(self.squares)

    def __str__(self) -> str:
        return f"{PUZZLE_PIECE_NAMES[self.type]}\n" + "\n".join(self.to_ascii())

    def __repr__(self) -> str:
        return self.__class__.__name__ + "\n" + self.__str__()

    def max_x(self):
        return max([s.x for s in self.squares])

    def max_y(self):
        return max([s.y for s in self.squares])

    def get_rotated(self) -> "PuzzlePiece":
        return PuzzlePiece(rotate_squares(self.squares), self.type)

    def get_flipped(self) -> "PuzzlePiece":
        return PuzzlePiece(flip_squares(self.squares), self.type)

    def get_shifted(self, dx: int, dy: int) -> "PuzzlePiece":
        return PuzzlePiece(shift_squares(self.squares, dx, dy), self.type)

    def get_variations(self) -> "List[PuzzlePiece]":
        return [
            PuzzlePiece(variation, self.type)
            for variation in get_puzzle_piece_square_variations(self.squares)
        ]
