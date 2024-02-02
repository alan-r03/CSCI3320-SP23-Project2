def lowest_index(inputList, target):
    """
    returns the index of the first
    occurence of a target integer

    :param inputList: list of integers
    :param target: integer target
    :return: lowest index of target in
    inputList if it exists, else -1
    """
    currentLowest = -1
    low = 0
    high = len(inputList) - 1

    while low <= high:
        mid = (low + high) // 2
        if inputList[mid] == target:
            currentLowest = mid
        elif inputList[mid] < target:
            low = mid + 1
            continue
        high = mid - 1

    return currentLowest

userList = [1, 2, 3, 3, 4, 5, 10]
targetNumber = 3
print(f"The first index of {targetNumber} is {lowest_index(userList, targetNumber)}.\n")