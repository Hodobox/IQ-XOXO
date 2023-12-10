# IQ-XOXO

Python solver/helper of IQ-XOXO puzzle game, standard libraries only.

## Usage

```bash
python3 main.py path-to-puzzle [-l, --list] [-n, --next]
```

puzzle should be a file with the puzzle input in ascii art, like `BOARD_56.txt`:
```
.W........
.WW...T..C
..WWTTT..C
......TCCC
..........
```
the `.` character is an empty square. Same letters should represent one puzzle piece.
pass the `-l/--list` option to list ASCII arts for convenience.
pass the `-n/--next` option to show where the next piece should be placed in the puzzle.

So
```bash
python3 main.py BOARD_56.txt
```

will simply tell you
```
Welcome to IQ-XOXO solver
Your puzzle was successfuly loaded!
Solving...
Finished solving
The puzzle arrangement you provided has a valid solution.
```

while 
```
python3 main.py BOARD_56.txt --next
```
additionally shows you (one of) the next moves:
```
Place your next piece like this:
.W........
.WW...T..C
..WWTTT..C
......TCCC
.....=====
```

## Solver logic TL;DR

The board is 5x10 squares, so it can be represented as a 50-bit bitmasks (fits in four bytes!).
Since we also care about the pieces used, we also need a list of pieces and their positions (you 
guessed it, we can use the same type of bitmask).

At any given point, we have a board with some pieces on it. We then have a set of pieces yet
to be used, and want to place the next one.

For each square on the board, we preprocess (for each piece) all the ways the piece can
overlap with this square.

During solving, we check how many total possibilities we have for each square (how many
variations of each piece, that overlap this square, fit onto the current board).

We pick the square with the fewest possibilities, try all of them, and solve recursively.

## Ascii arts

For convenience, here are all the ascii arts of the pieces :)

```
Board
..........
..........
..........
..........
..........

LINE_PIECE
XXXXX

X
X
X
X
X

XXXXX

X
X
X
X
X

T_PIECE
XXX
.X.
.X.

..X
XXX
..X

.X.
.X.
XXX

X..
XXX
X..

XXX
.X.
.X.

..X
XXX
..X

.X.
.X.
XXX

X..
XXX
X..

U_PIECE
X.X
XXX

XX
X.
XX

XXX
X.X

XX
.X
XX

X.X
XXX

XX
X.
XX

XXX
X.X

XX
.X
XX

L_PIECE
X.
X.
X.
XX

XXXX
X...

XX
.X
.X
.X

...X
XXXX

.X
.X
.X
XX

X...
XXXX

XX
X.
X.
X.

XXXX
...X

Z_PIECE
.XX
.X.
XX.

X..
XXX
..X

XX.
.X.
.XX

..X
XXX
X..

P_PIECE
XX
XX
X.

XXX
.XX

.X
XX
XX

XX.
XXX

XX
XX
.X

.XX
XXX

X.
XX
XX

XXX
XX.

W_PIECE
X..
XX.
.XX

.XX
XX.
X..

XX.
.XX
..X

..X
.XX
XX.

..X
.XX
XX.

X..
XX.
.XX

.XX
XX.
X..

XX.
.XX
..X

CORNER_PIECE
X..
X..
XXX

XXX
X..
X..

XXX
..X
..X

..X
..X
XXX

..X
..X
XXX

X..
X..
XXX

XXX
X..
X..

XXX
..X
..X

POINTING_PIECE
X.
XX
X.
X.

XXXX
..X.

.X
.X
XX
.X

.X..
XXXX

.X
XX
.X
.X

..X.
XXXX

X.
X.
XX
X.

XXXX
.X..

WAVING_PIECE
.X
XX
X.
X.

XXX.
..XX

.X
.X
XX
X.

XX..
.XXX

X.
XX
.X
.X

..XX
XXX.

X.
X.
XX
.X

.XXX
XX..
```
