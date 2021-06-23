import pygame
import ctypes  # for pop-up window
from random import shuffle, randint  # for shuffling and generating random iterger
from pprint import pprint  # to print girid in terminal from 1-D array to 2-D array

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


defaultLevel = 1
level = defaultLevel


def levelSelect(level):
    if level == 1:
        removek(3)
    elif level == 2:  # ez difficulty
        removek(10)
    elif level == 3:  # easy difficulty
        removek(20)
    elif level == 4:  # medium difficulty
        removek(35)


WIDTH = 550  # width of game window
HEIGHT = 700  # height of game window
background_color = (255, 255, 255)  # background colour of game window


#################################
def levelSelectwindow():
    pygame.init()
    lswin = pygame.display.set_mode((WIDTH, HEIGHT))  # forming window

    pygame.display.set_caption("Choose Your Level")  # assigning caption to window
    lswin.fill(background_color)  # giving colour to window

    lfont = pygame.font.SysFont('Comic Sans MS', 15)
    levelchoose = lfont.render('Choose Your Level: ', True, (0, 0, 0))
    level1 = lfont.render('Quick Test', True, (0, 0, 0))
    level2 = lfont.render('Easy', True, (0, 0, 0))
    level3 = lfont.render('Medium', True, (0, 0, 0))
    level4 = lfont.render('Hard', True, (0, 0, 0))


    lswin.blit(levelchoose, (225 + 15, 50 + 10))
    pygame.draw.rect(lswin, (255,255,0), [200, 150, 200, 50])
    lswin.blit(level1, (225 + 35, 150 + 10))
    pygame.draw.rect(lswin, (0,255,0), [200, 250, 200, 50])
    lswin.blit(level2, (225 + 35, 250 + 10))
    pygame.draw.rect(lswin, (0,255,255), [200, 350, 200, 50])
    lswin.blit(level3, (225 + 35, 350 + 10))
    pygame.draw.rect(lswin, (255,0,0), [200, 450, 200, 50])
    lswin.blit(level4, (225 + 35, 450 + 10))
    pygame.display.update()

    lselectmenu = 1
    while lselectmenu == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # close the window
                pygame.quit()
                return
            mposefLevelSelection = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 200 <= mposefLevelSelection[0] <= 400 and 150 <= mposefLevelSelection[1] <= 200:
                    levelSelect(1)
                    return
                if 200 <= mposefLevelSelection[0] <= 400 and 250 <= mposefLevelSelection[1] <= 300:
                    levelSelect(2)
                    return
                if 200 <= mposefLevelSelection[0] <= 400 and 350 <= mposefLevelSelection[1] <= 400:
                    levelSelect(3)
                    return
                if 200 <= mposefLevelSelection[0] <= 400 and 450 <= mposefLevelSelection[1] <= 500:
                    levelSelect(4)
                    return


##################################


levelSelectwindow()

original_grid_element_color = (52, 31, 151)  # color of number generated by default
buffer = 5  # constant value to make sudoku attractive

grid_original = [[grid[x][y] for y in range(len(grid[0]))] for x in
                 range(len(grid))]  # copy of original grid - formed for checking the solution at last


# this function is created for inserting the input by the user in the grid

def insert(win, position):
    i, j = position[1], position[0]  # we will use i and j to made the update in grid variable
    myfont = pygame.font.SysFont('Comic Sans MS',
                                 35)  # font of input given by the user and also used for default populated grid

    while True:
        for event in pygame.event.get():  # event which we are going to do

            if event.type == pygame.QUIT:  # closing game window
                return

            if event.type == pygame.KEYDOWN:  # keyboard button is pressed
                if grid_original[i - 1][j - 1] != 0:  # means there is already some number on the grid . i.e original grid element is not empty
                    return

                if event.key == 48:  # if key = 0    bcz 48 is the ASCII value of 0
                    grid[i - 1][j - 1] = event.key - 48  # to update the grid variable
                    pygame.draw.rect(win, background_color, (
                        position[0] * 50 + buffer, position[1] * 50 + 2 * buffer, 50 - 3 * buffer,
                        50 - 3 * buffer))  # function is used to draw a rectangle

                    pygame.display.update()  # to update the changes we have made

                if 0 < event.key - 48 < 10:  # if key = [1,9]
                    grid[i - 1][j - 1] = event.key - 48  # to update the grid variable
                    value = myfont.render(str(event.key - 48), True,
                                          (0, 0, 255))  # render is used to make object of text
                    win.blit(value, (
                        position[0] * 50 + 15, position[1] * 50 + 5))  # blit is used to print object on the window

                    pygame.display.update()

                return
    return


def main():
    pygame.init()  # initialising pygame

    win = pygame.display.set_mode((WIDTH, HEIGHT))  # forming window

    pygame.display.set_caption("SUDOKU")  # assigning caption to window
    win.fill(background_color)  # giving colour to window
    myfont = pygame.font.SysFont('Comic Sans MS', 24)  # font for populating the grid
    solnfont = pygame.font.SysFont('Comic Sans MS', 15)  # font for printing CheckSolution term on screen
    checkSolntext = solnfont.render('Check Solution', True, (0, 0, 0))  # rendering CheckSolution

    for i in range(0, 10):
        if i % 3 == 0:
            pygame.draw.line(win, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 4)  # darker vertical line
            pygame.draw.line(win, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 4)  # darker horizontal line

        pygame.draw.line(win, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 1)  # lighter vertical line
        pygame.draw.line(win, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 1)  # lighter horizontal line
    pygame.display.update()

    pygame.draw.rect(win, (255, 199, 189), [225, 600, 125, 40])  # rectangle for CheckSolution term
    win.blit(checkSolntext, (225 + 15, 600 + 10))  # blitting checkSolution on screen
    pygame.display.update()

    for i in range(0, len(grid[0])):  # this whole for loop is for populating grid with numbers
        for j in range(0, len(grid[0])):
            if 0 < grid[i][j] < 10:
                value = myfont.render(str(grid[i][j]), True, (0, 0, 0))
                win.blit(value, ((j + 1) * 50 + 10, (i + 1) * 50 + 10))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # close the window
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # mousebuttonup means mouse button release after pressing and left click (1 means)
                pos = pygame.mouse.get_pos()  # getting position of mouse
                insert(win, (pos[0] // 50, pos[1] // 50))  # on dividing by 50 to get the grid indices

            if event.type == pygame.MOUSEBUTTONDOWN:  # means mouse button pressed and it can be any click . it is used for clicking on checksolution term
                mousepos = pygame.mouse.get_pos()  # getting position of click
                if 225 <= mousepos[0] <= 365 and 600 <= mousepos[1] <= 650:

                    # this whole function is used to checking the answer and then printing the result on pop-up window. i.e whether we are correct or wrong

                    if grid != sudokuGrid:
                        pprint(grid)
                        pprint(sudokuGrid)
                        ctypes.windll.user32.MessageBoxW(0, "Mission Failed, we'll get em next time", "OHHH NO!",
                                                         1)  # ctype is used for pop window
                    elif grid == sudokuGrid:
                        pprint(grid)
                        pprint(sudokuGrid)
                        ctypes.windll.user32.MessageBoxW(0, "You Won!!!", "CONGRATULATIONS", 1)


main()
