def flip_case(string, letter):
    swapped_string = ""
    for character in string:
        if character == letter.lower() or character == letter.upper():
            swapped_string += character.swapcase()
        else:
            swapped_string += character

    return swapped_string