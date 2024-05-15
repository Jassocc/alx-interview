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


def solve_n_queens(board, row, N):
    """
    solves the n queens
    """
    if row == N:
        print([[i, board[i]] for i in range(N)])
        return
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            solve_n_queens(board, row + 1, N)


def main():
    """
    main function
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N", file=sys.stderr)
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number", file=sys.stderr)
        sys.exit(1)
    if N < 4:
        print("N must be at least 4", file=sys.stderr)
        sys.exit(1)
    solve_n_queens([-1] * N, 0, N)


if __name__ == "__main__":
    main()
