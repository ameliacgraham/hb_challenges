def concat_lists(list1, list2):
    """Combine lists."""

    for item in list2:
        list1.append(item)

    return list1

print concat_lists([1, 2, 3, 4, 5], [6, 7])