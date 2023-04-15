from typing import Dict, List
from iq_xoxo.concrete_pieces import PUZZLE_PIECES
from iq_xoxo.constants import BOARD_HEIGHT, BOARD_WIDTH, NUM_PIECES, PuzzlePieceType

from iq_xoxo.puzzle_piece import PuzzlePiece

VARIATIONS: Dict[PuzzlePieceType, List[PuzzlePiece]] = {
    piece.type: piece.get_variations() for piece in PUZZLE_PIECES
}

POSSIBLE_PLACEMENT_MASKS: List[List[List[List[int]]]] = [
    [[[] for ___ in range(BOARD_HEIGHT)] for __ in range(BOARD_WIDTH)]
    for _ in range(NUM_PIECES)
]

for piece, variations in VARIATIONS.items():
    for variation in variations:
        for dy in range(BOARD_HEIGHT - variation.max_y()):
            for dx in range(BOARD_WIDTH - variation.max_x()):
                shifted = variation.get_shifted(dx, dy)

                assert shifted.max_x() < BOARD_WIDTH and shifted.max_y() < BOARD_HEIGHT

                if (
                    shifted.squares[0].x + shifted.squares[0].y + 1
                ) % 2 != shifted.squares[0].symbol:
                    continue

                mask = shifted.to_bitmask()

                for s in shifted.squares:
                    POSSIBLE_PLACEMENT_MASKS[int(shifted.type.value)][s.x][s.y].append(
                        mask
                    )
