testBoard = [
    [0,0,0,2,6,0,7,0,1],
    [6,8,0,0,7,0,0,9,0],
    [1,9,0,0,0,4,5,0,0],
    [8,2,0,1,0,0,0,4,0],
    [0,0,4,6,0,2,9,0,0],
    [0,5,0,0,0,3,0,2,8],
    [0,0,9,3,0,0,0,7,4],
    [0,4,0,0,5,0,0,3,6],
    [7,0,3,0,1,8,0,0,0]
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
                return (i,j)
            
    return None #had this in an else statment which caused the solve function to return true right away if the first number in board wasnt 0. 
                #Now it returns None only if there are no 0's after going through the whole i range/index/for loop
    

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

def solve(board):
    find = findEmpty(board)
    if not find:
        return True
    else:
        row,col = find
    #The meat and potatoes of this recursive program. Basically it checks if the range value is valid, if it is it inserts the value, and the executes the next line which calls solve board on the new board.
    #So now you've entered the world of this board and solve is running on it.Then lets say it finds no values in the range 1-9 that can work or be valid it then returns false and the id solve statement is skipped
    #Instead the board[row][col] = 0 section is executed, where the element in that position is set to 0 again, and the the range continous and tries to see if the next number will valid, and if it is then we continue 
    #The function and trie the if solve statment again by enterring the world of this new baord with the new Valid value. Lets say we keep trying and there are no Valid values again. Then we  peel back a layer/world/board
    #And we up the index/range and try with the next available Valid value
    for i in range(1,10):
        if(isValid(board,i,(row,col))):
            board[row][col] = i #had this as == insead of = i which caused "RecursionError: maximum recursion depth exceeded in comparison" Error
            
            if solve(board):
                return True
            board[row][col] = 0
            
    return False


printBoard(testBoard)
solve(testBoard)
print("---------------------------")
printBoard(testBoard)
    

