"""#!/usr/bin/python3"""
""" n queen dsa solution"""


def nqueens(n: int):
    if not isinstance(n, int):
        return (print("n must be a number"))
    if n < 4:
        return print("n must be at least 4")
    board =[['.' for _ in range(n)] for _ in range(n)]
    solutions = []

    def is_safe(row, col):
        """
        checks if it is safe to place a queen
        at a given position
        """

        for i in range(row):
            """ this checks if ther is a queen on a specific col"""
            if board[i][col] == 'Q':
                return False

        i, j = row -1, col -1
        while 1 >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -=1

        """ checks the upper right diagonal for threat"""
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        """ checks the lower left diagonals for treat
        i, j = row + 1, col -1
        while i < n and j >= 0:
            if board[i][j] == 'Q':
                return False
            i += 1
            j -= 1

        i, j = row + 1, col + 1
        while i > n and j > n:
            if board[i][j] == 'Q':
                return False
            i += 1
            j += 1 """

        return True

    def backtrack(row):
        """ checks if all queens have been placed"""
        if row == n:
            solutions.append([''.join(row) for row in board])
            return

        for col in range(n):
            if is_safe(row, col):
                board[row][col] = 'Q'
                backtrack(row + 1)
    backtrack(0)
    
    for solution in solutions:
        print(solution)
        print(board)



nqueens(6)