# https://dmoj.ca/problem/ccc05s3
number_of_matrices = int(input())
matrices = {}
for i in range(number_of_matrices):
    matrices[i] = []
    rows, columns = list(map(int, input().split()))
    for _ in range(rows):
        matrices[i].append(list(map(int, input().split())))


def tensor_product(matrix1, matrix2):
    final_matrix = [[None for _ in range(len(matrix1[0]) * len(matrix2[0]))] for _ in range(len(matrix1) * len(matrix2))]

    for row in range(len(matrix1) * len(matrix2)):
        for column in range(len(matrix1[0]) * len(matrix2[0])):
            final_matrix[row][column] = matrix1[int(row / len(matrix2))][int(column / len(matrix2[0]))] * matrix2[int(row % len(matrix2))][int(column % len(matrix2[0]))]

    return final_matrix


final_matrix = matrices[0]
for i in range(1, number_of_matrices):
    final_matrix = tensor_product(final_matrix, matrices[i])

largest_number = -9e9  # any large number
smallest_number = 9e9
largest_row_sum = -9e9
smallest_row_sum = 9e9
column_sums = [0 for _ in range(len(final_matrix[0]))]

for row in final_matrix:
    row_sum = 0
    for i in range(len(row)):
        if row[i] > largest_number:
            largest_number = row[i]
        if row[i] < smallest_number:
            smallest_number = row[i]
        row_sum += row[i]
        column_sums[i] += row[i]
    if row_sum > largest_row_sum:
        largest_row_sum = row_sum
    if row_sum < smallest_row_sum:
        smallest_row_sum = row_sum

print(largest_number)
print(smallest_number)
print(largest_row_sum)
print(smallest_row_sum)
print(max(column_sums))
print(min(column_sums))
