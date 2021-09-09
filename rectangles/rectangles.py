from itertools import combinations
from math import sqrt


def is_rectangle(points: [tuple]) -> bool:
    x1 = points[0][0]
    x2 = points[1][0]
    x3 = points[2][0]
    x4 = points[3][0]
    y1 = points[0][1]
    y2 = points[1][1]
    y3 = points[2][1]
    y4 = points[3][1]
    cx = (x1 + x2 + x3 + x4) / 4
    cy = (y1 + y2 + y3 + y4) / 4

    dd1 = sqrt(abs(cx - x1)) + sqrt(abs(cy - y1))
    dd2 = sqrt(abs(cx - x2)) + sqrt(abs(cy - y2))
    dd3 = sqrt(abs(cx - x3)) + sqrt(abs(cy - y3))
    dd4 = sqrt(abs(cx - x4)) + sqrt(abs(cy - y4))
    return dd1 == dd2 and dd1 == dd3 and dd1 == dd4;


def get_mid_points(a: tuple, b: tuple) -> [tuple]:
    result = []
    if a[0] == b[0]:
        for i in range(min(a[1], b[1]), max(a[1], b[1])):
            result.append((a[0], i))
    elif a[1] == b[1]:
        for i in range(min(a[0], b[0]), max(a[0], b[0])):
            result.append((i, a[1]))
    return result


def check_lines_correct(strings: [str], points: [tuple]) -> bool:
    if len(points) <= 1:
        return True
    if points[0][0] == points[1][0]:
        # -, +
        return all([strings[p[0]][p[1]] == "-" or strings[p[0]][p[1]] == "+" for p in points])
    else:
        # |, +
        return all([strings[p[0]][p[1]] == "|" or strings[p[0]][p[1]] == "+" for p in points])


def move(a: tuple, b: tuple):
    if a[0] == b[0] or a[1] == b[1]:
        return 1
    return 0


def can_traverse(points: [tuple]) -> bool:
    a = points[0]
    b = points[1]
    c = points[2]
    d = points[3]
    result = 0
    result += move(a, b)
    result += move(a, c)
    result += move(a, d)
    result += move(b, c)
    result += move(b, d)
    result += move(c, d)

    return result == 4


def rectangles(strings):
    points = []
    for i in range(0, len(strings)):
        for j in range(len(strings[i])):
            if strings[i][j] == "+":
                points.append((i, j))

    points = combinations(points, 4)

    result = 0
    for p in points:
        if is_rectangle(p) and can_traverse(p):
            mid_points1 = get_mid_points(p[0], p[1])
            mid_points2 = get_mid_points(p[1], p[3])
            mid_points3 = get_mid_points(p[2], p[3])
            mid_points4 = get_mid_points(p[2], p[0])

            if check_lines_correct(strings, mid_points1) and check_lines_correct(strings, mid_points2) and \
                    check_lines_correct(strings, mid_points3) and check_lines_correct(strings, mid_points4):
                result += 1
                print(p)

    return result
