def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('Strands not equal')

    res = [x for ind, x in enumerate(strand_a) if x != strand_b[ind]]
    return len(res)

