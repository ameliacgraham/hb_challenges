def has_more_vowels(word):
    """Does word contain more vowels than non-vowels?"""

    vowel_count = 0
    con_count = 0
    vowels = {'a', 'e', 'i', 'o', 'u'}

    for char in word:
        if char.lower() in vowels:
            vowel_count += 1
        else:
            con_count += 1

    return vowel_count > con_count

print has_more_vowels("hello")
print 5 /2