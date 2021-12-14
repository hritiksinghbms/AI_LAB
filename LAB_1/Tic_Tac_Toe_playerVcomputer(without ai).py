import random

Board = {'1': ' ', '2': ' ', '3': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '7': ' ', '8': ' ', '9': ' '}

board_keys = []

for key in Board:
    board_keys.append(key)

def createBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-----')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-----')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

def game():
    print("X : Human Player")
    print("O : Computer")
    turn = 'O'
    count = 0

    for i in range(10):
        print("\n")
        createBoard(Board)
        print("\n'" + turn + "' turn. Move to which place?")
        
        if turn == 'X':
            move = input()
        
        if turn == 'O':
            if Board['7'] == Board['8'] == 'O' != ' ' and Board['9'] == ' ':
                move='9'
            elif Board['9'] == Board['8'] == 'O' != ' ' and Board['7'] == ' ':
                move='7'
            elif Board['4'] == Board['5'] == 'O' != ' ' and Board['6'] == ' ':
                move='6'
            elif Board['5'] == Board['6'] == 'O' != ' ' and Board['4'] == ' ':
                move='4'
            elif Board['1'] == Board['2'] == 'O' != ' ' and Board['3'] == ' ':
                move='3'
            elif Board['2'] == Board['3'] == 'O' != ' ' and Board['1'] == ' ':
                move='1'
            elif Board['1'] == Board['4'] == 'O' != ' ' and Board['7'] == ' ':
                move='7'
            elif Board['4'] == Board['7'] == 'O' != ' ' and Board['1'] == ' ':
                move='1'
            elif Board['2'] == Board['5'] == 'O' != ' ' and Board['8'] == ' ':
                move='8'
            elif Board['5'] == Board['8'] == 'O' != ' ' and Board['2'] == ' ':
                move='2'
            elif Board['3'] == Board['6'] == 'O' != ' ' and Board['9'] == ' ':
                move='9'
            elif Board['6'] == Board['9'] == 'O' != ' ' and Board['3'] == ' ':
                move='3'
            elif Board['7'] == Board['5'] == 'O' != ' ' and Board['3'] == ' ':
                move='3'
            elif Board['5'] == Board['3'] == 'O' != ' ' and Board['7'] == ' ':
                move='7'
            elif Board['1'] == Board['5'] == 'O' != ' ' and Board['9'] == ' ':
                move='9'
            elif Board['9'] == Board['5'] == 'O' != ' ' and Board['1'] == ' ':
                move='1'
            elif Board['7'] == Board['8'] == 'X' != ' ' and Board['9'] == ' ':
                move='9'
            elif Board['9'] == Board['8'] == 'X' != ' ' and Board['7'] == ' ':
                move='7'
            elif Board['4'] == Board['5'] == 'X' != ' ' and Board['6'] == ' ':
                move='6'
            elif Board['5'] == Board['6'] == 'X' != ' ' and Board['4'] == ' ':
                move='4'
            elif Board['1'] == Board['2'] == 'X' != ' ' and Board['3'] == ' ':
                move='3'
            elif Board['2'] == Board['3'] == 'X' != ' ' and Board['1'] == ' ':
                move='1'
            elif Board['1'] == Board['4'] == 'X' != ' ' and Board['7'] == ' ':
                move='7'
            elif Board['4'] == Board['7'] == 'X' != ' ' and Board['1'] == ' ':
                move='1'
            elif Board['2'] == Board['5'] == 'X' != ' ' and Board['8'] == ' ':
                move='8'
            elif Board['5'] == Board['8'] == 'X' != ' ' and Board['2'] == ' ':
                move='2'
            elif Board['3'] == Board['6'] == 'X' != ' ' and Board['9'] == ' ':
                move='9'
            elif Board['6'] == Board['9'] == 'X' != ' ' and Board['3'] == ' ':
                move='3'
            elif Board['7'] == Board['5'] == 'X' != ' ' and Board['3'] == ' ':
                move='3'
            elif Board['5'] == Board['3'] == 'X' != ' ' and Board['7'] == ' ':
                move='7'
            elif Board['1'] == Board['5'] == 'X' != ' ' and Board['9'] == ' ':
                move='9'
            elif Board['9'] == Board['5'] == 'X' != ' ' and Board['1'] == ' ':
                move='1'
            else :
                move = str(random.randrange(1,10))
        
        if move not in Board.keys() :
            print("Invalid position")
            continue

        if Board[move] == ' ':
            Board[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue
        
        if count >= 5:
            if Board['7'] == Board['8'] == Board['9'] != ' ':
                createBoard(Board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif Board['4'] == Board['5'] == Board['6'] != ' ':
                createBoard(Board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif Board['1'] == Board['2'] == Board['3'] != ' ':
                createBoard(Board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif Board['1'] == Board['4'] == Board['7'] != ' ':
                createBoard(Board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif Board['2'] == Board['5'] == Board['8'] != ' ':
                createBoard(Board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif Board['3'] == Board['6'] == Board['9'] != ' ':
                createBoard(Board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif Board['7'] == Board['5'] == Board['3'] != ' ':
                createBoard(Board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif Board['1'] == Board['5'] == Board['9'] != ' ':
                createBoard(Board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            
            
            
        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":
        for key in board_keys:
            Board[key] = " "

        game()
        
game()

