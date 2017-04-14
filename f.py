#import copy
#row = [0, 0, 0, 0, 0, 0, 0, 0]
#col = [0, 0, 0, 0, 0, 0, 0, 0]
# board = [[0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0]
#          ]
boardPostions = []
def getEmptyBoard():
    emptyBoard = [[0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0]
                     ]
    return emptyBoard
#
# Function to check if board has an empty square that can not be reached from 2 or more squares
#
def canReachFrom2Squares(board):
    if board[8][2] >= 62:
        return True
    print("checking unreacheable squares")

    for i in range(8):
        for j in range(8):
            canReach = 0;
            if board[i][j] == 0:
                #
                newRow = i+2
                newCol = j+1
                if canReach <2 and newRow in range(0,8) and newCol in range(0,8) and board[newRow][newCol]==0:
                    canReach = canReach+1
                #
                newRow = i+2
                newCol = j-1
                if canReach <2 and newRow in range(0,8) and newCol in range(0,8) and board[newRow][newCol]==0:
                    canReach = canReach+1
                #
                newRow = i-2
                newCol = j+1
                if canReach <2 and newRow in range(0,8) and newCol in range(0,8) and board[newRow][newCol]==0:
                    canReach = canReach+1
                #
                newRow = i-2
                newCol = j-1
                if canReach <2 and newRow in range(0,8) and newCol in range(0,8) and board[newRow][newCol]==0:
                    canReach = canReach+1
                #
                newRow = i+1
                newCol = j+2
                if canReach <2 and newRow in range(0,8) and newCol in range(0,8) and board[newRow][newCol]==0:
                    canReach = canReach+1
                #
                newRow = i+1
                newCol = j-2
                if canReach <2 and newRow in range(0,8) and newCol in range(0,8) and board[newRow][newCol]==0:
                    canReach = canReach+1
                #
                newRow = i-1
                newCol = j+2
                if canReach <2 and newRow in range(0,8) and newCol in range(0,8) and board[newRow][newCol]==0:
                    canReach = canReach+1
                #
                newRow = i-1
                newCol = j-2
                if canReach <2 and newRow in range(0,8) and newCol in range(0,8) and board[newRow][newCol]==0:
                    canReach = canReach+1
                #
                if canReach < 2:
                    return False
                else:
                    return True
#
# Function makeMove
#
def makeMove(i, j, k, board):
    newBoard = getEmptyBoard()
    if (board != None):
        #newBoard = list(board)
        # newBoard = copy.copy(board)
        for ii in range(8):
            for ji in range(8):
                newBoard[ii][ji] = board[ii][ji]
    newBoard[i][j] = k
    newBoard[8][0] = i
    newBoard[8][1] = j
    newBoard[8][2] = k
    #print ((i*8)+j+1, "Printed from makeMove Function")
    printBoard(newBoard)
    print("-")
    if canReachFrom2Squares(newBoard):
        return newBoard
#
# Function printBoard
#
def printBoard(singleBoardPosition):
        for i in range(8):
            for j in range(8):
                print("%3d" % (singleBoardPosition[i][j]), end="")
            print()
        print("===", singleBoardPosition[8][0], singleBoardPosition[8][1], singleBoardPosition[8][2])
