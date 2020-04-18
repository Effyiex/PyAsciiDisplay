
from display import Vector

import display

display.init("Host_02.py - TicTacToe", 48, 24, 'b', '0')
display.set_frame('#', '#')

width = display.width
height = display.height

icons = Vector('X', 'O')

winner = None

grid = Vector(
    Vector(' ', ' ', ' '),
    Vector(' ', ' ', ' '),
    Vector(' ', ' ', ' ')
)

w_tile = width / 6
h_tile = height / 6

bot = False
turn = False

while True:

    display.background(' ')
    display.fill_state(width / 3, 0, 1, height, display.frame.x)
    display.fill_state(width / 3 * 2, 0, 1, height, display.frame.x)
    display.fill_state(0, height / 3, width, 1, display.frame.y)
    display.fill_state(0, height / 3 * 2, width, 1, display.frame.y)
    for xi in range(3):
        for yi in range(3):
            x = w_tile * (xi * 2 + 1)
            y = h_tile * (yi * 2 + 1)
            display.set_state(x, y, grid.index(yi).index(xi))
    display.render()

    if not (turn and bot):
        vec = Vector(-1, -1)
        while (vec.x < 0 and vec.y < 0):
            i = input("On which Position(x, y) do you wanna place your icon?\n>>> ")
            if len(i) != 4 or i[1] != ',' or i[2] != ' ' : i = "9, 9"
            vec = Vector(int(i[0]) - 1, int(i[3]) - 1)
            if vec.x >= 0 and vec.y >= 0 and vec.x < 3 and vec.y < 3 and grid.index(yi).index(xi) is ' ':
                setter = icons.x
                if turn : setter = icons.y
                grid.index(vec.y).index(vec.x, setter)
            else:
                vec = Vector(-1, -1)
                print("False Input")
                display.render("pause")

    turn = not turn
        
        
    
    
    
