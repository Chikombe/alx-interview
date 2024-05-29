#!/usr/bin/env python3
"""
N Queens Problem: Solving for N Queens on an N×N chessboard
"""


def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen at board[row][col]
    """
    # Check this column on the upper side
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper diagonal on the right side
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens_util(board, row, N, solutions):
    """
    Utilizes backtracking to find all solutions
    """
    if row >= N:
        # A valid solution found, add it to the solutions list
        solution = []
        for i in range(N):
            row_solution = []
            for j in range(N):
                if board[i][j] == 1:
                    row_solution.append('Q')
                else:
                    row_solution.append('.')
            solution.append("".join(row_solution))
        solutions.append(solution)
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            # Place a queen
            board[row][col] = 1
            # Recur to place rest of the queens
            solve_n_queens_util(board, row + 1, N, solutions)
            # Backtrack and remove the queen from the current position
            board[row][col] = 0


def solve_n_queens(N):
    """
    Solves the N Queens problem and returns all solutions
    """
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_n_queens_util(board, 0, N, solutions)
    return solutions


if __name__ == "__main__":
    N = int(input("Enter the value of N: "))
    solutions = solve_n_queens(N)
    print(f"Number of solutions for {N} queens: {len(solutions)}")
    for solution in solutions:
        for row in solution:
            print(row)
        print()
