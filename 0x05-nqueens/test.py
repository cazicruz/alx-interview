def is_safe(board, row, col, N):
    # Check if a queen can be placed at board[row][col]
    
    # Check row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal on the left side
    i = row
    j = col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

def solve_n_queens_util(board, col, N):
    # Base case: If all queens are placed, return True
    if col >= N:
        return True

    # Consider this column and try placing a queen in each row one by one
    for i in range(N):
        if is_safe(board, i, col, N):
            # Place the queen in board[i][col]
            board[i][col] = 1

            # Recur to place the rest of the queens
            if solve_n_queens_util(board, col + 1, N):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution, backtrack
            board[i][col] = 0

    # If the queen cannot be placed in any row of this column, return False
    return False

def solve_n_queens(N):
    # Create an NxN chessboard
    board = [[0] * N for _ in range(N)]

    # Solve the N-Queens problem
    if solve_n_queens_util(board, 0, N):
        # Print the solution
        for row in board:
            print(' '.join(map(str, row)))
    else:
        print("No solution exists.")

# Test the function with N = 4
solve_n_queens(6)
