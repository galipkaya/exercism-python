ONE = "one"
TWO = "two"


def measure(bucket_one, bucket_two, goal, start_bucket):
    def is_bucket_1_filled():
        return b1 == bucket_one

    def is_bucket_2_filled():
        return b2 == bucket_two

    def is_bucket_1_empty():
        return b1 == 0

    def is_bucket_2_empty():
        return b2 == 0

    turn = start_bucket
    if start_bucket == ONE:
        b1 = bucket_one
        b2 = 0
    else:
        b1 = 0
        b2 = bucket_two

    print(b1,b2)
    moves = 1
    while b1 != goal and b2 != goal:
        if is_bucket_2_empty() and goal == bucket_two:
            b2 = bucket_two

        elif is_bucket_1_filled():
            empty = bucket_two - b2
            if empty > b1:
                b2 += b1
                b1 = 0
            else:
                b2 += empty
                b1 -= empty
        elif is_bucket_2_filled():
            b2 = 0
        elif is_bucket_1_empty():
            b1 = bucket_one
        elif is_bucket_2_empty():
            b2 = b1
            b1 = 0
        moves += 1
        print(b1,b2)

        """
        if is_bucket_2_empty():
            b2 = bucket_two
            moves += 1
        elif is_bucket_2_filled():
            b2 -= b1
            b1 = bucket_one
            moves += 1
        elif is_bucket_1_filled():
            b1 = 0
            moves += 1
        """

    if b1 == goal:
        winner = ONE
        other = b2
    else:
        winner = TWO
        other = b1

    return moves, winner, other