#
# Function makeKnightMove
#
def moveKnightmove():
    tempBoard = []
    currentBoardPostion = list(boardPostions[len(boardPostions)-1])
    boardPostions.pop()
    #currentBoardPostion = []
    #
    # for loop1 in range(8):
    #     for loop2 in range(8):
    #         currentBoardPostion[loop1][loop2] = (boardPostions[len(boardPostions)-1])[loop1][loop2]
    row = currentBoardPostion[8][0]
    col = currentBoardPostion[8][1]
    moveNumber = currentBoardPostion[8][2]
    #
    # First possible moveNumber#
    #
    newRow = row+2
    newCol = col+1
    if (newRow >=0 and newRow<8 and newCol >= 0 and newCol<8):
        if currentBoardPostion[newRow][newCol] == 0: #means position is empty and knight can move
            tempBorad = makeMove(newRow, newCol, moveNumber+1, currentBoardPostion)
            if tempBoard != None:
                boardPostions.append(tempBorad)
                print("made move #1")
    newRow = row+2
    newCol = col-1
    if (newRow >=0 and newRow<8 and newCol >= 0 and newCol<8):
        if currentBoardPostion[newRow][newCol] == 0:
            tempBorad = makeMove(newRow, newCol, moveNumber+1, currentBoardPostion)
            if tempBoard != None:
                boardPostions.append(tempBorad)
                print("made move #2")

    if (newRow >=0 and newRow<8 and newCol >= 0 and newCol<8):
        if currentBoardPostion[newRow][newCol] == 0:
            tempBorad = makeMove(newRow, newCol, moveNumber+1, currentBoardPostion)
            if tempBoard != None:
                boardPostions.append(tempBorad)
                print("made move #3")
    newRow = row-2
    newCol = col-1
    if (newRow >=0 and newRow<8 and newCol >= 0 and newCol<8):
        if currentBoardPostion[newRow][newCol] == 0:
            tempBorad = makeMove(newRow, newCol, moveNumber+1, currentBoardPostion)
            if tempBoard != None:
                boardPostions.append(tempBorad)
                print("made move #4")
    newRow = row-1
    newCol = col+2
    if (newRow >=0 and newRow<8 and newCol >= 0 and newCol<8):
        if currentBoardPostion[newRow][newCol] == 0:
            tempBorad = makeMove(newRow, newCol, moveNumber+1, currentBoardPostion)
            if tempBoard != None:
                boardPostions.append(tempBorad)
                print("made move #5")
    newRow = row-1
    newCol = col-2
    if (newRow >=0 and newRow<8 and newCol >= 0 and newCol<8):
        if currentBoardPostion[newRow][newCol] == 0:
            tempBorad = makeMove(newRow, newCol, moveNumber+1, currentBoardPostion)
            if tempBoard != None:
                boardPostions.append(tempBorad)
                print("made move #6")
    newRow = row+1
    newCol = col+2
    if (newRow >=0 and newRow<8 and newCol >= 0 and newCol<8):
        if currentBoardPostion[newRow][newCol] == 0:
            tempBorad = makeMove(newRow, newCol, moveNumber+1, currentBoardPostion)
            if tempBoard != None:
                boardPostions.append(tempBorad)
                print("made move #7")
    newRow = row+1
    newCol = col-2
    if (newRow >=0 and newRow<8 and newCol >= 0 and newCol<8):
        if currentBoardPostion[newRow][newCol] == 0:
            tempBorad = makeMove(newRow, newCol, moveNumber+1, currentBoardPostion)
            if tempBoard != None:
                boardPostions.append(tempBorad)
                print("made move #8")
    return moveNumber+1

for i in range(8):
    for j in range(8):
        boardPostions.append(makeMove(i, j, 1, None))

printBoard(boardPostions[0])
printBoard(boardPostions[1])
printBoard(boardPostions[2])
printBoard(boardPostions[3])
printBoard(boardPostions[63])
#boardPostions[63] = boardPostions[1]
#printBoard(boardPostions[63])
print("Before making night move")
loop_count = 0
current_move = 1
while loop_count < 15000 and current_move < 63:
    print("")
    print("loop number", loop_count, "Number of boards", len(boardPostions))
    current_move = moveKnightmove()
    loop_count = loop_count+1
printBoard(boardPostions[len(boardPostions)-1])
printBoard(boardPostions[len(boardPostions)-2])
printBoard(boardPostions[len(boardPostions)-3])
printBoard(boardPostions[len(boardPostions)-4])
printBoard(boardPostions[len(boardPostions)-5])
printBoard(boardPostions[len(boardPostions)-6])
printBoard(boardPostions[len(boardPostions)-8])
