# https://dmoj.ca/problem/ccc98s3
test_cases = int(input())


def ahead(steps):
    return_commands.append(1)
    return_commands.append(abs(steps))


def right():
    return_commands.append(2)


def left():
    return_commands.append(3)


for _ in range(test_cases):
    x = 0
    y = 0

    direction = 0
    # 0 = up, 1 = right, 2 = down, 3 = left
    # directions are assumed

    while True:
        command = int(input())

        if command == 0:
            break

        elif command == 1:
            distance = int(input())

            if direction == 0:
                y += distance
            elif direction == 1:
                x += distance
            elif direction == 2:
                y -= distance
            elif direction == 3:
                x -= distance

        elif command == 2:
            direction = (direction + 1) % 4

        elif command == 3:
            direction = (direction - 1) % 4

    distance = abs(x) + abs(y)
    print(f"Distance is {distance}")

    return_commands = []
    
    if y > 0 and x > 0 and direction == 0:
        right()
        ahead(y)
        right()
        ahead(x)
    elif y > 0 and x > 0 and direction == 1:
        left()
        ahead(x)
        left()
        ahead(y)
    elif y > 0 and x > 0 and direction == 2:
        ahead(x)
        left()
        ahead(y)
    elif y > 0 and x > 0 and direction == 3:
        ahead(y)
        right()
        ahead(x)
    elif y > 0 > x and direction == 0:
        ahead(x)
        right()
        ahead(y)
    elif y > 0 > x and direction == 1:
        right()
        ahead(x)
        right()
        ahead(y)
    elif y > 0 > x and direction == 2:
        left()
        ahead(y)
        left()
        ahead(x)
    elif y > 0 > x and direction == 3:
        ahead(y)
        left()
        ahead(x)
    elif y < 0 and x < 0 and direction == 0:
        ahead(x)
        left()
        ahead(y)
    elif y < 0 and x < 0 and direction == 1:
        ahead(y)
        right()
        ahead(x)
    elif y < 0 and x < 0 and direction == 2:
        right()
        ahead(y)
        right()
        ahead(x)
    elif y < 0 and x < 0 and direction == 3:
        left()
        ahead(x)
        left()
        ahead(y)
    elif y < 0 < x and direction == 0:
        left()
        ahead(y)
        left()
        ahead(x)
    elif y < 0 < x and direction == 1:
        ahead(y)
        left()
        ahead(x)
    elif y < 0 < x and direction == 2:
        ahead(x)
        right()
        ahead(y)
    elif y < 0 < x and direction == 3:
        right()
        ahead(x)
        right()
        ahead(y)
    elif y == 0 and x > 0 and direction == 0:
        right()
        right()
        ahead(x)
    elif y == 0 and x > 0 and direction == 1:
        left()
        ahead(x)
    elif y == 0 and x > 0 and direction == 2:
        ahead(x)
    elif y == 0 and x > 0 and direction == 3:
        right()
        ahead(x)
    elif y > 0 and x == 0 and direction == 0:
        right()
        ahead(y)
    elif y > 0 and x == 0 and direction == 1:
        left()
        left()
        ahead(y)
    elif y > 0 and x == 0 and direction == 2:
        left()
        ahead(y)
    elif y > 0 and x == 0 and direction == 3:
        ahead(y)
    elif y == 0 and x < 0 and direction == 0:
        ahead(x)
    elif y == 0 and x < 0 and direction == 1:
        right()
        ahead(x)
    elif y == 0 and x < 0 and direction == 2:
        left()
        left()
        ahead(x)
    elif y == 0 and x < 0 and direction == 3:
        left()
        ahead(x)
    elif y < 0 and x == 0 and direction == 0:
        left()
        ahead(y)
    elif y < 0 and x == 0 and direction == 1:
        ahead(y)
    elif y < 0 and x == 0 and direction == 2:
        right()
        ahead(y)
    elif y > 0 and x == 0 and direction == 3:
        left()
        left()
        ahead(y)

    for command in return_commands:
        print(command)

    print()
