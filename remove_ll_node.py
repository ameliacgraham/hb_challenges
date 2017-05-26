def remove_node(node):
    """Given a node in a linked list, remove it.
    Remove this node from a linked list. Note that we do not have access to
    any other nodes of the linked list, like the head or the tail.
    Does not return anything; changes list in place.
    """

    node.data = node.next.data
    node.next = node.next.next




