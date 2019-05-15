#!/usr/bin/env python3

'''
    The function counts the number of islands in a given 2D matrix.
    An island is defined as a group of adjacent values that are all 1s.
    A cell in binaryMatrix is considered adjacent to another cell if they are next to each either on the same row or column. Note that two values of 1 are not part of the same island if they’re sharing only a mutual “corner” (i.e. they are diagonally neighbors).
    Source: https://www.pramp.com/challenge/yZm60L6d5juM7K38KYZ6
'''

def get_number_of_islands(binaryMatrix):
    '''
    This function iterates over each element of the matrix to check if it's a 1
    if 1 is found it will send it over to another function for traversing
    Takes:
        - the target Matrix
    returns:
        - Total count of islands
    '''

    rows = len(binaryMatrix)
    col = len(binaryMatrix[0])
    r = 0
    count = 0
    for r in range(rows):
        for c in range(col):
          if binaryMatrix[r][c] == 1:
            binaryMatrix = traverse_nbrs(binaryMatrix, (r,c))
            count += 1
    return count

def traverse_nbrs(matrix, pos):
    '''
    This is a helper function that traverse nbrs of a given node
    if it was found to be 1
    Takes:
        - the matrix Itself
        - The position where the node where found
    returns:
        - a modified version of the matrix where
          all 1s belongs to this island has been eliminated
          to avoid being counted again
    '''

    r, c = pos
    matrix[r][c] = 0
    if c != 0:
        if matrix[r][c-1] == 1:
          matrix = traverse_nbrs(matrix, (r, c-1))
    if c != len(matrix[r])-1:
        if matrix[r][c+1] == 1:
          matrix = traverse_nbrs(matrix, (r, c+1))
    if r != 0:
        if matrix[r-1][c] == 1:
          matrix = traverse_nbrs(matrix, (r-1, c))
    if r != len(matrix)-1:
        if matrix[r+1][c] == 1:
          matrix = traverse_nbrs(matrix, (r+1, c))
    return matrix
