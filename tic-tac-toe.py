#board to display

board=["-","-","-",
      "-","-","-",
      "-","-","-"]

#players identity and choices

player1_name = ""
player2_name = ""
player1_choice =""
player2_choice = ""

#display_board function

def display_board():
    print(board[0]+"|"+board[1]+"|"+board[2])
    print(board[3]+"|"+board[4]+"|"+board[5])
    print(board[6]+"|"+board[7]+"|"+board[8])

#iswinner function to check winner at any time

def isWinner(board):
    if(board[0]==board[4] and board[4]==board[8]):
        if(board[0]==player1_choice):
            return 1
        else:
            return 1
    elif(board[2]==board[4] and board[4]==board[6]):
        if (board[2] == player1_choice):
            return 1
        else:
            return 1
    elif(board[0]==board[1] and board[1]==board[2]):
        if (board[0] == player1_choice):
            return 1
        else:
            return 1
    elif(board[3]==board[4] and board[4]==board[5]):
        if (board[3] == player1_choice):
            return 1
        else:
            return 1
    elif (board[6] == board[7] and board[7] == board[8]):
        if (board[6] == player1_choice):
            return 1
        else:
            return 1
    elif (board[0] == board[3] and board[3] == board[6]):
        if (board[0] == player1_choice):
            return 1
        else:
            return 1
    elif (board[1] == board[4] and board[4] == board[7]):
        if (board[1] == player1_choice):
            return 1
        else:
            return 1
    elif (board[2] == board[5] and board[5] == board[8]):
        if (board[2] == player1_choice):
            return 1
        else:
            return 1
    else:
        return 0

#run_game function to start the game

def run_game():
    player1_name = ""
    player2_name = ""
    player1_choice = ""
    player2_choice = ""
    print("******Welcome to the Tic Tac Toe Game*******")
    print("Two players are required for this game......")
    player1_name=input("Player 1 Enter your name:\n")
    player2_name=input("Player 2 Enter your name:\n")
    player1_choice=input(player1_name+" Select your choice:\n")
    player2_choice=input(player2_name+" Select your choice:\n")
    print(player1_name+" your choice is:"+player1_choice)
    print(player2_name + " your choice is:" + player2_choice)
    print("All the best "+player1_name+" and "+player2_name)
    print("Here we Go!.....")
    display_board()
    for i in range(9):
        if (i % 2 == 0):
            print(player1_name+" it's your turn....")
            print("Select a position from 0-8:")
            n=int(input())
            board[n]=player1_choice
        else:
            print(player2_name+" it's your turn....")
            print("Select a position from 0-8:")
            n=int(input())
            board[n]=player2_choice
        display_board()
        if(i>=5 and isWinner(board)):
            if (board[0] == board[4] and board[4] == board[8]):
                if (board[0] == player1_choice):
                    print(player1_name + " is the winner...")
                else:
                    print(player2_name + " is winner.......")
            elif (board[2] == board[4] and board[4] == board[6]):
                if (board[2] == player1_choice):
                    print(player1_name + " is the winner...")
                else:
                    print(player2_name + " is winner.......")
            elif (board[0] == board[1] and board[1] == board[2]):
                if (board[0] == player1_choice):
                    print(player1_name + " is the winner...")
                else:
                    print(player2_name + " is winner.......")
            elif (board[3] == board[4] and board[4] == board[5]):
                if (board[3] == player1_choice):
                    print(player1_name + " is the winner...")
                else:
                    print(player2_name + " is winner.......")
            elif (board[6] == board[7] and board[7] == board[8]):
                if (board[6] == player1_choice):
                    print(player1_name + " is the winner...")
                else:
                    print(player2_name + " is winner.......")
            elif (board[0] == board[3] and board[3] == board[6]):
                if (board[0] == player1_choice):
                    print(player1_name + " is the winner...")
                else:
                    print(player2_name + " is winner.......")
            elif (board[1] == board[4] and board[4] == board[7]):
                if (board[1] == player1_choice):
                    print(player1_name + " is the winner...")
                else:
                    print(player2_name + " is winner.......")
            elif (board[2] == board[5] and board[5] == board[8]):
                if (board[2] == player1_choice):
                    print(player1_name + " is the winner...")
                else:
                    print(player2_name + " is winner.......")
            break

run_game()