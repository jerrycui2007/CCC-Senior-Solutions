# https://dmoj.ca/problem/ccc01s3

map = {char: [] for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
roads = []
while True:
    road = input()

    if road == "**":
        break

    map[road[0]].append(road[1])
    map[road[1]].append(road[0])
    roads.append(road)


def is_connected(start, end, bombed_road):
    visited = set()
    queue = [start]
    visited.add(start)

    while queue:
        current = queue.pop(0)
        if current == end:
            return True
        for neighbor in map[current]:
            # Skip both directions of the bombed road
            if (current == bombed_road[0] and neighbor == bombed_road[1]) or (current == bombed_road[1] and neighbor == bombed_road[0]):
                continue
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return False


disconnecting_roads = []
for road in roads:
    if not is_connected("A", "B", road):
        disconnecting_roads.append(road)

for road in disconnecting_roads:
    print(road)
print(f"There are {len(disconnecting_roads)} disconnecting roads.")