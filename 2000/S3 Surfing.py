# https://dmoj.ca/problem/ccc00s3
import re

n = int(input())
pages = {}

pattern = r'<A HREF="(.*?)">'

for _ in range(n):
    url = input()
    pages[url] = []

    while True:
        line = input()

        for link in re.findall(pattern, line):
            pages[url].append(link)

        if "</HTML>" in line:
            break

# Print out all links
for url in pages:
    for link in pages[url]:
        print("Link from", url, "to", link)


# Check connections
def check_connection(start, end):
    visited = set()
    queue = [start]

    while len(queue) > 0:
        url = queue.pop(0)
        visited.add(url)

        for link in pages[url]:
            if link == end:
                return True

            if link not in visited:
                queue.append(link)

    return False


while True:
    start = input()
    if start == "The End":
        break

    end = input()

    if check_connection(start, end):
        print(f"Can surf from {start} to {end}.")
    else:
        print(f"Can't surf from {start} to {end}.")
