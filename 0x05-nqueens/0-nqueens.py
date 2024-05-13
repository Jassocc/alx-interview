#!/usr/bin/python3
"""
script for task 0
"""
import sys


def is_safe(board, row, col, n):
    """
    check if is safe
    """
    for i in range(row):
        if (board[i] == col or board[i] - i == col - row or
            board[i] + i == col + row):
            return False
    return True

def solve_n_queens(board, row, n):
    """
    solves the n queens
    """
    if row == n:
        print([[i, board[i]] for i in range(n)])
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_n_queens(board, row + 1, n)

def main():
    """
    main function
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N", file=sys.stderr)
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number", file=sys.stderr)
        sys.exit(1)
    if n < 4:
        print("N must be at least 4", file=sys.stderr)
        sys.exit(1)
    solve_n_queens([-1] * n, 0, n)


if __name__ == "__main__":
    main()
