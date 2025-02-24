# import copy
boardPostions = []


def getEmptyBoard():
    """Get empty board."""
    emptyBoard = [[0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0]]
    return emptyBoard


def copyBoardElements(b1, b2):
    """Copy board elements."""
    if b1 is None:
        print("copyBoardElements, b1 is None")
    if b2 is None:
        print("copyBoardElements, b2 is None")
    for cp1 in range(8):
        for cp2 in range(8):
            b1[cp1][cp2] = b2[cp1][cp2]
    b1[8][0] = b2[8][0]
    b1[8][1] = b2[8][1]
    b1[8][2] = b2[8][2]


def canReachFrom2Squares(board):
    """Check if all empty postions can be reached from two other positions."""
    #
    # Function to check if board has an empty square that can not be reached from 2 or more squares
    #
    i = 0
    j = 0
    totalCannotReach = 0
    if board[8][2] >= 62:
        print("Return from top line")
        return True
    # print("checking unreacheable squares", i, j)

    for i in range(8):
        # print("inside for loop 1")
        for j in range(8):
            # print("inside for loop 2")
            canReach = 0
            if board[i][j] == 0:
                # print("Found empty postion at", i, j)
                #
                newRow = i+2
                newCol = j+1
                # print ("checking 1", newRow, newCol)
                if canReach < 2 and newRow in range(0, 8) and newCol in range(0, 8) and board[newRow][newCol] == 0:
                    canReach = canReach+1
                    # print("Can reach Number-1")
                #
                newRow = i+2
                newCol = j-1
                # print ("checking 2", newRow, newCol)
                if canReach < 2 and newRow in range(0, 8) and newCol in range(0, 8) and board[newRow][newCol] == 0:
                    canReach = canReach+1
                    # print("Can reach Number-2")
                #
                newRow = i-2
                newCol = j+1
                # print ("checking 3", newRow, newCol)
                if canReach < 2 and newRow in range(0, 8) and newCol in range(0, 8) and board[newRow][newCol] == 0:
                    canReach = canReach+1
                #     print("Can reach Number-3")
                #
                newRow = i-2
                newCol = j-1
                # print("checking 4", newRow, newCol)
                if canReach < 2 and newRow in range(0, 8) and newCol in range(0, 8) and board[newRow][newCol] == 0:
                    canReach = canReach+1
                    # print("Can reach Number-4")
                #
                newRow = i+1
                newCol = j+2
                # print("checking 5", newRow, newCol)
                if canReach < 2 and newRow in range(0, 8) and newCol in range(0, 8) and board[newRow][newCol] == 0:
                    canReach = canReach+1
                    # print("Can reach Number-5")
                #
                newRow = i+1
                newCol = j-2
                # print("checking 6", newRow, newCol)
                if canReach < 2 and newRow in range(0, 8) and newCol in range(0, 8) and board[newRow][newCol] == 0:
                    canReach = canReach+1
                    # print("Can reach Number-6")
                #
                newRow = i-1
                newCol = j+2
                # print("checking 7", newRow, newCol)
                if canReach < 2 and newRow in range(0, 8) and newCol in range(0, 8) and board[newRow][newCol] == 0:
                    canReach = canReach+1
                    # print("Can reach Number-7")
                #
                newRow = i-1
                newCol = j-2
                # print("checking 8", newRow, newCol)
                if canReach < 2 and newRow in range(0, 8) and newCol in range(0, 8) and board[newRow][newCol] == 0:
                    canReach = canReach+1
                    # print("Can reach Number-8")
                #
                # print("canReach value = ", canReach)
                if canReach < 2:
                    totalCannotReach = totalCannotReach+1
                    if totalCannotReach > 1:
                        # print("all not reachable from two positions", i, j)
                        # printBoard(board)
                        return False
                # else:
                #    return True
                #    print("all reachable from two positions")
    return True
#
# Function makeMove
#


def makeMove(i, j, k, board):
    """Make knight move onthe board."""
    newBoard = getEmptyBoard()
    if board is not None:
        # newBoard = list(board)
        # newBoard = copy.copy(board)
        for mm1 in range(8):
            for mm2 in range(8):
                newBoard[mm1][mm2] = board[mm1][mm2]

    # print ((i*8)+j+1, "Printed from makeMove Function")

    # print("- Calling canReachFrom2Squares")
    if board is None or canReachFrom2Squares(newBoard):
        newBoard[i][j] = k
        newBoard[8][0] = i
        newBoard[8][1] = j
        newBoard[8][2] = k
        printBoard(newBoard)
        return newBoard
    # else:
    #     print("it will make board unreachable if knight move to ", i, j, "for move number=", k)
#
# Function printBoard
#


def printBoard(singleBoardPosition):
    """Print board postions."""
    for i in range(8):
        for j in range(8):
            print("%3d" % (singleBoardPosition[i][j]), end="")
        print()
    print("===", singleBoardPosition[8][0], singleBoardPosition[8][1], singleBoardPosition[8][2])
#
# Function makeKnightMove
#


def makeSignleMove(pRow, pCol, pMoveNumber, pCurrentBoard):
    """Make single move on board."""
    if (pRow >= 0 and pRow < 8 and pCol >= 0 and pCol < 8):
        if pCurrentBoard[pRow][pCol] == 0:
            tempBoard = makeMove(pRow, pCol, pMoveNumber+1, pCurrentBoard)
            if tempBoard:
                boardPostions.append(tempBoard)
                # printBoard(boardPostions[len(boardPostions)-1])
            # else:
            #     print("List is false????")
            #     if tempBoard is None:
            #         print("list is None")
            #     else:
            #         print("list is not NONE")


def makeKnightmove():
    """Make knight move."""
    if boardPostions[len(boardPostions)-1] is None:
        return 1

    currentBoardPostion = getEmptyBoard()
    copyBoardElements(currentBoardPostion, boardPostions[len(boardPostions)-1])
    # print("Removing last board")
    boardPostions.pop()
    row = currentBoardPostion[8][0]
    col = currentBoardPostion[8][1]
    moveNumber = currentBoardPostion[8][2]
    #
    # First possible moveNumber#
    #
    newRow = row+2
    newCol = col+1
    makeSignleMove(newRow, newCol, moveNumber, currentBoardPostion)

    newRow = row+2
    newCol = col-1
    makeSignleMove(newRow, newCol, moveNumber, currentBoardPostion)

    newRow = row-2
    newCol = col+1
    makeSignleMove(newRow, newCol, moveNumber, currentBoardPostion)

    newRow = row-2
    newCol = col-1
    makeSignleMove(newRow, newCol, moveNumber, currentBoardPostion)

    newRow = row-1
    newCol = col+2
    makeSignleMove(newRow, newCol, moveNumber, currentBoardPostion)

    newRow = row-1
    newCol = col-2
    makeSignleMove(newRow, newCol, moveNumber, currentBoardPostion)

    newRow = row+1
    newCol = col+2
    makeSignleMove(newRow, newCol, moveNumber, currentBoardPostion)

    newRow = row+1
    newCol = col-2
    makeSignleMove(newRow, newCol, moveNumber, currentBoardPostion)

    return moveNumber+1


for i in range(8):
    for j in range(8):
        boardPostions.append(makeMove(i, j, 1, None))

print("Before making night move")
loop_count = 0
current_move = 1
while loop_count < 1000000 and current_move < 63:
    print("")
    print("loop number", loop_count, "Number of boards", len(boardPostions))
    current_move = makeKnightmove()
    loop_count = loop_count+1
