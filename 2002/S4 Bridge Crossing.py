# https://dmoj.ca/problem/ccc02s4
from math import inf

maximum_group_size = int(input())
number_of_people = int(input())

names = []
times = []
for _ in range(number_of_people):
    names.append(input())
    times.append(int(input()))

best_times = [[inf] for _ in range(number_of_people + 1)]  # 2D dp array
best_times[0][0] = 0

for i in range(number_of_people + 1):
    for group_size in range(1, maximum_group_size + 1):
        if i + group_size > number_of_people:
            continue
        if max(times[i:i + group_size]) + best_times[i][0] < best_times[i + group_size][0]:
            best_times[i + group_size] = [j for j in best_times[i]]
            best_times[i + group_size][0] += max(times[i:i + group_size])
            best_times[i + group_size].append(names[i:i + group_size])

print("Total Time: " + str(best_times[number_of_people][0]))
for i in range(1, len(best_times[number_of_people])):
    print(" ".join(best_times[number_of_people][i]))
