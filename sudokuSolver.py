testBoard = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


def printBoard(board):
    for i in range(len(board)):
        if i % 3 == 0 and i!= 0:
            print("- - - - - - - - - - ")
        for j in range(len(board[i])):
            if j % 3 == 0 and j!= 0:
                print("|", end="")
            if j == 8:
                print(str(board[i][j]))
            else:
                print(str(board[i][j]),"",end="")
def findEmpty(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return board[i][j]
            else: 
                return None

def isValid(board,num,pos):
    row = pos[0]
    column = pos[1]
    grid_row = pos[0]//3
    grid_column = pos[1]//3
    for i in range(len(board[0])): 
        #check row
        if board[row][i] == num and i != column:
            return False
        
        #check column
        if board[i][column] == num and i != row:
            return False
        #check grid(Simple algorithm for multiplying by 3 then adding 3 to get to original element and stay in range of the square  through the x and y corodonates)
        for i in range(grid_row * 3, grid_row * 3 + 3):
            for j in range(grid_column * 3, grid_column * 3 +3):
                if board[i][j] == num and (i,j) != pos:
                    return False
    return True


printBoard(testBoard)
print(isValid(testBoard,3,(1,5)))
henok = findEmpty(testBoard)
    

