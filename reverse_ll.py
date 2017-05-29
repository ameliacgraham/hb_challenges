def reverse_linked_list(head):
    """Given LL head node, return head node of new, reversed linked list.
    >>> ll = Node(1, Node(2, Node(3)))
    >>> reverse_linked_list(ll).as_string()
    '321'
    """

    new_head = None
    n = head

    while n:
        print "N: {}".format(n)
        out_head = Node(n.data, n.next)
        n = n.next

    print new_head

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT!\n"
