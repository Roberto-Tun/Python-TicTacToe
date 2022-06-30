board = ["-","-","-","-","-","-","-","-","-"] #list to input the x and o
Taken_Positions = []

def display_board(board): #function that displays the board 
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])


def input_position(x, p): #function that places the 'X' or 'O' at the place the user desires 
    if p == "X": #if that checks which player is inputting
        for i in range(1, len(board)+1): #for that start at 1 and ends at the length of the list and adds 1
            if x == i: #that checks the input of the user
                z = i - 1 #subtracting one from i because i is ahead by one of the index of the board list
                board[z] = "X" #using z to change the index of the board list depending on the value of z
    elif p == "O": #Does same thing as above
        for i in range(1, len(board)+1):
            if x == i:
                z = i - 1
                board[z] = "O"

def CheckWinner(board):
    #checks for horizontal wins
    if board[0] == board[1] == board[2] and board[0] != "-":
        Winner = board[0]
        return Winner
    elif board[3] == board[4] == board[5] and board[3] != "-":
        Winner = board[3]
        return Winner
    elif board[6] == board[7] == board[8] and board[6] != "-":
        Winner = board[6]
        return Winner
    #checks for Vertical wins
    elif board[0] == board[3] == board[6] and board[0] != "-":
        Winner = board[0]
        return Winner
    elif board[1] == board[4] == board[7] and board[1] != "-":
        Winner = board[1]
        return Winner
    elif board[2] == board[5] == board[8] and board[2] != "-":
        Winner = board[2]
        return Winner
    #checks for the X winning style
    elif board[0] == board[4] == board[8] and board[0] != "-":
        Winner = board[0]
        return Winner
    elif board[2] == board[4] == board[6] and board[0] != "-":
        Winner = board[0]
        return Winner



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
    CurrentPlayer = "X"
    while Gameover == False:
        if CurrentPlayer == "X":
            print("X |Player's turn")
            Position = int(input("Enter a number between 1 - 9: ")) #input needs to be a int to compare 
            if Position in Taken_Positions:
                print("This Position is already taken")
            else:
                if Position >= 1 and Position <= 9:
                    input_position(Position, CurrentPlayer)
                    Taken_Positions.append(Position)
                    display_board(board)
                    CurrentPlayer = "O"
                else:
                    print("Invalid Input")
        else:
            print("O |Player's turn")
            Position = int(input("Enter a number between 1 - 9: ")) #input needs to be a int to compare 
            if Position in Taken_Positions:
                print("This Position is already taken")
            else:
                if Position >= 1 and Position <= 9:
                    input_position(Position, CurrentPlayer)
                    Taken_Positions.append(Position)
                    display_board(board)
                    CurrentPlayer = "X"
                else:
                    print("Invalid Input")
            
        Winner = CheckWinner(board)
        if Winner == "X":
            Gameover = True
        elif Winner == "O":
            Gameover = True
    else:
        print("Winner is:", Winner)



TicTacToe()


