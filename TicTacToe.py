from ast import Num


board = ["-","-","-","-","-","-","-","-","-"] #list to input the x and o
Nums = []

def display_board(board): #function that displays the board 
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])


def check_input(x, p): #function that places the 'X' or 'O' at the place the user desires 
    if p == "PlayerOne": #if that checks which player is inputting
        for i in range(1, len(board)+1): #for that start at 1 and ends at the length of the list and adds 1
            if x == i: #that checks the input of the user
                z = i - 1 #subtracting one from i because i is ahead by one of the index of the board list
                board[z] = "X" #using z to change the index of the board list depending on the value of z
    elif p == "PlayerTwo": #Does same thing as above
        for i in range(1, len(board)+1):
            if x == i:
                z = i - 1
                board[z] = "O"

def TicTacToe():

    print("----------------------------")
    print("----Welcome to TicTacToe----")
    print("----------------------------")
    print("\n")
    print("1 | 2 | 3")
    print("---------")  #Welcome GUI and Positions related to the number
    print("4 | 5 | 6")
    print("---------")
    print("7 | 8 | 9")
    print("\n")

    Gameover = False
    Switch_Player = False
    while Gameover == False:
        while Switch_Player == False:
            print("X |Player's turn")
            Xuser = int(input("Enter a number between 1 - 9: ")) #input needs to be a int to compare 
            Player = "PlayerOne"
            if Xuser in Nums:
                print("This Position is already taken")
            else:
                check_input(Xuser, Player)
                Nums.append(Xuser)
                display_board(board)
                Switch_Player = True
        else:
            print("O |Player's turn")
            Xuser = int(input("Enter a number between 1 - 9: ")) #input needs to be a int to compare 
            Player = "PlayerTwo"
            if Xuser in Nums:
                print("This Position is already taken")
            else:
                check_input(Xuser, Player)
                Nums.append(Xuser)
                display_board(board)
                Switch_Player = False



TicTacToe()



'''Xuser = int(input("Enter a number between 1 - 9: "))
for i in range(1, len(board)+1):
    if Xuser == i:
        x = i - 1
        board[x] = "x"'''