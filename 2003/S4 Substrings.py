# https://dmoj.ca/problem/ccc03s4
n = int(input())


def longest_common_prefix(string_1, string_2):
    max_length = min(len(string_1), len(string_2))
    for i in range(max_length):
        if string_1[i] != string_2[i]:
            return i

    return max_length


cache = {}

for _ in range(n):

    string = input()

    if string in cache:
        print(cache[string])
    else:
        suffixes = []
        for i in range(len(string)):
            suffixes.append(string[i:])
        suffixes.sort()

        total = len(suffixes[0]) + 1
        for i in range(1, len(string)):
            total += len(suffixes[i]) - longest_common_prefix(suffixes[i], suffixes[i - 1])

        cache[string] = total

        print(total)