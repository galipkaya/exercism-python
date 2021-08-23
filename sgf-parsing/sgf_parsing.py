class SgfTree:
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for k, v in self.properties.items():
            if k not in other.properties:
                return False
            if other.properties[k] != v:
                return False
        for k in other.properties.keys():
            if k not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for a, b in zip(self.children, other.children):
            if a != b:
                return False
        return True

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        if len(self.children) > 0:
            return f"{self.properties}:{self.children}"
        else:
            return f"{self.properties}"

    def __repr__(self):
        return self.__str__()


def parse(input_string):
    parts = input_string.split(";")

    if len(parts) < 2 or parts[0] == '':
        raise ValueError("wrong format")

    sgf_tree = SgfTree()
    properties = parts[1]
    if properties == ')':
        return sgf_tree

    # properties
    if properties[0].islower():
        raise ValueError("wrong format")

    add_to_map(sgf_tree.properties, properties)

    # children
    for i in range(2, len(parts)):
        add_to_map(sgf_tree.children, parts[i])

    return sgf_tree


def add_to_map(structure_to_add, input_str):

    i = 0
    while i < len(input_str):

        key_name = input_str[i]
        if not key_name.isalpha():
            break
        properties = get_properties(input_str[i+1:])

        if len(properties) == 0:
            raise ValueError("wrong format")
        try:
            # main tree
            if type(structure_to_add) is dict:
                structure_to_add[key_name] = properties
            # children
            else:
                child = SgfTree()
                child.properties[key_name] = properties
                structure_to_add.append(child)
        except IndexError:
            raise ValueError("wrong format")
        i = input_str.index("]", i)
        while input_str[i-1] == "\\":
            i = input_str.index("]", i+1)
        i += 1


def get_properties(input_str):
    if input_str[0] != "[":
        return []

    properties = []
    new_property = ""
    for j in range(0, len(input_str)):
        ch = input_str[j]
        previous_ch = input_str[j-1]
        if ch == "\t":
            ch = " "
        elif ch == "\\":
            continue
        elif ch == "[" and previous_ch != '\\':
            continue
        elif ch == "]" and previous_ch != '\\':
            properties.append(new_property)
            new_property = ""
            if j+1 < len(input_str) and input_str[j+1] != "[":
                break
            continue

        new_property += ch

    return properties
