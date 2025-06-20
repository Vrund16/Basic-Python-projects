import random

board=["_"]*9              # can also write "_" in 3 by 3 form inside the bracket's   
currentPlayer="X"   
winner=None
GameRunning=True

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])

    print(board[3] + " | " + board[4] + " | " + board[5])
    
    print(board[6] + " | " + board[7] + " | " + board[8])
          
def playerInput(board):
    inp=int(input("Enter a number 1-9: "))
    if inp>=1 and inp<=9 and board[inp-1]=="_":
        board[inp-1]=currentPlayer
    else:
        print("Oops player has alredy occupied!")

def checkHorizontal(board):
    global winner
    
    if board[0] == board[1] == board[2] and board[0]!="_":
        winner = board[0]
        return True
    
    elif board[3] == board[4] == board[5] and board[3] != "_":
        winner = board[3]
        return True
    
    elif board[6] == board[7] == board[8] and board[6] != "_":
        winner = board[6]
        return True
        
def checkRow(board):
    global winner
    
    if board[0] == board[3] == board[6] and board[0]!="_":
        winner=board[0]
        return True
        
    elif board[1] == board[4] == board[7] and board[1]!="_":
        winner=board[1]
        return True
        
    elif board[2] == board[5] == board[8] and board[2]!="_":
        winner=board[2]
        return True
        
def checkDiagonal(board):
    global winner
    
    if board[0] == board[4] == board[8] and board[0]!="_":
        winner=board[0]
        return True
    
    elif board[2] == board[4] == board[6] and board[2]!="_":
        winner=board[2]
        return True
    return False
    
def checkTie(board):
    global GameRunning
    if "_" not in board and winner is None:
        printBoard(board)
        print("It's a tie!")
        GameRunning=False
        
def checkWin(board):
    if checkDiagonal(board) or checkRow(board) or checkHorizontal(board):
        printBoard(board)
        print(f"The winner is {winner}")
        Gamerunning=False
    
def switchPlayer():
    global currentPlayer
    if currentPlayer=="X":
        currentPlayer="O"
        
    else:
        currentPlayer="X"
        
def computer(board):
    if currentPlayer=="O" and GameRunning:
        position=random.randint(0, 8)
        while board[position]!="_":
            position=random.randint(0,8)
        board[position]="O"
        switchPlayer()
    
while GameRunning:
    printBoard(board)
    if currentPlayer=="X":
         playerInput(board)
    checkWin(board)
    checkTie(board)
    switchPlayer()
    computer(board)
    checkWin(board)
    checkTie(board)