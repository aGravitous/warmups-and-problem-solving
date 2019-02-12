def multiple_letter_count(str):
    popularities = {}
    for ltr in str:
        popularities[ltr] += 1 if popularities[ltr] else popularities[ltr] = 1
    return popularities