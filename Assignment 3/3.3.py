def sumTwo(array, target):
    hashTable = {}
    for index, num in enumerate(array):
        if (target - num) in hashTable:
            return [hashTable[target-num], index]
        hashTable[num] = index
    return [-1, -1]

numArray1 = [2, 7, 11, 15]
numArray2 = [15, 2, 7, 11]
target = 9

print("Return:", sumTwo(numArray1, target))
print("Return:", sumTwo(numArray2, target))