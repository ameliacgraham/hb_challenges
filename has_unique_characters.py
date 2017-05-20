# def has_unique_chars(word):
#     """Does word contains unique set of characters?"""

#     seen = set()

#     for char in word:
#         if char in seen:
#             return False
#         else:
#             seen.add(char)

#     return True

def has_unique_chars(word):
    """Does word contains unique set of characters?"""

    unique_word = set(word)

    return len(unique_word) == len(word)

print has_unique_chars("hello")