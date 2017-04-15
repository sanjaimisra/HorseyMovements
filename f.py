#import copy
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
def copyBoardElements(b1, b2):
    if b1==None:
        print("copyBoardElements, b1 is None")
    if b2==None:
        print("copyBoardElements, b2 is None")
    for cp1 in range(8):
        for cp2 in range(8):
            b1[cp1][cp2] = b2[cp1][cp2]
    b1[8][0] = b2[8][0]
    b1[8][1] = b2[8][1]
    b1[8][2] = b2[8][2]
#
# Function to check if board has an empty square that can not be reached from 2 or more squares
#
def canReachFrom2Squares(board):
    i = 0
    j = 0
    if board[8][2] >= 62:
        print("Return from top lie")
        return True
    print("checking unreacheable squares", i, j)

    for i in range(8):
        #print("inside for loop 1")
        for j in range(8):
            #print("inside for loop 2")
            canReach = 0;
            if board[i][j] == 0:
                print("Found empty postion at", i, j)
                #
                newRow = i+2
                newCol = j+1
                print ("checking 1", newRow, newCol)
                if canReach <2 and newRow in range(0,8) and newCol in range(0,8) and board[newRow][newCol]==0:
                    canReach = canReach+1
                    print("Can reach Number-1")
                #
                newRow = i+2
                newCol = j-1
                print ("checking 2", newRow, newCol)
                if canReach <2 and newRow in range(0,8) and newCol in range(0,8) and board[newRow][newCol]==0:
                    canReach = canReach+1
                    print("Can reach Number-2")
                #
                newRow = i-2
                newCol = j+1
                print ("checking 3", newRow, newCol)
                if canReach <2 and newRow in range(0,8) and newCol in range(0,8) and board[newRow][newCol]==0:
                    canReach = canReach+1
                    print("Can reach Number-3")
                #
                newRow = i-2
                newCol = j-1
                print ("checking 4", newRow, newCol)
                if canReach <2 and newRow in range(0,8) and newCol in range(0,8) and board[newRow][newCol]==0:
                    canReach = canReach+1
                    print("Can reach Number-4")
                #
                newRow = i+1
                newCol = j+2
                print ("checking 5", newRow, newCol)
                if canReach <2 and newRow in range(0,8) and newCol in range(0,8) and board[newRow][newCol]==0:
                    canReach = canReach+1
                    print("Can reach Number-5")
                #
                newRow = i+1
                newCol = j-2
                print ("checking 6", newRow, newCol)
                if canReach <2 and newRow in range(0,8) and newCol in range(0,8) and board[newRow][newCol]==0:
                    canReach = canReach+1
                    print("Can reach Number-6")
                #
                newRow = i-1
                newCol = j+2
                print ("checking 7", newRow, newCol)
                if canReach <2 and newRow in range(0,8) and newCol in range(0,8) and board[newRow][newCol]==0:
                    canReach = canReach+1
                    print("Can reach Number-7")
                #
                newRow = i-1
                newCol = j-2
                print ("checking 8", newRow, newCol)
                if canReach <2 and newRow in range(0,8) and newCol in range(0,8) and board[newRow][newCol]==0:
                    canReach = canReach+1
                    print("Can reach Number-8")
                #
                print("canReach value = ", canReach)
                if canReach < 2:
                    return False
                    print("all not reachable from two positions")
                #else:
                #    return True
                #    print("all reachable from two positions")
    return True
