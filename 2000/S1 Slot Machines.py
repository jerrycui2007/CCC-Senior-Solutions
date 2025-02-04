# https://dmoj.ca/problem/ccc00s1

quarters = int(input())
machine1 = int(input())
machine2 = int(input())
machine3 = int(input())

times_played = 0

current = 1

while quarters > 0:
    quarters -= 1
    times_played += 1

    if current == 1:
        machine1 += 1
        if machine1 == 35:
            quarters += 30
            machine1 = 0
        current = 2
    elif current == 2:
        machine2 += 1
        if machine2 == 100:
            quarters += 60
            machine2 = 0
        current = 3
    elif current == 3:
        machine3 += 1
        if machine3 == 10:
            quarters += 9
            machine3 = 0
        current = 1

print(f"Martha plays {times_played} times before going broke.")
