"""Memory game adapted from Free Python Games.

Author of the modifications: Luis Gabriel Miranda Espinoza.
Student ID: A01714017.

The game uses a 4x4 board with eight matching pairs.
It displays the number of discovered pairs and a victory message
when all tiles have been revealed.
"""

from random import *
from turtle import *

from freegames import path

# Keep the board 400 pixels wide while changing the number of cells.
GRID_SIZE = 4
CELL_SIZE = 400 // GRID_SIZE

car = path('car.gif')

# Each value appears twice, producing eight pairs on the 4x4 board.
tiles = list(range(GRID_SIZE * GRID_SIZE // 2)) * 2

# mark stores the selected tile index; pairs counts completed matches.
state = {'mark': None, 'pairs': 0}

# True means the tile is covered; matched tiles become False.
hide = [True] * len(tiles)

def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(CELL_SIZE)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    # Shift the board origin from (-200, -200) to (0, 0).
    column = int((x + 200) // CELL_SIZE)
    row = int((y + 200) // CELL_SIZE)
    return row * GRID_SIZE + column


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    # Recover the bottom-left corner of a tile from its list index.
    x = (count % GRID_SIZE) * CELL_SIZE - 200
    y = (count // GRID_SIZE) * CELL_SIZE - 200
    return x, y


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    # Ignore clicks outside the board, including the counter area.
    if not (-200 <= x < 200 and -200 <= y < 200):
        return

    spot = index(x, y)

    # Ignore revealed tiles so completed pairs cannot be counted again.
    if not hide[spot]:
        return

    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        # Count a pair only after matching two different covered tiles.
        state['pairs'] += 1


def draw():
    """Draw image, tiles, pair counter, and victory message."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(len(tiles)):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + CELL_SIZE / 2, y + CELL_SIZE / 2 - 20)
        color('black')
        write(
            tiles[mark],
            align='center',
            font=('Arial', 30, 'normal'),
        )
    # Derive the total from the tile list so it follows the board size.
    up()
    goto(0, 210)
    color('black')
    write(
        f"Pares descubiertos: {state['pairs']}/{len(tiles) // 2}",
        align='center',
        font=('Arial', 14, 'normal'),
    )
    # The game ends when no covered tiles remain.
    if not any(hide):
        up()
        goto(0, -230)
        color('darkgreen')
        write(
            "¡Ganaste! Descubriste todos los pares",
            align='center',
            font=('Arial', 12, 'bold'),
        )
        # Disable input and stop scheduling redraws after victory.
        onscreenclick(None)
        update()
        return

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 500, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
