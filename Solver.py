# Author: Ernestas Škudzinskas
# 
# Program: This program will solve a sudoku.
# Initial grid is filled with numbers and empty spaces (zeroes)
# It will output a solved sudoku grid
#
# The solution is found using backtracking


grid = [
    [0, 3, 0, 0, 1, 0, 0, 6, 0],
    [7, 5, 0, 0, 3, 0, 0, 4, 8],
    [0, 0, 6, 9, 8, 4, 3, 0, 0],
    [0, 0, 3, 0, 0, 0, 8, 0, 0],
    [9, 1, 2, 0, 0, 0, 6, 7, 4],
    [0, 0, 4, 0, 0, 0, 5, 0, 0],
    [0, 0, 1, 6, 7, 5, 2, 0, 0],
    [6, 8, 0, 0, 9, 0, 0, 1, 5],
    [0, 9, 0, 0, 4, 0, 0, 3, 0]
]


def Solve(grid):

    position = findNext(grid)
    
    if position != None:
        row, col = position
    else:
        return True

    for i in range(1, 10):
        if(Valid(grid, position, i)):
            grid[row][col] = i
            if Solve(grid):
                return True
            grid[row][col] = 0

    return False


def findNext(grid):
    for i in range(0, 9):
        for j in range(0, 9):
            if grid[i][j] == 0:
                return (i, j)
    
    return None

def Valid(grid, pos, number):

    row, col = pos

    for i in range(0, 9):
        if( grid[i][col] == number and row != i):
            return False

    for j in range(0, 9):
        if( grid[row][j] == number and col != j):
            return False

    xRegion = row // 3
    yRegion = col // 3

    for i in range(xRegion * 3, xRegion * 3 + 3):
        for j in range(yRegion * 3, yRegion * 3 + 3):
            if grid[i][j] == number and (i, j) != pos:
                return False
        
    return True

def PrintGrid(grid):
    for i in range(0, 9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(0, 9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            
            print(grid[i][j], end=" ")
        print("\n", end="")


Solve(grid)
PrintGrid(grid)