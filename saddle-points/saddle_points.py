def saddle_points(matrix):
    # greater than or equal to every element in its row
    # less than or equal to every element in its column

    if len(matrix) == 0:
        return []

    greatest_in_rows = []
    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise ValueError("irregular matrix")
        greatest_in_rows.append(get_maxs(row))

    columns = [get_column(i, matrix) for i in range(len(matrix[0]))]
    smallest_in_columns = []
    for column in columns:
        smallest_in_columns.append(get_mins(column))

    row_coords = []
    for ind, num in enumerate(greatest_in_rows):
        for coord in num:
            row_coords.append((ind + 1, coord + 1))

    col_coords = []
    for ind, num in enumerate(smallest_in_columns):
        for coord in num:
            col_coords.append((coord + 1, ind + 1))

    res = set(row_coords) & set(col_coords)
    return [{"row": row, "column": column} for row, column in res]


def get_column(index, matrix):
    res = [column_value[index] for column_value in matrix]
    return res


def get_mins(arr):
    min_element = min(arr)
    return [ind for ind, i in enumerate(arr) if i == min_element]


def get_maxs(arr):
    max_element = max(arr)
    return [ind for ind, i in enumerate(arr) if i == max_element]
