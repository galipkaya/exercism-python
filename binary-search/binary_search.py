def find(search_list, value):
    def _find(l_index, r_index):
        if r_index<0 or l_index >= len(search_list):
            raise ValueError("not found")
        if l_index == r_index:
            if search_list[l_index] == value:
                return l_index
            raise ValueError("not found")
        mid_index = (l_index + r_index)//2
        mid_val = search_list[mid_index]
        if mid_val == value:
            return mid_index
        if mid_val < value:
            return _find(mid_index+1, r_index)
        else:
            return _find(l_index, mid_index-1)

    if not search_list:
        raise ValueError("empty")
    return _find(0, len(search_list)-1)


