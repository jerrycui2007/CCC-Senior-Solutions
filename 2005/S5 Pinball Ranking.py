# https://dmoj.ca/problem/ccc05s5
# Question can be cheesed by doing merge sort and counting how many swaps were made
# Submit on PyPy3 to avoid TLE


def merge_sort(array):
    global total_swaps

    array_length = len(array)

    if array_length > 1:
        divisor_index = array_length // 2
        left_side = array[:divisor_index]
        right_side = array[divisor_index:]

        merge_sort(left_side)
        merge_sort(right_side)

        current_left_index = 0
        current_right_index = 0
        counter = 0

        while current_left_index < len(left_side) and current_right_index < len(right_side):
            if left_side[current_left_index] > right_side[current_right_index]:
                array[counter] = right_side[current_right_index]
                current_right_index += 1
                total_swaps += len(left_side) - current_left_index
            else:
                array[counter] = left_side[current_left_index]
                current_left_index += 1
            counter += 1

        while current_left_index < len(left_side):
            array[counter] = left_side[current_left_index]
            counter += 1
            current_left_index += 1

        while current_right_index < len(right_side):
            array[counter] = right_side[current_right_index]
            counter += 1
            current_right_index += 1

    return array


if __name__ == "__main__":
    total_swaps = 0
    scores = []

    games_played = int(input())
    for _ in range(games_played):
        scores.append(int(input()))

    merge_sort(scores)

    total_swaps += games_played

    print(round(total_swaps / games_played, 2))