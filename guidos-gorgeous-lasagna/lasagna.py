EXPECTED_BAKE_TIME = 40


# TODO: define the 'PREPARATION_TIME' constant


def bake_time_remaining(elapsed_bake_time):
    """
    :param elapsed_bake_time: int baking time already elapsed
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(layers):
    """
    :param layers: layers of lasagna
    :return: calculated preparation time
    """
    return 2 * layers


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    :param number_of_layers: layers of lasagna
    :param elapsed_bake_time: elapsed time
    :return: total time
    """
    return 2 * number_of_layers + elapsed_bake_time
