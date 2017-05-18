def replace_vowels(chars):
    """Given list of chars, return a new copy, but with vowels replaced by '*'."""

    vowels = set(["a", "e", "i", "o", "u"])

    new_char_list = []
    for char in chars:
        if char.lower() in vowels:
            new_char_list.append("*")
        else:
            new_char_list.append(char)

    return new_char_list


print replace_vowels(['a', 'm', 'e', 'l', 'i', 'a'])