# https://dmoj.ca/problem/ccc24s1
def count_matching_hats(n, hats):
    count = 0
    half_n = n // 2
    for i in range(n):
        if hats[i] == hats[(i + half_n) % n]:
            count += 1
    return count


n = int(input())
hats = [int(input()) for _ in range(n)]
result = count_matching_hats(n, hats)
print(result)
