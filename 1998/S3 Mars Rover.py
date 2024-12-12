
n = int(input())

for _ in range(n):
    startX, startY = 0, 0
    roverX, roverY = 0, 0
    direction = 0  # 0 is north, 90 is east, . . .

    while True:
        instruction = int(input())

        # End of excursion
        if instruction == 0:
            break

        # Move
        if instruction == 1:
            distance = int(input())

            if direction == 0:
                roverY += distance
            elif direction == 90:
                roverX += distance
            elif direction == 180:
                roverY -= distance
            else:
                roverX -= distance

        # Turn right
        elif instruction == 2:
            direction += 90
            direction %= 360

        # Turn left
        else:
            direction += 270
            direction %= 360

    # Output distance
    print(f"Distance is {abs(roverX) + abs(roverY)}")

    # Top Left Quadrant
    if roverX < startX and roverY > startY:
        if direction == 0:
            print("2\n1\n" + str(startX - roverX) + "\n2\n1\n" + str(roverY))
        elif direction == 90:
            print("1\n" + str(startX - roverX) + "\n2\n1\n" + str(roverY))
        elif direction == 180:
            print("1\n" + str(roverY) + "\n3\n1\n" + str(startX - roverX))
        else:
            print("3\n1\n" + str(roverY) + "\n3\n1\n" + str(startX - roverX))

    # Top Right Quadrant
    if roverX > startX and roverY > startY:
        if direction == 0:
            print("3\n1\n" + str(roverX) + "\n3\n1\n" + str(roverY))
        elif direction == 90:
            print("2\n1\n" + str(roverY) + "\n2\n1\n" + str(roverX))
        elif direction == 180:
            print("1\n" + str(roverY) + "\n2\n1\n" + str(roverX))
        else:
            print("1\n" + str(roverX) + "\n3\n1\n" + str(roverY))

    # Bottom Right Quadrant
    if roverX > startX and roverY < startY:
        if direction == 0:
            print("1\n" + str(startY - roverY) + "\n3\n1\n" + str(roverX))
        elif direction == 90:
            print("3\n1\n" + str(startY - roverY) + "\n3\n1\n" + str(roverX))
        elif direction == 180:
            print("2\n1\n" + str(roverX) + "\n2\n1\n" + str(startY - roverY))
        else:
            print("1\n" + str(roverX) + "\n2\n1\n" + str(startY - roverY))

    # Bottom Left Quadrant
    if roverX < startX and roverY < startY:
        if direction == 0:
            print("1\n" + str(startY - roverY) + "\n2\n1\n" + str(startX - roverX))
        elif direction == 90:
            print("1\n" + str(startX - roverX) + "\n3\n1\n" + str(startY - roverY))
        elif direction == 180:
            print("3\n1\n" + str(startX - roverX) + "\n3\n1\n" + str(startY - roverY))
        else:
            print("2\n1\n" + str(startY - roverY) + "\n2\n1\n" + str(startX - roverX))

    # Positive Y Axis
    if roverX == startX and roverY > startY:
        if direction == 0:
            print("2\n2\n1\n" + str(roverY))
        elif direction == 90:
            print("2\n1\n" + str(roverY))
        elif direction == 180:
            print("1\n" + str(roverY))
        else:
            print("3\n1\n" + str(roverY))

    # Negative Y Axis
    if roverX == startX and roverY < startY:
        if direction == 0:
            print("1\n" + str(startY - roverY))
        elif direction == 90:
            print("3\n1\n" + str(startY - roverY))
        elif direction == 180:
            print("2\n2\n1\n" + str(startY - roverY))
        else:
            print("2\n1\n" + str(startY - roverY))

    # Positive X Axis
    if roverX > startX and roverY == startY:
        if direction == 0:
            print("3\n1\n" + str(roverX))
        elif direction == 90:
            print("2\n2\n1\n" + str(roverX))
        elif direction == 180:
            print("2\n1\n" + str(roverX))
        else:
            print("1\n" + str(roverX))

    # Negative X Axis
    if roverX < startX and roverY == startY:
        if direction == 0:
            print("2\n1\n" + str(startX - roverX))
        elif direction == 90:
            print("1\n" + str(startX - roverX))
        elif direction == 180:
            print("3\n1\n" + str(startX - roverX))
        else:
            print("2\n2\n1\n" + str(startX - roverX))
