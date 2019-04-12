#!/usr/bin/env python3

'''
    The function determines the shortest path between two given cells in a grid.
    The distance is counted by the number of cells with value 1 in between
    The function returns the shortest path or -1 if there is no path to the target
    Source: https://www.pramp.com/challenge/Y56aZmaj9Ptmd9wV9xvL
'''

def shortestCellPath(grid, sr, sc, tr, tc):
    ''' Starer function reads input and send over the starting point for traversing
        Takes:
            - The grid
            - the source row and col position
            - the target row and col position
        Return:
            - The shortest distance
            - Or -1 if impossible
    '''

    dist = 0
    r, c = sr, sc
    flag, dist = traverse_nbrs(grid, r, c, tr, tc, dist)
    return dist


def traverse_nbrs(matrix, r, c, tr, tc, dist):
    ''' Helper function that traverse the nbrs of a given node as to the adjacent
        nbrs of value 1. For each 1 hop the distance will be incremented
        Takes:
            - the grid without the previous hop
            - the current position
            - the target position
            - the calculated distance so far
        returns: (a tuple consists of a flag and an int no.)
            - a true flag if the target position was reached
            - a false flag otherwise
            - the shortest path from any given node to the target if found
            - -1 otherwise
    '''

    dist += 1
    dist_list = []
    cur_pos = (r, c)
    tar_pos = (tr, tc)
    new_dist = 0

    if cur_pos == tar_pos:
        return True, dist-1

    matrix[r][c] = 0


    if c != len(matrix[0])-1:
        if matrix[r][c+1] == 1:
          flag, new_dist = traverse_nbrs(matrix, r, c+1, tr, tc, dist)
          if flag:
            dist_list.append(new_dist)
    if c != 0:
        if matrix[r][c-1] == 1:
          flag, new_dist = traverse_nbrs(matrix, r, c-1, tr, tc, dist)
          if flag:
            dist_list.append(new_dist)
    if r != len(matrix)-1:
        if matrix[r+1][c] == 1:
          flag, new_dist = traverse_nbrs(matrix, r+1, c, tr, tc, dist)
          if flag:
            dist_list.append(new_dist)
    if r != 0:
        if matrix[r-1][c] == 1:
          flag, new_dist = traverse_nbrs(matrix, r-1, c, tr, tc, dist)
          if flag:
            dist_list.append(new_dist)
    if dist_list:
        return True, min(dist_list)
    return False, -1


def main():
  grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 1]]
  sr = 0
  sc = 0
  tr = 2
  tc = 0
  print(shortestCellPath(grid, sr, sc, tr, tc))

if __name__ == '__main__':
  main()
