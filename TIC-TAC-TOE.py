def displayboard(board):
    
    print(board[1]+"|"+board[2]+"|"+board[3])
    print(board[4]+"|"+board[5]+"|"+board[6])
    print(board[7]+"|"+board[8]+"|"+board[9])
board = ['','','','','','','','','','']

def playerinput():
    marker = ''
    while marker != "X" and marker != "O":
        marker = input("player 1::choose X,O").upper()
    if marker == "X":
        return ("X","O")
    else:
        return ("O","X")

def place_marker(board,marker,position):
    board[position] = marker
    
def wincheck(board, mark):
    return (board[1] == board[2] == board[3] == mark)or(board[4] == board[5] == board[6] == mark)or(board[7] == board[8] == board[9] == mark)or(board[7] == board[4] == board[1] == mark)or(board[8] == board[5] == board[2] == mark)or(board[9] == board[6] == board[3] == mark)or(board[7] == board[5] == board[3] == mark)or(board[8] == board[5] == board[1] == mark)
import random
def choose_first():
    flip = random.randint(0,1)
    if flip==0:
        return 'player 1'
    else:
        return 'player 2'
def space_check(board, position):
    return board[position] == ''

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True    
def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board,position):
        position = int(input("chosse a position:(1,9)"))
    return position
def replay():
    choise = input("play again y/n")
    return choise == "y"
print("welcome to tic tac toe")
while True:
    
    the_board = [' ']*10
    player1_marker,player2_marker = playerinput()
    
    turn = choose_first()
    print(turn + "will go first")
    
    play_game = input('ready to play? yes or no')
    if play_game == "yes":
        game_on = True
    else:
        game_on = False
    while game_on:
        if turn == 'player 1':
            
            displayboard(board)

            position = player_choice(board)

            place_marker(board,player1_marker,position)

            if wincheck(board,player1_marker):
                displayboard(board)
                print('player 1 has won!!!')
                game_on = False
            else:
                if full_board_check(board):
                    displayboard(board)
                    print("tie game")
                else:
                    turn = "player 2"
        else:
            displayboard(board)

            position = player_choice(board)

            place_marker(board,player2_marker,position)

            if wincheck(board,player1_marker):
                displayboard(board)
                print('player 2 has won!!!')
                game_on = False
            else:
                if full_board_check(board):
                    displayboard(board)
                    print("tie game")
                else:
                    turn = "player 1"
            
            

    if not replay():
        break

