from argparse import ArgumentParser
from copy import deepcopy

from iq_xoxo.board import BOARD_56, Board
from iq_xoxo.concrete_pieces import PUZZLE_PIECES
from iq_xoxo.solve import solve

parser = ArgumentParser(
    prog="IQ-XOXO solver",
    description="Helps you solve the IQ-XOXO puzzle game",
    epilog="Is there anything else you'd want this project to do? Make an issue or submit a PR at https://github.com/Hodobox/IQ-XOXO",
)

usage_example = (
    "python3 main.py path-to-puzzle [-l, --list] [-n, --next]\n"
    "puzzle should be a file with the puzzle input in ascii art, like so:\n"
    + str(BOARD_56)
    + "\n"
    + "the . character is an empty square. Same letters should represent one puzzle piece.\n"
    + "pass the -l/--list option to list ASCII arts for convenience\n"
    + "pass the -n/--next option to show where the next piece should be placed in the puzzle"
)

parser.usage = (parser.usage or "") + usage_example


parser.add_argument(
    "puzzle", nargs='?', type=str, help="Path to file with ascii art of the puzzle",
)

parser.add_argument(
    "-l", "--list", action="store_true", help="List ascii art of board and pieces"
)
parser.add_argument(
    "-n",
    "--next",
    action="store_true",
    help="Show where the next puzzle piece should be placed",
)

args = parser.parse_args()

print(f"Welcome to {parser.prog}")

if args.list:
    print("Printing ascii arts:")
    print(Board())
    for piece in PUZZLE_PIECES:
        s = str(piece)
        label, nonlabel = s.split('\n')[0], s.split('\n')[1:]
        nonlabel = [ line.replace('O','X') for line in nonlabel ]
        print(label)
        print('\n'.join(nonlabel))
    exit(0)

if args.puzzle is None:
    print(parser.usage)
    exit(0)


with open(args.puzzle, "r") as puzzle_file:
    puzzle = [l.strip() for l in puzzle_file.readlines()]

try:
    board = Board.from_ascii(puzzle)
except Exception as e:
    print("Something went wrong when loading the puzzle input you provided:")
    print(e)
    exit()

print("Your puzzle was successfuly loaded!")
print("Solving...")
solution = solve(board)
print("Finished solving")

if solution is None:
    print("The puzzle arrangement you provided has no solution!")
    exit()

print("The puzzle arrangement you provided has a valid solution.")

if args.next:

    if len(board.pieces_used) != len(PUZZLE_PIECES):

        board_with_next_piece = deepcopy(solution)
        board_with_next_piece.masks = board_with_next_piece.masks[
            : len(board.pieces_used) + 1
        ]
        board_with_next_piece.mask = sum(board_with_next_piece.masks)

        print("Place your next piece like this:")
        print(board_with_next_piece)
    else:
        print("The puzzle you provided already has all the pieces placed!")
