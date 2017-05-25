def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?"""

    counts = {}
    num_of_odd_occurences = 0

    for char in word:
        counts[char] = counts.get(char, 0) + 1
    for val in counts.values():
        if val % 2 != 0:
            num_of_odd_occurences += 1

    return num_of_odd_occurences <= 1

print is_anagram_of_palindrome('arceaceb')