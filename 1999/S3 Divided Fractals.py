test_cases = int(input())


def fractal(row, column, side_length):
    section_length = side_length // 3
    start_row = row + section_length
    start_col = column + section_length

    for i in range(section_length):
        for j in range(section_length):
            grid[start_row + i][start_col + j] = " "


def recursive_fractal(row, column, side_length):
    if side_length == 1:
        return

    fractal(row, column, side_length)

    new_side = side_length // 3

    recursive_fractal(row, column, new_side)
    recursive_fractal(row, column + new_side, new_side)
    recursive_fractal(row, column + 2 * new_side, new_side)

    recursive_fractal(row + new_side, column, new_side)
    recursive_fractal(row + new_side, column + 2 * new_side, new_side)

    recursive_fractal(row + 2 * new_side, column, new_side)
    recursive_fractal(row + 2 * new_side, column + new_side, new_side)
    recursive_fractal(row + 2 * new_side, column + 2 * new_side, new_side)


for _ in range(test_cases):
    n = int(input())
    b = int(input())
    t = int(input())
    l = int(input())
    r = int(input())

    grid_size = 3 ** n
    grid = [["*" for _ in range(grid_size)] for _ in range(grid_size)]

    recursive_fractal(0, 0, grid_size)

    start_row = t - 1
    end_row = b - 1
    left_col = l - 1
    right_col = r - 1

    for row in range(start_row, end_row - 1, -1):
        line = " ".join(grid[row][left_col: right_col + 1])
        print(line)

    print()
