# https://dmoj.ca/problem/ccc04s5
def get_grid(rows, columns):
    grid = [[0] * columns for _ in range(rows)]  # initialize grid

    for i in range(rows):
        line = input()
        for j in range(len(line)):
            if line[j] == "*":
                grid[i][j] = -1
            elif line[j] == ".":
                grid[i][j] = 0
            else:
                grid[i][j] = int(line[j])

    return grid


def solve(grid, rows, columns):
    dp_grid = [[-1] * columns for _ in range(rows)]  # initialize all values to -1

    # solve first column
    dp_grid[rows - 1][0] = grid[rows - 1][0]  # starting location
    for row in range(rows - 2, -1, -1):
        if grid[row][0] >= 0:
            dp_grid[row][0] = dp_grid[row + 1][0] + grid[row][0]
        else:
            break  # leave because we encountered a wall

    # now solve each column afterwards
    for column in range(1, columns):
        # going down
        for row in range(0, rows):
            if dp_grid[row][column - 1] >= 0:  # make sure tile to left is not a wall
                current_score = dp_grid[row][column - 1]
                for current_row in range(row, rows):
                    if grid[current_row][column] >= 0:
                        current_score += grid[current_row][column]
                        if current_score > dp_grid[current_row][column]:
                            dp_grid[current_row][column] = current_score
                    else:  # hit a wall and exit
                        break
        # going up
        for row in range(rows - 1, -1, -1):
            if dp_grid[row][column - 1] >= 0:
                current_score = dp_grid[row][column - 1]
                for current_row in range(row, -1, -1):
                    if grid[current_row][column] >= 0:
                        current_score += grid[current_row][column]
                        if current_score > dp_grid[current_row][column]:
                            dp_grid[current_row][column] = current_score
                    else:
                        break

    return dp_grid[rows - 1][columns - 1]  # bottom right corner


while True:
    rows, columns = map(int, input().split())
    if rows == columns == 0:
        break
    else:
        print(solve(get_grid(rows, columns), rows, columns))
