def single_letter_count (string, letter):
    str = string.lower()
    ltr = letter.lower()
    counter = 0

    for char in str:
        if char == ltr:
            counter += 1
    return counter