def read_matrix_func():
    rows, columns = map(int, input().split(", "))
    current_matrix = []

    for row in range(rows):
        row_data = list(map(int, input().split(" ")))
        current_matrix.append(row_data)

    return current_matrix


def get_sum_of_columns():
    matrix = read_matrix_func()
    rows = len(matrix)
    columns = len(matrix[0])
    sum_of_columns = []

    for i in range(columns):
        col_sum = 0
        for j in range(rows):
            col_sum += matrix[j][i]

        sum_of_columns.append(col_sum)

    return sum_of_columns


data = get_sum_of_columns()

for num in data:
    print(int(num))
