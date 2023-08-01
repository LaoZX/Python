def PutQueen(row):
    global n, column, leftDiag, rightDiag, positionInRow

    for col in range(n):
        if column[col] and leftDiag[row + col] and rightDiag[row - col + n - 1]:
            positionInRow[row] = col
            column[col] = False
            leftDiag[row + col] = False
            rightDiag[row - col + n - 1] = False

            if row < n - 1:
                PutQueen(row + 1)
            else:
                print("Solution found")

            column[col] = True
            leftDiag[row + col] = True
            rightDiag[row - col + n - 1] = True

# Example usage:
n = 8  # Set the desired board size
column = [True] * n
leftDiag = [True] * (2 * n - 1)
rightDiag = [True] * (2 * n - 1)
positionInRow = [-1] * n

PutQueen(0)
