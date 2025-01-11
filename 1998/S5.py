# https://dmoj.ca/problem/ccc98s5
from math import inf
from heapq import heappush, heappop

trips = int(input())


def shortest_path(elevations, size, starting_elevation):
    # start is always (0, 0), end is always (size - 1, size - 1)
    distances = [[inf for _ in range(size)] for _ in range(size)]
    distances[0][0] = 0

    visited = [[False for _ in range(size)] for _ in range(size)]
    visited[0][0] = True

    queue = [(0, (0, 0))]  # (distances[start], start)

    while queue:
        cost, target = heappop(queue)
        row, column = target
        if not visited[row][column]:
            visited[row][column] = True

        if row == size - 1 and column == size - 1:  # reached the end
            return cost

        # Get all neighbors
        if row > 0:  # up
            if not visited[row - 1][column]:
                if abs(elevations[row][column] - elevations[row - 1][column]) <= 2:  # within distance
                    if elevations[row][column] > starting_elevation or elevations[row - 1][column] > starting_elevation:
                        cost = 1 + distances[row][column]
                    else:
                        cost = distances[row][column]

                    if cost < distances[row - 1][column]:
                        distances[row - 1][column] = cost
                        heappush(queue, (cost, (row - 1, column)))

        if row < size - 1:  # down
            if not visited[row + 1][column]:
                if abs(elevations[row][column] - elevations[row + 1][column]) <= 2:  # within distance
                    if elevations[row][column] > starting_elevation or elevations[row + 1][column] > starting_elevation:
                        cost = 1 + distances[row][column]
                    else:
                        cost = distances[row][column]

                    if cost < distances[row + 1][column]:
                        distances[row + 1][column] = cost
                        heappush(queue, (cost, (row + 1, column)))

        if column > 0:  # left
            if not visited[row][column - 1]:
                if abs(elevations[row][column] - elevations[row][column - 1]) <= 2:  # within distance
                    if elevations[row][column] > starting_elevation or elevations[row][column - 1] > starting_elevation:
                        cost = 1 + distances[row][column]
                    else:
                        cost = distances[row][column]

                    if cost < distances[row][column - 1]:
                        distances[row][column - 1] = cost
                        heappush(queue, (cost, (row, column - 1)))

        if column < size - 1:  # left
            if not visited[row][column + 1]:
                if abs(elevations[row][column] - elevations[row][column + 1]) <= 2:  # within distance
                    if elevations[row][column] > starting_elevation or elevations[row][column + 1] > starting_elevation:
                        cost = 1 + distances[row][column]
                    else:
                        cost = distances[row][column]

                    if cost < distances[row][column + 1]:
                        distances[row][column + 1] = cost
                        heappush(queue, (cost, (row, column + 1)))

    return -1  # no path found


for i in range(trips):
    size = int(input())

    elevations = [[None for _ in range(size)] for _ in range(size)]

    for row in range(size):
        for column in range(size):
            elevations[row][column] = int(input())

    starting_elevation = elevations[0][0]
    oxygen_required = shortest_path(elevations, size, starting_elevation)

    if oxygen_required == -1:
        print("CANNOT MAKE THE TRIP")
    else:
        print(oxygen_required)

    if i != trips - 1:
        print()




