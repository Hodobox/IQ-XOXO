from iq_xoxo.board import Board
from iq_xoxo.solve import solve

puzzle001 = [
    "ZZUUUW....",
    "CZUTUWW...",
    "CZZTTTWW..",
    "CCCTXXXX.L",
    "=====XLLLL",
]

puzzle025 = [
    ".XXXX.....",
    "..X=====..",
    "...TPPZZ..",
    ".TTTPPZ...",
    "...TPZZ...",
]

puzzle072 = [
    "..........",
    "..........",
    "CZ........",
    "CZZZPPP...",
    "CCCZPP....",
]

puzzle086 = [
    "..........",
    "..........",
    "..........",
    "......L...",
    ".=====LLLL",
]

puzzle110 = [
    ".=====....",
    "..........",
    "..........",
    "..........",
    "..........",
]

from time import time


board = Board.from_ascii(puzzle110)


print(board)

print()

s = time()
solution = solve(board)
e = time()

print(solution)

print(f"{e - s:.3f} seconds")
