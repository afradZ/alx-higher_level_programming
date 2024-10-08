#!/usr/bin/python3
import sys

def is_safe(board, row, col):

    """
    Check if it's safe to place a queen at board[row][col].
    This function checks the column and both diagonals.
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(N, row, board, solutions):

    """
    Solve the N queens problem using backtracking.
    """
    if row == N:
        solutions.append([[i, board[i]] for i in range(N)])
        return
    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(N, row + 1, board, solutions)
            # Backtrack here

def nqueens(N):

    """
    Solves the N queens puzzle and prints all solutions.
    """
    board = [-1] * N
    solutions = []
    solve_nqueens(N, 0, board, solutions)
    for solution in solutions:
        print(solution)

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(N)
