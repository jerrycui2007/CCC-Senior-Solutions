# https://dmoj.ca/problem/ccc02s5

width = int(input())
height = int(input())
b_initial = int(input())
first_bounce = int(input())

slope = first_bounce / (width - b_initial)
b = -slope * b_initial

done = False

# Start loop at i=1, matching C++ code
for i in range(1, 999999):
    y = slope * (i * width) + b
    x = ((i * height) - b) / slope

    heights = y // height
    actual_height = y - height * heights

    # Check for pockets
    if actual_height < 5 or (height - actual_height) < 5:
        # Check if exactly at corner
        if abs(y - round(y / height) * height) < 1e-9:
            total_bounces = i - 1 + (y // height) - 1
        else:
            total_bounces = i - 1 + (y // height)
        print(int(total_bounces))
        done = True
        break

    widths = x // width
    actual_width = x - width * widths

    if actual_width < 5 or (width - actual_width) < 5:
        if abs(x - round(x / width) * width) < 1e-9:
            total_bounces = i - 1 + (x // width) - 1
        else:
            total_bounces = i - 1 + (x // width)
        print(int(total_bounces))
        done = True
        break

if not done:
    print(0)



