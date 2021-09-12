def append(list1, list2):
    if not list1:
        return list2
    if list2:
        list1.extend(list2)
    return list1


def concat(lists):
    result = []
    for tmp in lists:
        if tmp:
            result.extend(tmp)
    return result


def filter(function, list):
    return [x for x in list if function(x)]


def length(list):
    return len(list)


def map(function, list):
    return [function(x) for x in list]


def foldl(function, list, initial):
    if not list:
        return initial
    tmp = initial
    for ll in list:
        tmp = function(tmp, ll)
    return tmp


def foldr(function, list, initial):
    if not list:
        return initial
    tmp = initial
    for ll in reversed(list):
        tmp = function(ll, tmp)
    return tmp


def reverse(list):
    list.reverse()
    return list
