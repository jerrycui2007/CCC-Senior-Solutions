# https://dmoj.ca/problem/ccc00s5hard
# Run on PyPy3 to avoid TLE

number_of_sheep = int(input())

sheep = []
for _ in range(number_of_sheep):
    x = int(input())
    y = int(input())
    sheep.append((x, y))

eaten_sheep = set()

for s in sheep:
    s_x, s_y = s
    left = 0.0
    right = 10 ** 6
    feasible = True

    for s_prime in sheep:
        if s == s_prime:
            continue
        sp_x, sp_y = s_prime

        if sp_x == s_x:
            if s_y ** 2 >= sp_y ** 2:
                feasible = False
                break
            continue

        numerator = (sp_x ** 2 + sp_y ** 2) - (s_x ** 2 + s_y ** 2)
        denominator = 2 * (sp_x - s_x)
        x_eq = numerator / denominator

        if denominator > 0:
            if x_eq < left:
                feasible = False
                break
            right = min(right, x_eq)
        else:
            if x_eq > right:
                feasible = False
                break
            left = max(left, x_eq)

        if left > right:
            feasible = False
            break

    left_clamped = max(left, 0.0)
    right_clamped = min(right, 10 ** 6)

    if feasible and left_clamped <= right_clamped:
        eaten_sheep.add(s)

# Sort the sheep by x then y for consistent output
eaten_sheep_sorted = sorted(eaten_sheep, key=lambda coord: (coord[0], coord[1]))

for s_x, s_y in eaten_sheep_sorted:
    print(f"The sheep at ({s_x}, {s_y}) might be eaten.")