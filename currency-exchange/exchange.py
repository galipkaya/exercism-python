def estimate_value(budget, exchange_rate):
    '''

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return:
    '''

    return budget / exchange_rate


def get_change(budget, exchanging_value):
    '''

    :param budget: float - amount of money you own.
    :param exchanging_value: int - amount of your money you want to exchange now.
    :return:
    '''

    return budget - exchanging_value


def get_value(denomination, number_of_bills):
    '''

    :param denomination: int - the value of a bill.
    :param number_of_bills: int amount of bills you received.
    :return:
    '''

    return denomination * number_of_bills


def get_number_of_bills(budget, denomination):
    '''

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return:
    '''

    return budget // denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    '''

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return:
    '''

    exchange_value = estimate_value(budget, exchange_rate * (1.0 + spread / 100))
    bills = get_number_of_bills(exchange_value, denomination)
    return get_value(denomination, bills)

def unexchangeable_value(budget, exchange_rate, spread, denomination):
    """

    :param budget:
    :param exchange_rate:
    :param spread:
    :param denomination:
    :return:
    """
    full_value = estimate_value(budget, exchange_rate * (1.0 + spread / 100))
    exchangeable = exchangeable_value(budget, exchange_rate, spread, denomination)
    return int(full_value - exchangeable)
