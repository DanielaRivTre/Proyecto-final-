"""Tic Tac Toe - Proyecto Final
Modificaciones realizadas por A01712539
"""

from turtle import *
from freegames import line

# Diccionario para registrar casillas ocupadas
occupied = {}

def grid():
    """Dibuja la cuadrícula principal del juego."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)

def drawx(x, y):
    """Dibuja el símbolo X centrado, azul y con grosor 5."""
    color('blue')
    width(5)
    line(x + 25, y + 25, x + 108, y + 108)
    line(x + 25, y + 108, x + 108, y + 25)

def drawo(x, y):
    """Dibuja el símbolo O centrado, rojo y con grosor 5."""
    color('red')
    width(5)
    up()
    goto(x + 66.5, y + 25)
    down()
    circle(41.5)

def floor(value):
    """Redondea la coordenada al límite inferior de la casilla."""
    return float((value + 200) // 133 * 133 - 200)

state = {'player': 0}
players = [drawx, drawo]

def check_winner():
    """Determina si hay un ganador o si el juego termina en empate."""
    coords = [-200.0, -67.0, 66.0]
    lines = []

    # Generar filas y columnas
    for c in coords:
        lines.append([(c, r) for r in coords])
        lines.append([(r, c) for r in coords])

    # Diagonales
    lines.append([(coords[i], coords[i]) for i in range(3)])
    lines.append([(coords[i], coords[2 - i]) for i in range(3)])

    # Evaluar si hay 3 símbolos iguales alineados
    for l in lines:
        if l[0] in occupied and l[1] in occupied and l[2] in occupied:
            if occupied[l[0]] == occupied[l[1]] == occupied[l[2]]:
                return occupied[l[0]]

    # Si se llenaron las 9 casillas sin ganador
    if len(occupied) == 9:
        return 'Empate'

    return None

def tap(x, y):
    """Maneja el clic del usuario y la lógica del turno."""
    x = floor(x)
    y = floor(y)

    # Modificación 2: Validar si la casilla ya está ocupada
    if (x, y) in occupied:
        print("¡Casilla ocupada! Elige un espacio libre.")
        return

    player = state['player']
    draw = players[player]
    draw(x, y)
    update()

    # Guardar la jugada
    occupied[(x, y)] = player

    # Modificación 3: Verificar si el juego terminó
    result = check_winner()
    if result is not None:
        if result == 'Empate':
            print("¡Juego Terminado! Es un EMPATE.")
        else:
            symbol = 'X' if result == 0 else 'O'
            print(f"¡Juego Terminado! El ganador es el jugador {symbol}.")
        onscreenclick(None)
        return

    # Cambiar de turno
    state['player'] = not player

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()