import random, math, copy, time
from colorama import Fore


def createBoard(dimens):
    
    global counter
    counter = 0
    board=[["-"]*dimens for j in range(dimens)]
    for j in range(dimens):
        board[0][j]=j
        board[j][0]=j
    board1 = copy.deepcopy(board)
    #place ships on board
    usedr=set()
    usedc=set()
    for i in range(math.ceil(dimens/2)):
        rowss = random.randint(1, dimens-1)
        columss = random.randint(1, dimens-1)
        while (rowss, columss) in zip(usedr, usedc):
            rowss = random.randint(0, dimens-1)
            columss = random.randint(0, dimens-1)
        board1[rowss][columss] = "S"
        counter = counter + 1
        usedr.add(rowss)
        usedc.add(columss)
    return board, board1


def printBoard(board):
  for b in board:
      print(*b)

def setup():
    global myBoard, board1
    myBoard, board1 = createBoard(5)

    printBoard(myBoard)
    print("\n")

def enterguess():
    global counter
    row = int(input("What row do you want to place your ship? "))
    column = int(input("What collumn do you want to place your ship? "))
    

    if board1[row][column]=="S":
        myBoard[row][column]="O"
        printBoard(myBoard)
        counter = counter - 1
        
    else:
        myBoard[row][column]="X"
        printBoard(myBoard)
    
while True:
    
    myBoard, board1 = createBoard(5)

    printBoard(myBoard)
    print("\n")
    
    while counter > 0:
        enterguess()
    if counter == 0:
        print(Fore.GREEN + "you win")
        print(Fore.RESET)
        time.sleep(1.5)
