# https://dmoj.ca/problem/ccc03s1
square = 1

while True:
    roll = int(input())
    if roll == 0:
        print("You Quit!")
        break

    if square + roll <= 100:
        square += roll

    if square == 9:
        square = 34
    elif square == 40:
        square = 64
    elif square == 67:
        square = 86
    elif square == 54:
        square = 19
    elif square == 90:
        square = 48
    elif square == 99:
        square = 77

    print("You are now on square", square)
    if square == 100:
        print("You Win!")
        break


