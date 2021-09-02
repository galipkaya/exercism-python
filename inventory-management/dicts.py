import collections


def create_inventory(items):
    '''

    :param items: list - list of items to create an inventory from.
    :return:  dict - the inventory dictionary.
    '''

    return collections.Counter(items)


def add_items(inventory, items):
    '''

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return:  dict - the inventory dictionary update with the new items.
    '''

    for i in items:
        if i in inventory:
            inventory[i] = inventory[i] + 1
        else:
            inventory[i] = 1
    return inventory


def delete_items(inventory, items):
    '''

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to remove from the inventory.
    :return:  dict - updated inventory dictionary with items removed.
    '''

    for i in items:
        if i in inventory and inventory[i] > 0:
            inventory[i] = inventory[i] - 1
    return inventory


def list_inventory(inventory):
    '''

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    '''

    return [(k,v) for k,v in inventory.items() if v != 0]
