# https://dmoj.ca/problem/ccc03s3
flooring = int(input())
rows = int(input())
columns = int(input())

floor_plan = []
for _ in range(rows):
    floor_plan.append([*input()])  # turn string into list of characters

# "." represents an empty space. Will turn these to "," after processing


def get_neighbors(target):
    neighbors = []

    row = target[0]
    column = target[1]

    if row - 1 >= 0:
        neighbors.append((row - 1, column))
    if row + 1 < rows:
        neighbors.append((row + 1, column))
    if column - 1 >= 0:
        neighbors.append((row, column - 1))
    if column + 1 < columns:
        neighbors.append((row, column + 1))

    return neighbors


rooms = []

for row in range(rows):
    for column in range(columns):
        if floor_plan[row][column] == ".":  # found a new room
            # quick BFS to find rest of the tiles in the room
            current_room = []  # equivalent to a "visited" list
            queue = [(row, column)]
            while len(queue) > 0:
                target = queue.pop()
                if target not in current_room:
                    current_room.append(target)
                    floor_plan[target[0]][target[1]] = ","
                    for neighbor in get_neighbors(target):
                        if (neighbor not in current_room) and (floor_plan[neighbor[0]][neighbor[1]] == "."):
                            queue.append(neighbor)
            rooms.append(current_room)


rooms = sorted(rooms, key=lambda x: len(x), reverse=True)
rooms_filled = 0

while True:
    try:
        if flooring >= len(rooms[0]):
            flooring -= len(rooms[0])
            rooms_filled += 1
            rooms.remove(rooms[0])
        else:
            break
    except IndexError:
        break

if rooms_filled == 1:
    print("1 room, {0} square metre(s) left over".format(flooring))
else:
    print("{0} rooms, {1} square metre(s) left over".format(rooms_filled, flooring))