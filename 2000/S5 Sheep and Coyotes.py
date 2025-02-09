# https://dmoj.ca/problem/ccc00s5
# Run on PyPy3 to avoid TLE

number_of_sheep = int(input())

sheep = []

# Avoid floating-point errors by splitting into integer and fractional parts
for _ in range(number_of_sheep):
    x_str = input().strip()
    y_str = input().strip()

    # Process x coordinate
    if '.' in x_str:
        x_parts = x_str.split('.')
        x_int = x_parts[0]
        x_frac = x_parts[1].ljust(2, '0')[:2]
    else:
        x_int = x_str
        x_frac = '00'
    x_scaled = int(x_int) * 100 + int(x_frac)

    # Process y coordinate
    if '.' in y_str:
        y_parts = y_str.split('.')
        y_int = y_parts[0]
        y_frac = y_parts[1].ljust(2, '0')[:2]
    else:
        y_int = y_str
        y_frac = '00'
    y_scaled = int(y_int) * 100 + int(y_frac)

    sheep.append((x_scaled, y_scaled))

eaten_sheep = []

for i in range(0, 100001):
    min_distance_sq = None
    min_sheep_list = []

    for s_x, s_y in sheep:
        dx = i - s_x
        dy = s_y
        distance_sq = dx * dx + dy * dy

        if min_distance_sq is None:
            min_distance_sq = distance_sq
            min_sheep_list = [(s_x, s_y)]
        else:
            if distance_sq < min_distance_sq:
                min_distance_sq = distance_sq
                min_sheep_list = [(s_x, s_y)]
            elif distance_sq == min_distance_sq:
                min_sheep_list.append((s_x, s_y))

    for sheep_pos in min_sheep_list:
        if sheep_pos not in eaten_sheep:
            eaten_sheep.append(sheep_pos)


# format to two decimal places
def format_scaled(coord):
    integer_part = coord // 100
    fractional_part = coord % 100
    return f"{integer_part}.{fractional_part:02d}"


for s_x, s_y in eaten_sheep:
    formatted_x = format_scaled(s_x)
    formatted_y = format_scaled(s_y)

    print(f"The sheep at ({formatted_x}, {formatted_y}) might be eaten.")