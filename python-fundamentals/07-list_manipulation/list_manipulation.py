def list_manipulation(list, command, location, value=0):
    """Using keywords manipulate a list, either removing or adding values from
    the beginning or end of the list."""

    if command == "remove" and location == "end":
        return list.pop()
    elif command == "remove" and location == "beginning":
        return list.pop(0)
    elif command == "add" and location == "end":
        list.append(value)
        return list
    else:
        list.insert(0, value)
        return list