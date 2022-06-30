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

def CheckWinner(board): #functions that checks the different ways the user can win
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
    elif board[2] == board[4] == board[6] and board[2] != "-":
        Winner = board[2]
        return Winner
    #checks if it a tie
    elif "-" not in board:
        Winner = "Tie"
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
            if Position in Taken_Positions: #checks if the number entered isn't already taken 
                print("This Position is already taken")
            else:
                if Position >= 1 and Position <= 9: #checks that the number is between the limits 
                    input_position(Position, CurrentPlayer) #calling the input position function
                    Taken_Positions.append(Position) #appending the current position used to the taken position list 
                    display_board(board) #display the updated board
                    CurrentPlayer = "O" #switch player
                else:
                    print("Invalid Input")
        else: #does the same thing as above 
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
        print("\n")
            
        Winner = CheckWinner(board)#calls the Check Winner Function to see who wins
        if Winner == "X": #checks if there is a winner to change Gameover to True
            Gameover = True
        elif Winner == "O":
            Gameover = True
        elif Winner == "Tie":
            Gameover = True


        
    else:
        if Winner == "Tie":
            print("Its a Tie")
        else: #else that prints the winner
            print("Winner is:", Winner)

#while for the users to continue playing if they wish
play = input("Would you like to Play Tic Tac Toe: Enter 'Y' or 'N' ").upper()
while play == "Y":
    TicTacToe()
    play = input("Would you like to play again: Enter 'Y' or 'N' ").upper()
else:
    print("I guess your boring")


