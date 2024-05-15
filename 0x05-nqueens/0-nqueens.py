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
        if (board[i] == col or board[i] - i == col - row
                or board[i] + i == col + row):
            return False
    return True


def solve_n_queens(N):
    """
    solves the n queens
    """
    if N < 4:
        print("N must be at least 4", file=sys.stderr)
        sys.exit(1)
    if not isinstance(N, int):
        print("N must be a number", file=sys.stderr)
        sys.exit(1)
    if len(sys.argv) != 2:
        print("Usage: nqueens N", file=sys.stderr)
        sys.exit(1)

    def solve(row):
        """
        solves work
        """
        if row == N:
            print(board)
            return
        for col in range(N):
            if is_safe(board, row, col, N):
                board[row] = col
                solve(row + 1)
    board = [-1] * N
    solve(0)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        try:
            N = int(sys.argv[1])
            solve_n_queens(N)
        except ValueError:
            print("N must be a number", file=sys.stderr)
            sys.exit(1)
