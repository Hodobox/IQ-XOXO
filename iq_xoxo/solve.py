from copy import deepcopy
from typing import List, Optional, Tuple

from iq_xoxo.board import Board
from iq_xoxo.constants import (BITMASK_FINISHED, BOARD_HEIGHT, BOARD_WIDTH,
                               PuzzlePieceType)
from iq_xoxo.variations import POSSIBLE_PLACEMENT_MASKS


def _solve(board: Board, pieces_to_go: List[PuzzlePieceType]) -> Optional[Board]:
    if board.mask == BITMASK_FINISHED:
        return board

    best_square: Tuple[int, int] = (-1, -1)
    best_square_possibilities: int = 1 << 20

    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            m = 1 << (BOARD_WIDTH * y + x)

            if m & board.mask:
                continue

            possibilities = 0
            for piece_type_to_go in pieces_to_go:
                for possibility in POSSIBLE_PLACEMENT_MASKS[piece_type_to_go.value][x][
                    y
                ]:
                    if (possibility & board.mask) == 0:
                        possibilities += 1

            if possibilities == 0:
                return None

            if possibilities < best_square_possibilities:
                best_square = (x, y)
                best_square_possibilities = possibilities

    x, y = best_square
    for i, piece_type_to_go in enumerate(pieces_to_go):
        pieces_to_go_after = pieces_to_go[:i] + pieces_to_go[i + 1 :]

        for possibility in POSSIBLE_PLACEMENT_MASKS[int(piece_type_to_go.value)][x][y]:
            if (possibility & board.mask) != 0:
                continue

            board.masks.append(possibility)
            board.mask |= possibility
            board.pieces_used.append(piece_type_to_go)

            solution = _solve(board, pieces_to_go_after)

            if solution is not None:
                return solution

            board.mask ^= possibility
            board.masks.pop()
            board.pieces_used.pop()

    return None


def solve(board: Board) -> Optional[Board]:
    pieces_to_go = [
        piece for piece in PuzzlePieceType if piece not in board.pieces_used
    ]

    solution = _solve(deepcopy(board), pieces_to_go)

    return solution
