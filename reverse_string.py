def rev_string(word):
    """Return reverse of string.

    You may NOT use the reversed() function!
    """

    rev = ""
    while word:
        rev += word[-1]
        word = word[:-1]

    print rev

rev_string("porcupine")