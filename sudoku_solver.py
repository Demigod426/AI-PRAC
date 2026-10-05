def find_empty(board):
    for r in range(9):
        for c in range(9):
            if board[r][c]==0:
                return r,c
    return None

def valid(board,num,pos):
    r,c=pos
    if num in board[r]:
        return False
    if num in [board[i][c] for i in range(9)]:
        return False
    box_r,box_c=3*(r//3),3*(c//3)
    for i in range(box_r,box_r+3):
        for j in range(box_c,box_c+3):
            if board[i][j]==num:
                return False
    return True

def solve(board):
    empty=find_empty(board)
    if not empty:
        return True
    r,c=empty
    for num in range(1,10):
        if valid(board,num,(r,c)):
            board[r][c]=num
            if solve(board):
                return True
            board[r][c]=0
    return False

board=[
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

if solve(board):
    for row in board:
        print(row)
else:
    print("No solution exists")