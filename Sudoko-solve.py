#!/usr/bin/env python3

'''
    The function determines if a given sudoko solvable or not
    The sudoko is checked by checking every single possibility in each empty node
    then passing on to the next empty element and so forth
    Source: https://www.pramp.com/challenge/O5PGrqGEyKtq9wpgw6XP
'''

def sudoku_solve(board, r=0):
    ''' Iterate over each row to find the empty slots
        then plug in every single possibility and send it over to see
        if it's solvable
        Takes:
            - the sudoko board
            - the current positional row (Default 0 for first iteration)
        Returns:
            - true if solvable
            - false otherwise
    '''
    if 0 in board[r]:
        c = board[r].index(0)
        value = getP(board, r, c)
        if value:
            for v in value:
                board[r][c] = v
                if sudoku_solve(board, r):
                    return True
            board[r][c] = 0
            return False
        return False
    elif r < len(board)-1:
            return sudoku_solve(board, r+1)
    print(board)
    return True


def getP(board, row, col):
    ''' Helper function to get all possibile values for a certain slot
        it does that by comparing all possible values to the existing ones
        in the same row and col
        Takes:
            - the sudoko board
            - the position of the subject element in row and col
        Returns:
            - a set of all possible values
    '''
    all_pos = set(range(1,10))
    row_pos = set()
    col_list = set()
    subboard = getSubboard(board, (row, col))
    for r in range(9):
        col_list.add(board[r][col])
    row_pos = all_pos - set(board[row]) - col_list - subboard
    return row_pos

def replace_int(matrix):
    ''' Just for better efficiency. replace all strings to integers in the input'''
    for r in range(9):
        for c in range(9):
          if not matrix[r][c] == ".":
            matrix[r][c] = int(matrix[r][c])
          else:
            matrix[r][c] = 0
    return matrix

def getSubboard(board, vertix, visited=set()):
    '''
        Helper function to get all the values in a given subboard for
        possibilities calculations. It basically builds a graph structure
        for the subboard based on the subject position and then it does a
        BSF to get all the values in the graph
        Takes:
            - The board values
            - The positin of the test subject
            - a set of all visited nodes in the graph
        Returns:
            - a set of all the values in the given subboard
    '''
    visited.add(vertix)
    adj = {1:[1], 2:[-1,1], 0:[-1]}
    r, c = vertix
    subboard = set()
    r_pos, c_pos = ((r+1) % 3), ((c+1) % 3)
    r_oper, c_oper = adj[r_pos], adj[c_pos]
    edges = []
    for v in r_oper:
        next_r = r + v
        edges.append((next_r, c))
    for v in c_oper:
        next_c = c + v
        edges.append((r, next_c))
    for edge in edges:
        i, j = edge[0], edge[1]
        subboard.add(board[i][j])
    for edge in edges:
        if edge not in visited:
            subboard.union(getSubboard(board, edge, visited))
    return subboard



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
