# Dijkstra's algorithm, finds the shortest path in a weighted graph
from heapq import heappop, heappush

sample_graph = {"A": {"B": 1, "D": 4},
                "B": {"A": 2, "C": 1},
                "C": {"B": 3, "G": 2},
                "D": {"A": 4, "E": 3},
                "E": {"D": 1, "F": 4},
                "F": {"E": 2, "G": 1},
                "G": {"F": 3, "C": 2}
                }


def shortest_path_weighted(graph, start, end):
    distances = {node: 10000 for node in graph}  # cost from start to each node
    distances[start] = 0

    visited = set()
    visited.add(start)
    queue = [(distances[start], start)]

    predecessors = {node: None for node in graph}

    while len(queue) > 0:
        (cost, target) = heappop(queue)
        if target not in visited:
            visited.add(target)

        if target == end:
            # option if you want path
            path = [end]
            while path[-1] != start:
                path.append(predecessors[path[-1]])

            path.reverse()
            # optional part ends
            return cost, path

        for neighbor in graph[target]:
            if neighbor not in visited:
                temp_distance = distances[target] + graph[target][neighbor]
                if temp_distance < distances[neighbor]:
                    distances[neighbor] = temp_distance
                    predecessors[neighbor] = target
                    heappush(queue, (temp_distance, neighbor))




if __name__ == "__main__":
    print(shortest_path_weighted(sample_graph, "A", "F"))
