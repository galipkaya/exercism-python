def flatten(iterable):
    result = []

    def fill_items(element):
        if element is None:
            return
        
        if isinstance(element, list):
            for e in element:
                fill_items(e)
        else:
            result.append(element)

    for i in iterable:
        fill_items(i)
    return result
