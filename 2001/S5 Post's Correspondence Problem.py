# https://dmoj.ca/problem/ccc01s5
m = int(input())
n = int(input())

A = []
B = []

for _ in range(n):
    A.append(input())

for _ in range(n):
    B.append(input())

solution = []
solved = False


def posts_correspondence_problem(k, i, a, b):
    global solved

    if k >= m:  # index out of bounds
        return False

    solution.append(i + 1)
    a += A[i]
    b += B[i]

    if a == b:
        solved = True

        print(k)
        for index in solution:
            print(index)

        return True

    # Brute force check
    for j in range(n):
        if posts_correspondence_problem(k + 1, j, a, b):
            return True

    solution.pop(-1)


for i in range(n):
    posts_correspondence_problem(1, i, "", "")

if not solved:
    print("No solution.")