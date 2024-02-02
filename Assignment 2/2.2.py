def verify_string(inputString):
    """
    returns a bool determined by whether
    the given string contains a valid use
    of brackets or not

    :param inputString: given string
    :return: True if valid, else False
    """
    stack = [] if len(inputString) > 0 else True
    bracketPairs = {'(': ')', '{': '}', '[': ']'}

    for char in inputString:
        if char in bracketPairs.keys():
            stack.append(char)
        elif stack and bracketPairs[stack[-1]] == char:
            stack.pop()
        else:
            return False

    return not stack

userString = "()[]{}"
print(f"The given string is {'valid' if verify_string(userString) else 'not valid'}.\n")