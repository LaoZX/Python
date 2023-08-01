# Check if it is safe to place a queen at board[row][col]
def is_safe(board, row, col):

    # Check left side of the current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal on the left side
    i, j = row, col
    while i < 8 and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_n_queens(board, col, solutions):
    # when all queens have been, one solution found
    if col >= 8:
        solutions.append([row[:] for row in board])
        return

    # Try placing a queen in each row of the current column
    for i in range(8):
        if is_safe(board, i, col):
            # Place the queen on the board
            board[i][col] = 1

            # Recur for the next column
            solve_n_queens(board, col + 1, solutions)

            # Backtrack and remove the queen from the board
            board[i][col] = 0


def solve_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]

    # solution list
    solutions = []

    solve_n_queens(board, 0, solutions)

    # Print the number of solutions
    print("Number of solutions:", len(solutions))

    # Print each solution
    for i, solution in enumerate(solutions):
        print(f"Solution {i+1}:")
        for row in solution:
            print(" ".join(["1" if cell == 1 
                            else "0" for cell in row]))
        print()

solve_queens(8)