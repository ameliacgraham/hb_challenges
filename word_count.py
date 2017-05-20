def word_count(phrase):
    """Count words in a sentence, and print in ascending order."""

    word_counts = {}

    for word in phrase.split():
        word_counts[word] = word_counts.get(word, 0) + 1

    counts = [(count, word) for word, count in word_counts.items()]
    counts.sort()

    for count, word in counts:
        print "{}: {}".format(word, count)

word_count("hi hi Hi hello")