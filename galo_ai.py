# Tic Tac Toe with minimax algorithm
import sys

NONE = TIE = 0
ME = 1
ENEMY = -1

def draw_tab(values, me = "X", enemy = "O"):
    """Draws the board"""
    tab = "{0}|{1}|{2}\n{3}|{4}|{5}\n{6}|{7}|{8}"
    conv = {NONE: "_", ME: me, ENEMY: enemy}
    dtab = tab.format(*map(lambda x: conv[x], values))
    print(dtab[:-5] + dtab[-5:].replace("_", " "))

def check_victory(values):
    """Checks for victory of any of the players"""
    for i in range(3):
        if values[3*i] == values[3*i+1] == values[3*i+2] != NONE: #Horizontal
            return values[3*i]
        if values[i] == values[i+3] == values[i+6] != NONE: #Vertical
            return values[i]
    if values[0] == values[4] == values[8] != NONE: #Diagonal (\)
        return values[0]
    if values[2] == values[4] == values[6] != NONE: #Other diagonal (/)
        return values[2]
    return NONE #No victory yet

def check_tie(values):
    """Checks for ties"""
    for v in values:
        if v == NONE:
            return False
    return True

def minmax(values, player, play = 0):
    """Runs the minimax algorithm for the whoe game"""
    res = check_victory(values) #One player won
    if res != NONE:
        return res, play
    if check_tie(values): #Tie
        return TIE, play
    best_play = 0
    best_score = -2 #Scores always bigger than -2, so this value will always change
    for i in range(9): #Test all possible places
        if values[i] != NONE: #Place already occupied
            continue
        values2 = values[:]
        values2[i] = player
        res, _ = minmax(values2, -player, i) #Try this place
        if res*player > best_score: #res = 1 if ME won, -1 if ENEMY won, 0 if tie. If player is ENEMY, -1 is good, and so we change signs (*player)
            best_play = i
            best_score = res*player
    return best_score*player, best_play #best_score*player because ENEMY swaps signs

def end_of_game(values):
    if check_tie(values):
        print("End of game. Tie.")
        return True
    if check_victory(values) != NONE:
        if check_victory(values) == ME:
            print("End of game. I win.")
            return True
        else:
            print("End of game. You win.")
            return True
    return False

values = [NONE]*9

print("Choose a piece [X or O]: ")
enemy = input().upper()
if enemy != "X" and enemy != "O":
    print("Invalid choice.")
    sys.exit(-1)

me = ["X", "O"][enemy == "X"]
if me == "X":
    i_go = True
else:
    i_go = False

while True:
    if end_of_game(values):
        break
    if i_go:
        _, play = minmax(values, ME)
        values[play] = ME
    draw_tab(values, me, enemy)
    if end_of_game(values):
        break
    while True:
        print("Choose an option [0-8]: ")
        try:
            choice = int(input())
            if choice < 0 or choice > 8:
                raise ValueError("Invalid Value")
            if values[choice] != NONE:
                raise ValueError("Invalid Value")
        except ValueError:
            print("Invalid option. Try again.")
        else:
            break
    values[choice] = ENEMY
    i_go = True
