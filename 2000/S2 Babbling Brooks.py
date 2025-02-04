#　https://dmoj.ca/problem/ccc00s2

streams = []
number_of_streams = int(input())

for _ in range(number_of_streams):
    streams.append(int(input()))

while True:
    command = int(input())
    if command == 99:
        index = int(input()) - 1
        percentage = int(input())

        amount = streams[index]

        streams[index] = int(amount * percentage / 100)
        streams.insert(index + 1, amount - streams[index])

    elif command == 88:
        index = int(input()) - 1

        streams[index] += streams[index + 1]
        streams.pop(index + 1)

    elif command == 77:
        break

print(" ".join(map(str, streams)))
