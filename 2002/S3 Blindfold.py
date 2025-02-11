# https://dmoj.ca/problem/ccc02s3
# TLE on DMOJ but passes original test cases
rows = int(input())
columns = int(input())

original_map = []
for _ in range(rows):
    original_map.append(list(input().strip()))

number_of_moves = int(input())
moves = []
for _ in range(number_of_moves):
    moves.append(input())
            

# Create a copy of the map to mark possible positions
possible = [row.copy() for row in original_map]

directions = ("North", "East", "South", "West")


def is_valid(row, col):
    if 0 <= row < rows and 0 <= col < columns:
        return original_map[row][col] != "X"
    return False


def turn_right(d):
    return {"North": "East", "East": "South", "South": "West", "West": "North"}[d]


def turn_left(d):
    return {"North": "West", "West": "South", "South": "East", "East": "North"}[d]


for row in range(rows):
    for col in range(columns):
        if original_map[row][col] == "X":
            continue
        for direction in directions:
            current_row, current_col = row, col
            current_direction = direction
            invalid = False

            # Process moves in reverse order

            for move in reversed(moves):
                if move == "F":
                    if current_direction == "North":
                        current_row += 1
                    elif current_direction == "East":
                        current_col -= 1
                    elif current_direction == "South":
                        current_row -= 1
                    elif current_direction == "West":
                        current_col += 1
                    if not is_valid(current_row, current_col):
                        invalid = True
                        break
                elif move == "R":
                    current_direction = turn_left(current_direction)
                elif move == "L":
                    current_direction = turn_right(current_direction)
            if not invalid:
                possible[row][col] = "*"
                break

for row in possible:
    print("".join(row))