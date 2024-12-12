# https://dmoj.ca/problem/ccc98s2
from math import floor, sqrt


def get_perfect_divisors(n):
    divisors = []

    for i in range(1, n):
        if n % i == 0:  # divides perfectly
            divisors.append(i)

    return divisors


def is_perfect(n):
    return sum(get_perfect_divisors(n)) == n


def is_cube_sum(n):
    sum = 0

    for num in str(n):
        sum += int(num) ** 3

    return sum == n


for i in range(1000, 10000):
    if is_perfect(i):
        print(i, end=" ")

print()

for i in range(100, 1000):
    if is_cube_sum(i):
        print(i, end=" ")
