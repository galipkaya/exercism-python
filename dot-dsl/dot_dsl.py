NODE, EDGE, ATTR = range(3)


class Node:
    def __init__(self, name, attrs):
        self.name = name
        self.attrs = attrs

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs


class Edge:
    def __init__(self, src, dst, attrs):
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other):
        return (self.src == other.src and
                self.dst == other.dst and
                self.attrs == other.attrs)


class Graph:
    def __init__(self, data=None):
        self.nodes = []
        self.edges = []
        self.attrs = {}

        if data:
            if type(data) != list:
                raise TypeError("error")
            
            for d in data:
                length = len(d)
                if length == 0:
                    raise TypeError("empty")

                data_type = d[0]
                if data_type == NODE:
                    if length != 3:
                        raise ValueError("node")
                    self.nodes.append(Node(d[1], d[2]))
                elif data_type == EDGE:
                    if length != 4:
                        raise ValueError("edge")
                    self.edges.append(Edge(d[1], d[2], d[3]))
                elif data_type == ATTR:
                    if length < 3:
                        raise TypeError("attr")
                    if type(d[1]) != str or type(d[2]) != str:
                        raise ValueError("attr")
                    self.attrs[d[1]] = d[2]
                else:
                    raise ValueError("unknown")
