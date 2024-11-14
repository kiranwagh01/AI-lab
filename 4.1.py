def is_safe(board,row,col):
    for i in range(row):
        if board[i] == col or board[i]-i==col-row or board[i]+i == col +row:
            return False
    
    return True

def branch_and_bound(board,row,n,solution_found):
    if row==n:
        solution_found[0] = board.copy()
        return True
    
    for col in range(n):
        if is_safe(board,row,col):
            board[row]=col

            if branch_and_bound(board,row+1,n,solution_found):
                return True
            
    return False

def n_queen(n):
    board = [-1] * n

    solution_found = [None]
    branch_and_bound(board,0,n,solution_found)
    return solution_found[0]

def ps(solution):
    if solution:
        for row in solution:
            bl = ['Q' if i==row else '.' for i in range(len(solution))]
            print(' '.join(bl))
    else:
        print("No solution Found")

n=4
s=n_queen(n)
ps(s)   
