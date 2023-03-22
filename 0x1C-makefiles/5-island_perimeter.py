#!/usr/bin/python3

"""
    contains island_perimeter
"""


def island_perimeter(grid):
    """
        computes the perimeter of an 'island' in a grid
        0 represents water zone
        1 represents land zone
        one cell in the grid represents a square piece of land of length 1
    """
    tile_perimeter = 4
    total_permimeter = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                total_permimeter += tile_perimeter
                borders = get_borders(col, row, grid)
                total_permimeter -= borders
    return total_permimeter


def get_borders(col, row, grid):
    """
        returns the border of a cell with it's neighboring cells
    """
    vertical_borders = 0
    horizontal_borders = 0
    if (row - 1) >= 0:
        if grid[row - 1][col]:
            vertical_borders += 1
    if (row + 1) < len(grid):
        if grid[row + 1][col]:
            vertical_borders += 1
    if (col - 1) >= 0:
        if grid[row][col - 1]:
            horizontal_borders += 1
    if (col + 1) < len(grid[row]):
        if grid[row][col + 1]:
            horizontal_borders += 1
    return vertical_borders + horizontal_borders

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
