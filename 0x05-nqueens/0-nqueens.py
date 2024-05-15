#!/usr/bin/python3
"""
script for task 0
"""
import sys


def is_safe(board, row, col, N):
    """
    check if is safe
    """
    for i in range(row):
        if (board[i][col] == 1):
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False
    return True


def solve(board, row, N, solutions):
    """
    solves work
    """
    if row == N:
        solutions.append([[i, j] for i in range(N) for j in range(N)
                         if board[i][j] == 1])
        return
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solve(board, row + 1, N, solutions)
            board[row][col] = 0


def solve_n_queens(N):
    """
    solves the n queens
    """
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve(board, 0, N, solutions)
    for s in solutions:
        print(s)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
        solve_n_queens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
