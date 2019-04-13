def sudoku_solve(board):
    for r in range(9):
        for c in range(9):
            if not board[r][c]:
                value = getP(board, r, c)
                if value:
                    for v in value:
                        board[r][c] = v
                        if sudoku_solve(board):
                            return True
                    board[r][c] = 0
                    return False
                return False
    print(board)
    return True


def getP(board, row, col):
    row_pos = set()
    col_list = set()
    for r in range(9):
        col_list.add(board[r][col])
    for chr in range(1,10):
        if not (chr in board[row] or chr in col_list):
            row_pos.add(chr)
    return row_pos

# def intersection(arr, carr):
#   inter = []
#   for item in arr:
#     if item in carr:
#       inter.append(item)
#   return inter

def replace_int(matrix):
  for r in range(9):
    for c in range(9):
      if not matrix[r][c] == ".":
        matrix[r][c] = int(matrix[r][c])
      else:
        matrix[r][c] = 0
  return matrix



board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

board = replace_int(board)
print(sudoku_solve(board))

board = [
  [".","8","9",".","4",".","6",".","5"],
  [".","7",".",".",".","8",".","4","1"],
  ["5","6",".","9",".",".",".",".","8"],
  [".",".",".","7",".","5",".","9","."],
  [".","9",".","4",".","1",".","5","."],
  [".","3",".","9",".","6",".","1","."],
  ["8",".",".",".",".",".",".",".","7"],
  [".","2",".","8",".",".",".","6","."],
  [".",".","6",".","7",".",".","8","."]]

board = replace_int(board)
print(sudoku_solve(board))


#  row_pos = everything except what is in the row
#  col_pos = everything except what is in the col board[0-8][col]

#

#[
#  ["5","3",".",".","7",".",".",".","."],
#  ["6",".",".","1","9","5",".",".","."],
#  [".","9","8",".",".",".",".","6","."],
#  ["8",".",".",".","6",".",".",".","3"],
#  ["4",".",".","8",".","3",".",".","1"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".","6",".",".",".",".","2","8","."],
#  [".",".",".","4","1","9",".",".","5"],
#  [".",".",".",".","8",".",".","7","9"]
#]

# 1. Each row has no rep. [1-9]
# 2. Each col has no rep [1-9]
# 3. subboard has no rep [1-9]

# 1 2 4 6 9

# 1 . 3       1 . 3       1 2 3
# 3 . 4    => 3 5 6 =>    3 5 6
# 2 . 8       2 . 8       2 7 8
