ocr_numbers = {
    " _ \n| |\n|_|\n   ": "0",
    "   \n  |\n  |\n   ": "1",
    " _ \n _|\n|_ \n   ": "2",
    " _ \n _|\n _|\n   ": "3",
    "   \n|_|\n  |\n   ": "4",
    " _ \n|_ \n _|\n   ": "5",
    " _ \n|_ \n|_|\n   ": "6",
    " _ \n  |\n  |\n   ": "7",
    " _ \n|_|\n|_|\n   ": "8",
    " _ \n|_|\n _|\n   ": "9"

}


def get_rows(input_grid):
    rows = []
    row = []
    next_num = 3
    for i in range(len(input_grid)):
        row.append(input_grid[i])
        if i == next_num:
            rows.append(row)
            row = []
            next_num += 4
    return rows


def get_numbers(row):
    numbers = []
    for i in range(0, len(row[0]), 3):
        numbers.append([row[0][i:i + 3], row[1][i:i + 3], row[2][i:i + 3], row[3][i:i + 3]])
    return numbers


def convert(input_grid):
    if len(input_grid[0]) % 3 != 0:
        raise ValueError("invalid column count")
    if len(input_grid) % 4 != 0:
        raise ValueError("invalid line count")
    result = ""
    # first get rows
    for row in get_rows(input_grid):
        # then get numbers from row
        for number in get_numbers(row):
            result += ocr_numbers.get("\n".join(number), "?")
        result += ","
    return result[:-1]
