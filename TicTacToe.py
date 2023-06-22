import random
import os
import turtle


def clear():
    os.system( 'cls' )


def playerInput():
    marker = ''
    while not (marker =='X' or marker =='O'):
        marker = input('Player 1: Would you like to be X or O?').upper()

    if (marker == 'X'):
        return ('X', 'O')
    else:
        return ('O', 'X')
    

def placeMarker(board, marker, position):
    board[position] = marker


#Creating board to react to numpad
def winCheck(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[7] == mark and board[4] == mark and board[1] == mark) or
    (board[8] == mark and board[5] == mark and board[2] == mark) or
    (board[9] == mark and board[6] == mark and board[3] == mark) or
    (board[7] == mark and board[5] == mark and board[3] == mark) or
    (board[1] == mark and board[5] == mark and board[9] == mark))


#Creating board and making space holders in marking spots
def display_board(board):
    clear()
    print ('     |     |     ')
    print ('    ' + board[7] + '|    ' + board[8] + '|    ' + board[9])
    print ('     |     |     ')
    print ('-' * 17)
    print ('     |     |     ')
    print ('    ' + board[4] + '|    ' + board[5] + '|    ' + board[6])
    print ('     |     |     ')
    print ('-' * 17)
    print ('     |     |     ')
    print ('    ' + board[1] + '|    ' + board[2] + '|    ' + board[3])
    print ('     |     |     ')


def first():
    if (random.randint(0,1) == 0):
        return ("Player 2 goes first.")
    else:
        return ("Player 1 goes first")


def available(board, position):
    return board[position] == ' '


def fullBoardCheck(board):
    for x in range(1,10):
        if available(board, x):
            return False
    return True


#Asks player where they want to put their marker
#If place is already taken, it asks the question again 
def playerChoice(board):
    position = (' ')
    while position not in "1 2 3 4 5 6 7 8 9".split() or not available(board, int(position)):
        position = input("Choose a position on the board via the numpad.")
    return int(position)


def postWin(pB, gO, p):
    display_board(pB)
    gO = True
    print (f'Congrats {p}!!! You Won!!!')


def game(complete, player1Name, player2Name, theBoard):
    print (f"Welcome to Tic-Tac-Toe {player1Name} and {player2Name}.")
    turn = first()

    while (not complete):
        player1Marker, player2Marker = playerInput()
        turn = first()
        print (turn)
        gameOn = True
        while gameOn:
            if (turn == 'Player 1'):
                #Player 1 turn
                display_board(theBoard)
                position = playerChoice(theBoard)
                placeMarker(theBoard, player1Marker, position)
                if winCheck(theBoard, player1Marker):
                    postWin(theBoard, gameOn, player1Name)
                    exitPrompt = input("Hit [ENTER] to end the program:")
                    exit()
                else:
                    if fullBoardCheck(theBoard):
                        print('The game is a tie')
                        print("The game is a draw.")
                        exitPrompt = input("Hit [ENTER] to end the program:")
                        exit()
                    else:
                        turn = ('Player 2')
            else:
                #Player 2 turn
                display_board(theBoard)
                position = playerChoice(theBoard)
                placeMarker(theBoard, player2Marker, position)
                if winCheck(theBoard, player2Marker):
                    postWin(theBoard, gameOn, player2Name)
                    exitPrompt = input("Hit [ENTER] to end the program:")
                    exit()
                else:
                    if fullBoardCheck(theBoard):
                        print('The game is a tie')
                        exitPrompt = input("Hit [ENTER] to end the program:")
                        exit()
                    else:
                        turn = ('Player 1')


def main():
    gameFin = False
    while not gameFin:
        p1Name = input("Player 1, please enter your name here: ")
        p2Name = input("Player 2, please enter your name here: ")
        cceBoard = [' ']*10
        game(gameFin, p1Name, p2Name, cceBoard)


if (__name__=="__main__"):
    main()

