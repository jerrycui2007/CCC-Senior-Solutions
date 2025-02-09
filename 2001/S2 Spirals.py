# https://dmoj.ca/problem/ccc01s2

spiral_map = []
for _ in range(11):
    spiral_map.append([" "] * 11)

x = int(input())
y = int(input())

row, column = 5, 5
spiral_map[5][5] = str(x)
direction = "DOWN"

while x < y:
    if direction == "DOWN":
        if spiral_map[row][column + 1] == " " and (row, column) != (5, 5):  # Start position
            direction = "RIGHT"
            column += 1
        else:
            row += 1
    elif direction == "RIGHT":
        if spiral_map[row - 1][column] == " ":
            direction = "UP"
            row -= 1
        else:
            column += 1
    elif direction == "UP":
        if spiral_map[row][column - 1] == " ":
            direction = "LEFT"
            column -= 1
        else:
            row -= 1
    elif direction == "LEFT":
        if spiral_map[row + 1][column] == " ":
            direction = "DOWN"
            row += 1
        else:
            column -= 1

    x += 1
    spiral_map[row][column] = str(x)


output_lines = []
for line in spiral_map:
    string_line = " "
    for char in line:
        string_line += char + " "
    output_lines.append(string_line)

for line in output_lines:
    if line != "                       ":
        print(line)