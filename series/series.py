def slices(series, length):
    total_length = len(series)
    if total_length == 0 or length <= 0 or length > total_length:
        raise ValueError("invalid parameter")

    return [
        series[i:i + length]
        for i in range(total_length)
        if (i + length) <= total_length
    ]
