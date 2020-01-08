board = [
    [0, 5, 0, 0, 6, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 7, 8, 0, 3],
    [0, 0, 7, 0, 3, 4, 0, 0, 0],
    [0, 0, 0, 0, 0, 5, 9, 0, 0],
    [0, 0, 0, 0, 9, 0, 0, 0, 0],
    [8, 6, 0, 1, 7, 0, 0, 0, 4],
    [0, 0, 0, 0, 0, 3, 2, 1, 0],
    [0, 0, 0, 0, 5, 0, 6, 0, 7],
    [0, 4, 0, 0, 0, 0, 5, 0, 9],
]

def printBoard(board):
    for x in range(len(board)):
        stringy=""
        for y in range(len(board)):
            stringy = stringy + (str(board[x][y])+" ")
            if (y%3 == 2):
                stringy += "   "
        print(stringy)
        if ((x-2)%3 == 0):
            print()

def findEmptySlot(board):
    for y in range(len(board)):
        for x in range(len(board)):
            if board[y][x]==0:
                return [y,x]
    return False
def checkIfValidPosi (board, numberToInsert, position):
    for i in range(len(board)):
        if position[1] == i:
            continue
        elif (board[position[0]][i] == numberToInsert):
            return False
    for i in range(len(board)):
        if position[0] == i:
            continue
        elif (board[i][position[1]] == numberToInsert):
            return False

    boxx = position[1]//3
    boxy = position[0]//3
    for y in range (boxy*3,boxy*3+3):
        for x in range(boxx*3,boxx*3+3):
            if board[y][x]==numberToInsert and [y,x]!=position:
                return False
    return True

def solve(board):
    empty = findEmptySlot(board)
    if not empty:
        return True
    else:
        row = empty[0]
        column = empty[1]

    for i in range (1,10):
        if checkIfValidPosi(board, i, [row,column]):
            board[row][column]=i

            if solve(board):
                return True

            board[row][column]=0
    return False

printBoard(board)
solve(board)
printBoard(board)