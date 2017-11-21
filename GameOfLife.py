#!/usr/bin/python3
# Conway's Game of Life in python
import tkinter
import random
import copy

#Global names
WINDOW_SIZE = 640
EXTRA_SIZE = 60
SQUARE_SIZE = 5
UPDATE_TIME = 100 #1s
GAME_SIZE = WINDOW_SIZE//SQUARE_SIZE

def randbin(p):
    """Returns a 0 or a 1 (the latter with probability p)"""
    if random.random() < p:  # On with probability p
        return 1
    return 0

def count_neighbours(game, i, j):
    """Returns the number of active neighbours"""
    s = 0
    for il in range(i-1, i+2):
        for jl in range(j-1, j+2):
            if il == i and jl == j: #Ignore the cell itself
                continue
            s += game[il%GAME_SIZE][jl%GAME_SIZE]
    return s

def update_game():
    """Draws the game board"""
    global canvas, base, game
    old_game = copy.deepcopy(game)
    canvas.delete("all")
    for i in range(GAME_SIZE):
        for j in range(GAME_SIZE):
            neig = count_neighbours(old_game, i, j) #Computations are performed in old state
            if neig < 2 or neig > 3:
                game[i][j] = 0
            elif neig == 3:
                game[i][j] = 1
            #In other cases, the game remains unchanged

            if old_game[i][j]:
                canvas.create_rectangle(j*SQUARE_SIZE, i*SQUARE_SIZE, j*SQUARE_SIZE+SQUARE_SIZE, i*SQUARE_SIZE+SQUARE_SIZE, fill="black")
    
    base.after(UPDATE_TIME, update_game)

def draw_pattern(pattern):
    """Draws pattern in the middle of the game board"""
    global game
    rows = len(pattern)
    cols = len(pattern[0])

    if rows%2 == 0: #even
        istart, ifinish = GAME_SIZE//2-rows//2, GAME_SIZE//2+rows//2
    else:
        istart, ifinish = GAME_SIZE//2-rows//2, GAME_SIZE//2+rows//2+1

    if cols%2 == 0:
        jstart, jfinish = GAME_SIZE//2-cols//2, GAME_SIZE//2+cols//2
    else:
        jstart, jfinish = GAME_SIZE//2-cols//2, GAME_SIZE//2+cols//2+1
    
    for i in range(istart, ifinish):
        game[i][jstart:jfinish] = pattern[i-istart]

game = [[randbin(0.3) for i in range(GAME_SIZE)] for j in range(GAME_SIZE)]
# glidder_gun = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
#                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
#                [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
# pattern = [[0, 0, 1, 1, 1, 0, 0],
#            [0, 1, 0, 0, 0, 1, 0],
#            [1, 0, 0, 0, 0, 0, 1],
#            [1, 0, 0, 0, 0, 0, 1],
#            [1, 1, 1, 0, 1, 1, 1]]

# draw_pattern(glidder_gun)

#Draw Window
base = tkinter.Tk() #Base window
base.resizable(width=False, height=False) #Disallow resizing
base.minsize(width = WINDOW_SIZE+EXTRA_SIZE, height = WINDOW_SIZE)
base.title("Game of Life")

#Drawing Canvas
canvas = tkinter.Canvas(base, width=WINDOW_SIZE, height=WINDOW_SIZE)
canvas.config(background="white")
canvas.grid(row = 0, column = 0, rowspan = 20)
#canvas.bind("<Button-1>", canvas_clicked)

#Draw new button
#new_button = tkinter.Button(base, text="New Track", command=new_track)
#new_button.grid(row = 3, column = 1)

update_game()
#Show window
base.mainloop()
