def solve_n_queens(n):
    board=[-1]*n
    solutions=[]
    
    def is_safe(row,col):
        for r in range(row):
            c=board[r]
            if c==col or abs(c-col)==abs(r-row):
                return False
        return True
        
    def backtrack(row):
        if row==n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(row,col):
                board[row]=col
                backtrack(row+1)
                board[row]=-1
                
    backtrack(0)
    return solutions

solutions=solve_n_queens(8)
print(f"Total solutions for 8-Queens: {len(solutions)}")
print("First solution (column position per row):",solutions[0])