#
# Function makeMove
#
def makeMove(i, j, k, board):
    newBoard = getEmptyBoard()
    if (board != None):
        #newBoard = list(board)
        # newBoard = copy.copy(board)
        for mm1 in range(8):
            for mm2 in range(8):
                newBoard[mm1][mm2] = board[mm1][mm2]

    #print ((i*8)+j+1, "Printed from makeMove Function")

    print("- Calling canReachFrom2Squares")
    if canReachFrom2Squares(newBoard):
        newBoard[i][j] = k
        newBoard[8][0] = i
        newBoard[8][1] = j
        newBoard[8][2] = k
        printBoard(newBoard)
        return newBoard
    else:
        print("it will make board unreachable")
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
    if boardPostions[len(boardPostions)-1] == None:
        return 1
    tempBoard = []
    currentBoardPostion = getEmptyBoard()
    copyBoardElements(currentBoardPostion, boardPostions[len(boardPostions)-1])
    #currentBoardPostion = list(boardPostions[len(boardPostions)-1])
    print("Removing lasdt board")
    boardPostions.pop()
    print("number of board after deleting last one=", len(boardPostions))
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
            tempBoard = makeMove(newRow, newCol, moveNumber+1, currentBoardPostion)
            if not tempBoard:
                boardPostions.append(tempBoard)
                print("made move #1")
                printBoard(boardPostions[len(boardPostions)-1])
            else:
                print("List is fase????")
                if tempBoard == None:
                    print("list is None")
                else:
                    print("list is not NONE")
    newRow = row+2
    newCol = col-1
    if (newRow >=0 and newRow<8 and newCol >= 0 and newCol<8):
        if currentBoardPostion[newRow][newCol] == 0:
            tempBoard = makeMove(newRow, newCol, moveNumber+1, currentBoardPostion)
            if not tempBoard:
                boardPostions.append(tempBoard)
                print("made move #2")
                printBoard(boardPostions[len(boardPostions)-1])
            else:
                print("List is fase????")
                if tempBoard == None:
                    print("list is None")
                else:
                    print("list is not NONE")

    if (newRow >=0 and newRow<8 and newCol >= 0 and newCol<8):
        if currentBoardPostion[newRow][newCol] == 0:
            tempBoard = makeMove(newRow, newCol, moveNumber+1, currentBoardPostion)
            if not tempBoard:
                boardPostions.append(tempBoard)
                print("made move #3")
                printBoard(boardPostions[len(boardPostions)-1])
            else:
                print("List is fase????")
    newRow = row-2
    newCol = col-1
    if (newRow >=0 and newRow<8 and newCol >= 0 and newCol<8):
        if currentBoardPostion[newRow][newCol] == 0:
            tempBoard = makeMove(newRow, newCol, moveNumber+1, currentBoardPostion)
            if not tempBoard:
                boardPostions.append(tempBoard)
                print("made move #4")
                printBoard(boardPostions[len(boardPostions)-1])
            else:
                print("List is fase????")
                if tempBoard == None:
                    print("list is None")
                else:
                    print("list is not NONE")
    newRow = row-1
    newCol = col+2
    if (newRow >=0 and newRow<8 and newCol >= 0 and newCol<8):
        if currentBoardPostion[newRow][newCol] == 0:
            tempBoard = makeMove(newRow, newCol, moveNumber+1, currentBoardPostion)
            if not tempBoard:
                boardPostions.append(tempBoard)
                print("made move #5")
                printBoard(boardPostions[len(boardPostions)-1])
            else:
                print("List is fase????")
                if tempBoard == None:
                    print("list is None")
                else:
                    print("list is not NONE")
    newRow = row-1
    newCol = col-2
    if (newRow >=0 and newRow<8 and newCol >= 0 and newCol<8):
        if currentBoardPostion[newRow][newCol] == 0:
            tempBoard = makeMove(newRow, newCol, moveNumber+1, currentBoardPostion)
            if not tempBoard:
                boardPostions.append(tempBoard)
                print("made move #6")
                printBoard(boardPostions[len(boardPostions)-1])
            else:
                print("List is fase????")
                if tempBoard == None:
                    print("list is None")
                else:
                    print("list is not NONE")
    newRow = row+1
    newCol = col+2
    if (newRow >=0 and newRow<8 and newCol >= 0 and newCol<8):
        if currentBoardPostion[newRow][newCol] == 0:
            tempBoard = makeMove(newRow, newCol, moveNumber+1, currentBoardPostion)
            if not tempBoard:
                boardPostions.append(tempBoard)
                print("made move #7")
                printBoard(boardPostions[len(boardPostions)-1])
            else:
                print("List is fase????")
                if tempBoard == None:
                    print("list is None")
                else:
                    print("list is not NONE")
    newRow = row+1
    newCol = col-2
    if (newRow >=0 and newRow<8 and newCol >= 0 and newCol<8):
        if currentBoardPostion[newRow][newCol] == 0:
            tempBoard = makeMove(newRow, newCol, moveNumber+1, currentBoardPostion)
            if not tempBoard:
                boardPostions.append(tempBoard)
                print("made move #8")
                printBoard(boardPostions[len(boardPostions)-1])
            else:
                print("List is fase????")
                if tempBoard == None:
                    print("list is None")
                else:
                    print("list is not NONE")
    return moveNumber+1

for i in range(8):
    for j in range(8):
        boardPostions.append(makeMove(i, j, 1, None))

# printBoard(boardPostions[0])
# printBoard(boardPostions[1])
# printBoard(boardPostions[2])
# printBoard(boardPostions[3])
# printBoard(boardPostions[63])
#boardPostions[63] = boardPostions[1]
#printBoard(boardPostions[63])
print("Before making night move")
loop_count = 0
current_move = 1
while loop_count < 50000 and current_move < 63:
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
