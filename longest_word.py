def find_longest_word(words):
    """Return longest word in list of words."""

    # max_length = None

    # for word in words:
    #     char_count = 0
    #     for char in word:
    #         char_count += 1
    #     if char_count > max_length:
    #         max_length = char_count

    # return max_length

    max_length = len(words[0])

    for word in words:
        if max_length < len(word):
            max_length = len(word)

    return max_length

print find_longest_word(['hi', 'hello'])