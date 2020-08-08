board = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]
def check(board,row,column):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] ==1:
                if abs(i-row) == abs(j-column) or i == row or j==column:
                    return False
    return True

def print_board(board):
    for row in board:
        print(row)
    print()

def arrange(board,row=0):
    if row == len(board):
        print_board(board)
    if row < len(board):
        for col in range(len(board[row])):
            if check(board,row,col):
                board[row][col]=1
                arrange(board,row+1)
                board[row][col]=0
        
arrange(board)

