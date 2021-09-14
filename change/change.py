def change(coins, amount):
    result = [amount+1] * (amount+1)
    coins_results = [[] for _ in range(amount+1)]

    result[0] = 0

    for i in range(1, amount+1):
        for coin in coins:
            if i >= coin and result[i - coin] + 1 < result[i]:
                result[i] = result[i-coin] + 1
                coins_results[i] = coins_results[i-coin] + [coin]

    if result[amount] == amount+1:
        return []

    return sorted(coins_results[amount])


def find_fewest_coins(coins, amount):
    if amount == 0:
        return []

    if amount < 0:
        raise ValueError("negative amount")

    if all(c > amount for c in coins):
        raise ValueError("wrong amount")

    result = change(coins, amount)

    if not result:
        raise ValueError("no solution")

    return result

