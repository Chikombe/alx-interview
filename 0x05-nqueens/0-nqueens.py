#!/usr/bin/python3
"""A program that solves the N queens problem.

Determines all possible ways of placing N
non-attacking queens on an N×N chessboard.

N must be an integer greater or equal to 4.

Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.

Solutions are represented in the form of
[[row, col], [row, col], [row, col], [row, col].
A queen must be placed on the chessboard."""

import sys


def init_board(n):
    """Initialize an 'n' x 'n' sized chessboard with 0's."""
    board = []
    [board.append([]) for itr in range(n)]
    [row.append(' ') for itr in range(n) for row in board]
    return (board)


def board_deepcopy(board):
    """Return the deepcopy of a chessboard."""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)


def get_solution(board):
    """Returns the list of lists representation of a solved chessboard."""
    solution = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == "Q":
                solution.append([row, col])
                break
    return (solution)


def xout(board, current_row, column):
    """X out spots on a chessboard.

    All spots where non attacking queens can no longer be played are X-ed out.

    Arguments:
        board(int): The current working chessboard.
        current_row(int): The row where a queen was last played.
        column(int): The column where a queen was last played.
    """

    # X out all forward spots
    for col in range(column + 1, len(board)):
        board[current_row][col] = "x"
    # X out all backward spots
    for col in range(column - 1, -1, -1):
        board[current_row][col] = "x"
    # X out all spots below
    for row in range(current_row + 1, len(board)):
        board[row][column] = "x"
    # X out all spots above
    for row in range(current_row - 1, -1, -1):
        board[row][column] = "x"
    # X out all spots diagonally down to the right
    col = column + 1
    for row in range(current_row + 1, len(board)):
        if col >= len(board):
            break
        board[row][col] = "x"
        col += 1
    # X out all spots diagnally up to the left
    col = column - 1
    for row in range(current_row - 1, -1, -1):
        if col < 0:
            break
        board[row][col]
        col -= 1
    # X out all spots diagonally up to the right
    col = column + 1
    for row in range(current_row - 1, -1, -1):
        if col >= len(board):
            break
        board[row][col] = "x"
        col += 1
    # X out all spots diagonally down to the left
    col = column - 1
    for row in range(current_row + 1, len(board)):
        if col < 0:
            break
        board[row][col] = "x"
        col -= 1


def recursive_solve(board, current_row, queens, solutions):
    """Recursively solve an N-queens puzzle.

    Arguments:
        board(list): The current working chessboard.
        current_row(int): The current working row.
        queen(int): The current number of placed queens.
        solutions(list): A list of lists solutions
    Returns:
        solutions"""

    if queens == len(board):
        solutions.append(get_solution(board))
        return (solutions)

    for col in range(len(board)):
        if board[current_row][col] == " ":
            temp_board = board_deepcopy(board)
            temp_board[current_row][col] = "Q"
            xout(temp_board, current_row, col)
            solutions = recursive_solve(temp_board, current_row + 1,
                                        queens + 1, solutions)
    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print([[row, col] for row, col in sol])
