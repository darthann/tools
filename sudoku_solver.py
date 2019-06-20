SUDOKU_SIZE = 9

def isRowFree(value, grid, col):
        for y in range(SUDOKU_SIZE):
                if value == grid[y][col]:
                        return False
        return True


def isColFree(value, grid, row):
        for x in range(SUDOKU_SIZE):
                if value == grid[row][x]:
                        return False
        return True


def isBoxFree(value, grid, row, col):
        row_start = row - row % 3
        col_start = col - col % 3
        for x in range(row_start, row_start + 3):
                for y in range(col_start, col_start + 3):
                        if value == grid[x][y]:
                                return False
        return True


def isValid(value, grid, row, col):
        if isRowFree(value, grid, col) and isColFree(value, grid, row) and isBoxFree(value, grid, row, col):
                return True
        else:
                return False


def getFreeCase(grid):
        for x in range(SUDOKU_SIZE):
                for y in range(SUDOKU_SIZE):
                        if grid[x][y] == "0":
                                return (x, y)


def isSudokuComplete(grid):
        for line in grid:
                if "0" in line:
                        return False
        return True


def solveSudoku(grid):
        if isSudokuComplete(grid):
                return True

        position = getFreeCase(grid)

        for number in range(1, SUDOKU_SIZE + 1):
                if isValid(str(number), grid, position[0], position[1]):
                        grid[position[0]][position[1]] = str(number)

                        if solveSudoku(grid):
                                return True
                        
                        grid[position[0]][position[1]] = "0"
        
        return False


def printGrid(grid):
        for x in range(SUDOKU_SIZE):
                line = "|"
                for y in range(SUDOKU_SIZE):
                        line += " {} |".format(grid[x][y])
                print(line)


sudoku_input = open("sudoku_example.txt", "r").read()
sudoku_input = sudoku_input.split("\n")[4:len(sudoku_input.split("\n")) - 2]
sudoku = []
for line in sudoku_input:
        if "|" in line:
                sudoku.append(line)

line_size = len(sudoku[0])

for i in range(len(sudoku)):
        sudoku[i] = sudoku[i][1:line_size - 2].split("|")
        for j in range(SUDOKU_SIZE):
                sudoku[i][j] = sudoku[i][j].strip()
                if sudoku[i][j] == "":
                        sudoku[i][j] = "0"


printGrid(sudoku)
print("Sudoku resolver result : {}".format(solveSudoku(sudoku)))
printGrid(sudoku)