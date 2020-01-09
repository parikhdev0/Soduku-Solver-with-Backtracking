from graphics import *

win = GraphWin("Sudoku Solver", 603, 603)

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

labels = []
lineg1 = Line(Point(0, 0), Point(0, 0))
lineg2 = Line(Point(0, 0), Point(0, 0))
lineg3 = Line(Point(0, 0), Point(0, 0))
lineg4 = Line(Point(0, 0), Point(0, 0))


def printBoard(board):
    line1 = Line(Point(0, 201), Point(603, 201))
    line1.setWidth(5)
    line1.draw(win)
    line2 = Line(Point(0, 400), Point(603, 400))
    line2.setWidth(5)
    line2.draw(win)

    Line(Point(0, 67), Point(603, 67)).draw(win)
    Line(Point(0, 134), Point(603, 134)).draw(win)
    Line(Point(0, 67 + 201), Point(603, 67 + 201)).draw(win)
    Line(Point(0, 134 + 201), Point(603, 134 + 201)).draw(win)
    Line(Point(0, 67 + 2 * 201), Point(603, 67 + 2 * 201)).draw(win)
    Line(Point(0, 134 + 2 * 201), Point(603, 134 + 2 * 201)).draw(win)

    line3 = Line(Point(201, 0), Point(201, 603))
    line4 = Line(Point(400, 0), Point(400, 603))
    line3.setWidth(5)
    line4.setWidth(5)
    line3.draw(win)
    line4.draw(win)

    Line(Point(67, 0), Point(67, 603)).draw(win)
    Line(Point(134, 0), Point(134, 603)).draw(win)
    Line(Point(67 + 201, 0), Point(67 + 201, 603)).draw(win)
    Line(Point(134 + 201, 0), Point(134 + 201, 603)).draw(win)
    Line(Point(67 + 2 * 201, 0), Point(67 + 2 * 201, 603)).draw(win)
    Line(Point(134 + 2 * 201, 0), Point(134 + 2 * 201, 603)).draw(win)

    for x in range(len(board)):
        for y in range(len(board)):
            label = Text((Point(33.5 + (x * 67), 33.5 + (y * 67))), str(board[y][x]))
            labels.append(label)
            label.draw(win)


def findEmptySlot(board):
    for y in range(len(board)):
        for x in range(len(board)):
            if board[y][x] == 0:
                return [y, x]
    return False


def checkIfValidPosi(board, numberToInsert, position):
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

    boxx = position[1] // 3
    boxy = position[0] // 3
    for y in range(boxy * 3, boxy * 3 + 3):
        for x in range(boxx * 3, boxx * 3 + 3):
            if board[y][x] == numberToInsert and [y, x] != position:
                return False
    return True


def solve(board):
    empty = findEmptySlot(board)
    if not empty:
        return True
    else:
        row = empty[0]
        column = empty[1]

    for i in range(1, 10):
        if checkIfValidPosi(board, i, [row, column]):

            board[row][column] = i

            labels[column * 9 + row].undraw()
            labels[column * 9 + row] = Text((Point(33.5 + (column * 67), 33.5 + (row * 67))), i)
            labels[column * 9 + row].draw(win)

            lineg1 = Line(Point(column * 67, row * 67), Point((column + 1) * 67, row * 67))
            lineg1.setFill("gold")
            lineg1.draw(win)
            lineg1.setWidth(4)
            lineg2 = Line(Point(column * 67, row * 67), Point(column * 67, (row + 1) * 67))
            lineg2.setFill("gold")
            lineg2.draw(win)
            lineg2.setWidth(4)
            lineg3 = Line(Point((1 + column) * 67, row * 67), Point((column + 1) * 67, (1 + row) * 67))
            lineg3.setFill("gold")
            lineg3.draw(win)
            lineg3.setWidth(4)
            lineg4 = Line(Point((1 + column) * 67, (1 + row) * 67), Point(column * 67, (1 + row) * 67))
            lineg4.setFill("gold")
            lineg4.draw(win)
            lineg4.setWidth(4)

            time.sleep(0.1)
            lineg1.undraw()
            lineg2.undraw()
            lineg3.undraw()
            lineg4.undraw()

            if solve(board):
                return True

            board[row][column] = 0
            labels[column * 9 + row].undraw()
            labels[column * 9 + row] = Text((Point(33.5 + (column * 67), 33.5 + (row * 67))), 0)
            labels[column * 9 + row].draw(win)

            lineg1 = Line(Point(column * 67, row * 67), Point((column + 1) * 67, row * 67))
            lineg1.setFill("gold")
            lineg1.draw(win)
            lineg1.setWidth(4)
            lineg2 = Line(Point(column * 67, row * 67), Point(column * 67, (row + 1) * 67))
            lineg2.setFill("gold")
            lineg2.draw(win)
            lineg2.setWidth(4)
            lineg3 = Line(Point((1 + column) * 67, row * 67), Point((column + 1) * 67, (1 + row) * 67))
            lineg3.setFill("gold")
            lineg3.draw(win)
            lineg3.setWidth(4)
            lineg4 = Line(Point((1 + column) * 67, (1 + row) * 67), Point(column * 67, (1 + row) * 67))
            lineg4.setFill("gold")
            lineg4.draw(win)
            lineg4.setWidth(4)

            time.sleep(0.1)
            lineg1.undraw()
            lineg2.undraw()
            lineg3.undraw()
            lineg4.undraw()

    return False


printBoard(board)
solve(board)
print(board)
win.getKey()