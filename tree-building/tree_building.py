class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def get_node(root, node_id):
    if root.node_id == node_id:
        return root

    for node in root.children:
        child_node = get_node(node, node_id)
        if child_node and child_node.node_id == node_id:
            return child_node
    return None


def BuildTree(records):
    if len(records) == 0:
        return None

    records.sort(key=lambda x: x.record_id)
    if records[-1].record_id != len(records)-1:
        raise ValueError('Tree must be continuous')
    if records[0].parent_id != 0:
        raise ValueError('Root node cannot have a parent')

    root = Node(records[0].record_id)

    for i in range(1, len(records)):
        record = records[i]
        node = get_node(root, record.parent_id)
        if node is None:
            raise ValueError('Cannot find parent node')
        node.children.append(Node(record.record_id))

    return root
