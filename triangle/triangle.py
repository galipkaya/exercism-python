def equilateral(sides):
    return 0 not in sides and \
           sides.count(sides[0]) == 3


def isosceles(sides):
    return 0 not in sides and \
           (sides.count(sides[0]) == 2 or sides.count(sides[1]) == 2)


def scalene(sides):
    return 0 not in sides and \
           sides.count(sides[0]) == 1 and \
           sides.count(sides[1]) == 1
