# https://dmoj.ca/problem/ccc05s2

c, r = list(map(int, input().split()))
instructions = []
results = []
x = 0
y = 0

while True:
    instruction = input()
    if instruction == "0 0":
        break
    else:
        instructions.append(instruction.split())

for instruction in instructions:
    x += int(instruction[0])
    if x > c:
        x = c
    if x < 0:
        x = 0
    y += int(instruction[1])
    if y > r:
        y = r
    if y < 0:
        y = 0
    print(x, y)
