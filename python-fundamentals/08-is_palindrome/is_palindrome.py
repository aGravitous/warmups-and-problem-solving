def is_palindrome(string):
    """Tests to see if argument is a palindrome."""
    
    i = 0
    j = len(string) - 1
    lcased = string.lower()

    while i < j:
        if lcased[i] != lcased[j]:
            return False
        elif lcased[i] == " ":
            i += 1
        elif lcased[j] == " ":
            j -= 1
        elif lcased[i] == lcased[j]:
            j -= 1
            i += 1
    return True
