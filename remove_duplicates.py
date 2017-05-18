def deduped(items):
    """Return new list from items with duplicates removed in same order."""

    seen = set()

    deduped_items = []
    for item in items:
        if item not in seen:
            deduped_items.append(item)
            seen.add(item)
    return deduped_items

print deduped([1,2,3,3,5,6,6])