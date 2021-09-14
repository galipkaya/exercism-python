def knapsack(max_weight, weights, values, weight_length):

    if weight_length == 0 or max_weight == 0:
        return 0

    if weights[weight_length - 1] > max_weight:
        return knapsack(max_weight, weights, values, weight_length - 1)
    else:
        return max(
            values[weight_length - 1] + knapsack(
                max_weight - weights[weight_length - 1], weights, values, weight_length - 1),
            knapsack(max_weight, weights, values, weight_length - 1))


def maximum_value(maximum_weight, items):
    weights = []
    values = []
    for i in items:
        weights.append(i["weight"])
        values.append(i["value"])
    return knapsack(maximum_weight, weights, values, len(weights))
