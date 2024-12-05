# This problem was asked by Google.

# You are given a 2D matrix of 1s and 0s where 1 represents land and 0 represents water.

# Grid cells are connected horizontally orvertically (not diagonally). 
# The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# An island is a group is cells connected horizontally or vertically, but not diagonally. 
# There is guaranteed to be exactly one island in this grid, and the island doesn't have water inside that isn't connected to the water around the island. 
# Each cell has a side length of 1.

# Determine the perimeter of this island.

# For example, given the following matrix:

[[0, 1, 1, 0],
[1, 1, 1, 0],
[0, 1, 1, 0],
[0, 0, 1, 0]]
# Return 14.

## Solution ##

# When counting the perimeter of an island here, notice that a straightforward way to check whether an edge should be counted as part of the perimeter is whether it is adjacent to another land cell. 
# If there's a land cell adjacent to that edge, then it shouldn't count as the perimeter. 
# If it's a water cell or an edge, then it should count as the perimeter.

# This leads us to the following algorithm to compute the perimeter:
# 1) Iterate over every cell in the board 
# 2) Count the number of neighbouring land cells 
# 3) Add 4 - num_land_cells to the perimeter count

def get_num_neighbours(board, r, c):
    num = 0
    if r > 0:
        num += board[r-1][c] == 1
    
    if r < len(board) - 1:
        num += board[r+1][c] == 1
    
    if c > 0:
        num += board[r][c-1] == 1
    
    if c < len(board[0]) - 1:
        num += board[r][c+1] == 1
    
    return num


def island_perimeter(board):
    perimeter = 0
    for r, row in enumerate(board):
        for c, val in enumerate(row):
            if val == 1:
                perimeter += 4 - get_num_neighbours(board, r, c)
    return perimeter

# This runs in O(M N) time and constant space, since computing neighbours is constant time and we iterate over every cell on the N M board.
