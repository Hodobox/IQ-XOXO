from typing import List, Optional
from iq_xoxo.board import Board
from iq_xoxo.constants import BITMASK_FINISHED, PuzzlePieceType


def _solve(board: Board, pieces_to_go: List[PuzzlePieceType]) -> Optional[Board]:
    if board.mask == BITMASK_FINISHED:
        return board

    # TODO
    return None


def solve(board: Board):
    pieces_to_go = [
        piece for piece in PuzzlePieceType if piece not in board.pieces_used
    ]

    solution = _solve(board, pieces_to_go)

    if solution is None:
        print("No solution :(")

    print(solution.masks)
