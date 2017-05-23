def time_word(time):
    """Convert time to text"""

    HOURS = ['twelve', 'one', 'two', 'three', 'four', 'five', 'six',
             'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']
    TENS = ['', '', 'twenty', 'thirty', 'forty', 'fifty']

    ONES = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
            'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
            'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

    if time == '00:00':
        return "midnight"

    if time == '12:00':
        return "noon"

    hour, minutes = time.split(':')
    hour = int(hour)
    minutes = int(minutes)

    time_in_words = HOURS[hour % 12] + " "
    if minutes >= 20:
        time_in_words += TENS[minutes / 10] + " " + ONES[minutes % 10]
    elif minutes >= 10:
        time_in_words += ONES[minutes]
    elif minutes > 0:
        time_in_words += "oh " + ONES[minutes]
    else:
        time_in_words += "o'clock"

    return time_in_words.rstrip() + (" pm" if hour >= 12 else " am") 

print time_word('00:00')
print time_word('12:30')
print time_word('00:10')