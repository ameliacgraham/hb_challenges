def pig_latin(phrase):
    """Turn a phrase into pig latin.

    There will be no uppercase letters or punctuation in the phrase.

        >>> pig_latin('hello awesome programmer')
        'ellohay awesomeyay rogrammerpay'
    """

    vowels = {'a', 'e', 'i', 'o', 'u'}
    words = phrase.split()
    pig_words = []

    for word in words:
        if word[0].lower() in vowels:
            pig_word = word + 'yay'
            print pig_word
            pig_words.append(pig_word)
        else:
            pig_word = word[1:] + word[0] + 'ay'
            pig_words.append(pig_word)

    return pig_words

print pig_latin("hello awesome programmer")