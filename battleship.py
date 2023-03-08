import random
import math

def createBoard(dimens):
    board=[["-"]*dimens for j in range(dimens)]
    for j in range(dimens):
        board[0][j]=j
        board[j][0]=j
    board1 = board
    #place ships on board
    usedr=[]
    usedc=[]
    for i in range(math.ceil(dimens/2)):
        rowss = random.randint(1,dimens)
        columss = random.randint(1,dimens)
        if rowss[i] != usedr[i] and columss[i] != usedc[i]:
            board1[rowss][columss]="S"
            usedr.append(rowss)
            usedc.append(columss)
    return board, board1 



def printBoard(board):
  for b in board:
      print(*b)

myBoard, board1 = createBoard(10)

printBoard(myBoard)
print("\n")

def enterguess():
    column = int(input("What collumn do you want to place your ship? "))
    row = int(input("What row do you want to place your ship? "))

    myBoard[row][column]="X"
    printBoard(myBoard)

enterguess()
