def multiple_letter_count(string):
    """Take in a string and return a dictionary of letter keys with values of
    times they appear in string."""
    count = {}
    for letter in string:
        count[letter] = string.count(letter)
    
    return count
