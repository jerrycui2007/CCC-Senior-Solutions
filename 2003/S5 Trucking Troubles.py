# https://dmoj.ca/problem/ccc03s5
# Construct graph, and use a binary search to test every possible answer, using a DFS to see if possible
import sys


def main():
    c, r, d = map(int, sys.stdin.readline().split())
    adj = [[] for _ in range(c + 1)]

    for _ in range(r):
        x, y, w = map(int, sys.stdin.readline().split())
        adj[x].append((y, w))
        adj[y].append((x, w))

    destinations = [int(sys.stdin.readline()) for _ in range(d)]

    low = 0
    high = 100000
    answer = 0

    while low <= high:
        mid = (low + high) // 2
        visited = set()
        stack = [1]
        visited.add(1)

        while stack:
            current = stack.pop()
            for neighbor, weight in adj[current]:
                if weight >= mid and neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)

        all_visited = True
        for city in destinations:
            if city not in visited:
                all_visited = False
                break

        if all_visited:
            answer = mid
            low = mid + 1
        else:
            high = mid - 1

    print(answer)


if __name__ == "__main__":
    main()