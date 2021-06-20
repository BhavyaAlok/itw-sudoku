

import pygame
import ctypes
from random import shuffle, randint
from pprint import pprint

sudokuGrid = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],

Expand
final_sudoku.py8 KB
﻿

import pygame
import ctypes
from random import shuffle, randint
from pprint import pprint

sudokuGrid = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]


def completeCheck(sudokuGrid):
    for row in range(0, 9):
        for col in range(0, 9):
            if sudokuGrid[row][col] == 0:
                return False
    return True


ordNumList = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def fillsudokuGrid(sudokuGrid):
    # Find next empty cell
    for i in range(0, 81):
        row = i // 9  # 76 > 76//9 == 8 (stays same)
        col = i % 9  # 76> 76%9 == 4 then goes to 5 then 6 then 7 then 8...
        if sudokuGrid[row][col] == 0:
            shuffle(ordNumList)
            for value in ordNumList:
                # Check that this value has not already be used on this row
                if not (value in sudokuGrid[row]):
                    # Check that this value has not already be used on this column
                    if not value in (
                            sudokuGrid[0][col], sudokuGrid[1][col], sudokuGrid[2][col], sudokuGrid[3][col],
                            sudokuGrid[4][col], sudokuGrid[5][col], sudokuGrid[6][col],
                            sudokuGrid[7][col], sudokuGrid[8][col]):
                        # Identify which of the 9 squares we are working on
                        square = []
                        if row < 3:
                            if col < 3:
                                square = [sudokuGrid[i][0:3] for i in range(0, 3)]
                            elif col < 6:
                                square = [sudokuGrid[i][3:6] for i in range(0, 3)]
                            else:
                                square = [sudokuGrid[i][6:9] for i in range(0, 3)]
                        elif row < 6:
                            if col < 3:
                                square = [sudokuGrid[i][0:3] for i in range(3, 6)]
                            elif col < 6:
                                square = [sudokuGrid[i][3:6] for i in range(3, 6)]
                            else:
                                square = [sudokuGrid[i][6:9] for i in range(3, 6)]
                        else:
                            if col < 3:
                                square = [sudokuGrid[i][0:3] for i in range(6, 9)]
                            elif col < 6:
                                square = [sudokuGrid[i][3:6] for i in range(6, 9)]
                            else:
                                square = [sudokuGrid[i][6:9] for i in range(6, 9)]
                        # Check that this value has not already be used on this 3x3 square
                        if not value in (square[0] + square[1] + square[2]):
                            sudokuGrid[row][col] = value
                            if completeCheck(sudokuGrid):
                                return True
                            else:
                                if fillsudokuGrid(sudokuGrid):
                                    return True
            break
    sudokuGrid[row][col] = 0


# Generate a Fully Solved sudokuGrid
fillsudokuGrid(sudokuGrid)
pprint(sudokuGrid)

grid = [i.copy() for i in sudokuGrid]


def removek(k):
    while k:
        row = randint(0, 8)
        col = randint(0, 8)
        if grid[row][col] != 0:
            grid[row][col] = 0
        k = k - 1


removek(10)

WIDTH = 550
HEIGHT = 700
background_color = (255, 255, 255)
original_grid_element_color = (52,31,151)
buffer = 5

grid_original = [[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))]



