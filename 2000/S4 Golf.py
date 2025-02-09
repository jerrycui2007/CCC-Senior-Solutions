# https://dmoj.ca/problem/ccc00s4
from math import inf

distance = int(input())

number_of_clubs = int(input())
clubs = []
for _ in range(number_of_clubs):
    clubs.append(int(input()))

dp = [inf for _ in range(distance + 1)]  # non-zero indexed array
dp[0] = 0

for i in range(0, distance):
    for club in clubs:
        try:
            dp[i + club] = min(dp[i + club], dp[i] + 1)
        except IndexError:
            pass

if dp[distance] == inf:
    print("Roberta acknowledges defeat.")
else:
    print(f"Roberta wins in {dp[distance]} strokes.")

